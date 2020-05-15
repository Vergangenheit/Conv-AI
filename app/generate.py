from model.interact import sample_sequence, get_dataset
import torch
import config
import random
from database import database


def sample_personality(tokenizer, args):
    #generate a personality to be uploaded on the home page
    global personality
    dataset = get_dataset(tokenizer, args.dataset_path, args.dataset_cache)
    personalities = [dialog["personality"] for dataset in dataset.values() for dialog in dataset]
    personality = random.choice(personalities)
    personality = [tokenizer.decode(x) for x in personality]
    database.push_personality(personality)

    return personality

def generate_from_seed(model, tokenizer, personality, seed):
    #generate answers from inputted seeds
    
    history = []
    while True:
        if seed is "" or None:
            print('Prompt should not be empty!')
        history.append(tokenizer.encode(seed))
        with torch.no_grad():
            out_ids = sample_sequence(personality, history, tokenizer, model)
        history.append(out_ids)
        history = history[-(2 * config.max_history + 1):]
        out_text = tokenizer.decode(out_ids, skip_special_tokens=True)

    return history, out_text




