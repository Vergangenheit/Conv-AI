# main file
from flask import Flask, render_template, request, url_for
from forms import ReusableForm
from flask_ngrok import run_with_ngrok
from generate import sample_personality
from model.utils import download_pretrained_model
from database.database import update_history
from database.database import DataBase
import logging
import torch
import config
from transformers import OpenAIGPTLMHeadModel, OpenAIGPTTokenizer, GPT2LMHeadModel, GPT2Tokenizer
from model.train import SPECIAL_TOKENS, build_input_from_segments, add_special_tokens_
from model.interact import sample_sequence
from itertools import chain
from pprint import pformat
import warnings
from argparse import ArgumentParser
import random

def load_model_tokenizer(args):

    global model
    global tokenizer

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__file__)
    logger.info(pformat(args))

    if args.model_checkpoint == "":
        if args.model == 'gpt2':
            raise ValueError("Interacting with GPT2 requires passing a finetuned model_checkpoint")
        else:
            args.model_checkpoint = download_pretrained_model()

    if args.seed != 0:
        random.seed(args.seed)
        torch.random.manual_seed(args.seed)
        torch.cuda.manual_seed(args.seed)

    logger.info("Get pretrained model and tokenizer")
    tokenizer_class, model_class = (GPT2Tokenizer, GPT2LMHeadModel) if args.model == 'gpt2' else (
    OpenAIGPTTokenizer, OpenAIGPTLMHeadModel)
    tokenizer = tokenizer_class.from_pretrained(args.model_checkpoint)
    model = model_class.from_pretrained(args.model_checkpoint)
    model.to(args.device)
    add_special_tokens_(model, tokenizer)

    return model, tokenizer

def generate_from_seed(seed):
    #generate answers from inputted seeds
    
    history = []
    while True:
        #raw_text = input(">>> ")
        while not seed:
            print('Prompt should not be empty!')
            #raw_text = input(">>> ")
        history.append(tokenizer.encode(seed))
        # store encoded seed in db
        db.update_history(tokenizer.encode(seed))
        with torch.no_grad():
            out_ids = sample_sequence(personality, history, tokenizer, model, args)
        # update history in db
        history.append(out_ids)
        db.update_history(out_ids)
        history = history[-(2 * config.max_history + 1):]

        out_text = tokenizer.decode(out_ids, skip_special_tokens=True)
        # print(out_text)
    return out_text

# instantiate app
app = Flask(__name__)

# create homepage
@app.route("/", methods=["GET", "POST"])
def home():
    form = ReusableForm(request.form)
    if request.method == "POST":
        #extract info
        seed = request.form['seed']
        return render_template("seeded.html", input=generate_from_seed(seed=seed))
        
    return render_template("index.html", form=form)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--dataset_path", type=str, default="",
                        help="Path or url of the dataset. If empty download from S3.")
    parser.add_argument("--dataset_cache", type=str, default='./dataset_cache', help="Path or url of the dataset cache")
    parser.add_argument("--model", type=str, default="openai-gpt", help="Model type (openai-gpt or gpt2)",
                        choices=['openai-gpt', 'gpt2'])  # anything besides gpt2 will load openai-gpt
    # parser.add_argument("--model", type=str, default="gpt2", help="Model type (openai-gpt or gpt2)",
    #                     choices=['openai-gpt', 'gpt2'])  # anything besides gpt2 will load openai-gpt
    parser.add_argument("--model_checkpoint", type=str, default="drive/My Drive/GPT-2_Text_Generation/model_checkpoint", help="Path, url or short name of the model")
    # parser.add_argument("--model_checkpoint", type=str, default="", help="Path, url or short name of the model")
    parser.add_argument("--max_history", type=int, default=2, help="Number of previous utterances to keep in history")
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu",
                        help="Device (cuda or cpu)")

    parser.add_argument("--no_sample", action='store_true', help="Set to use greedy decoding instead of sampling")
    parser.add_argument("--max_length", type=int, default=20, help="Maximum length of the output utterances")
    parser.add_argument("--min_length", type=int, default=1, help="Minimum length of the output utterances")
    parser.add_argument("--seed", type=int, default=0, help="Seed")
    parser.add_argument("--temperature", type=int, default=0.7, help="Sampling softmax temperature")
    parser.add_argument("--top_k", type=int, default=0, help="Filter top-k tokens before sampling (<=0: no filtering)")
    parser.add_argument("--top_p", type=float, default=0.9,
                        help="Nucleus filtering (top-p) before sampling (<=0.0: no filtering)")
    global args
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__file__)
    logger.info(pformat(args))
    
    #load model and tokenizer
    global model
    global tokenizer
    model, tokenizer = load_model_tokenizer(args)

    # # sample personality
    global personality
    personality = sample_personality(tokenizer, args)
    logger.info("Selected personality: %s", tokenizer.decode(chain(*personality)))
    #instantiate db connection
    global db
    db = DataBase()
    personality_decoded = [tokenizer.decode(x) for x in personality]
    db.push_personality(personality_decoded)

    #clear history collection in db
    db.clear_history()
    #generate_from_seed(args, model=model, tokenizer=tokenizer, personality=personality, db=db)

    #launch app
    run_with_ngrok(app)
    app.run()

