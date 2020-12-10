# 🦄 Building a State-of-the-Art Conversational AI with Transfer Learning

The present repo forked the code accompanying the blog post [🦄 How to build a State-of-the-Art Conversational AI with Transfer Learning](https://medium.com/@Thomwolf/how-to-build-a-state-of-the-art-conversational-ai-with-transfer-learning-2d818ac26313).

I added a Flask app to generate a Conversational AI prototype with the help of Javascript and Firebase database. Currently the code requires a GPU and supports only the OpenAIGPT language model. 

## Installation

To install and use the training and inference scripts please clone the repo and install the requirements:



## Pretrained model

We make a pretrained and fine-tuned model available on our S3 [here](https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/finetuned_chatbot_gpt.tar.gz). The easiest way to download and use this model is just to run the `interact.py` script to talk with the model. Without any argument, this script will automatically download and cache our model.


## Citation


```bash
@article{DBLP:journals/corr/abs-1901-08149,
  author    = {Thomas Wolf and
               Victor Sanh and
               Julien Chaumond and
               Clement Delangue},
  title     = {TransferTransfo: {A} Transfer Learning Approach for Neural Network
               Based Conversational Agents},
  journal   = {CoRR},
  volume    = {abs/1901.08149},
  year      = {2019},
  url       = {http://arxiv.org/abs/1901.08149},
  archivePrefix = {arXiv},
  eprint    = {1901.08149},
  timestamp = {Sat, 02 Feb 2019 16:56:00 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1901-08149},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
## ToDo

Add code to plug a GPT2 pretrained model and to fine tune one as well.
