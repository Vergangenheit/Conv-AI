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
    # decode personality to be stored to db
    # personality_decoded = [tokenizer.decode(x) for x in personality]
    # database.push_personality(personality_decoded)

    return personality

def generate_from_seed_old(args, model, tokenizer, personality, db):
    #generate answers from inputted seeds
    
    history = []
    while True:
        raw_text = input(">>> ")
        while not raw_text:
            print('Prompt should not be empty!')
            raw_text = input(">>> ")
        history.append(tokenizer.encode(raw_text))
        # store encoded seed in db
        db.update_history(tokenizer.encode(raw_text))
        with torch.no_grad():
            out_ids = sample_sequence(personality, history, tokenizer, model, args)
        # update history in db
        history.append(out_ids)
        db.update_history(out_ids)
        history = history[-(2 * config.max_history + 1):]

        out_text = tokenizer.decode(out_ids, skip_special_tokens=True)
        # print(out_text)
    return out_text

def generate_from_seed(model, tokenizer, personality, seed, db, args):
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







