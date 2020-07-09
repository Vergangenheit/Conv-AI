# 🦄 Building a State-of-the-Art Conversational AI with Transfer Learning

The present repo contains the code accompanying the blog post [🦄 How to build a State-of-the-Art Conversational AI with Transfer Learning](https://medium.com/@Thomwolf/how-to-build-a-state-of-the-art-conversational-ai-with-transfer-learning-2d818ac26313).

This code is a clean and commented code base with training and testing scripts that can be used to train a dialog agent leveraging transfer Learning from an OpenAI GPT and GPT-2 Transformer language model.

This codebase can be used to reproduce the results of HuggingFace's participation to NeurIPS 2018 dialog competition [ConvAI2](http://convai.io/) which was state-of-the-art on the automatic metrics. The 3k+ lines of competition code was distilled in about 250 lines of training code with distributed & FP16 options to form the present repository.

This model can be trained in about one hour on a 8 V100 cloud instance (currently costs about $25) and a pre-trained model is also made available.

## Installation

To install and use the training and inference scripts please clone the repo and install the requirements:



## Pretrained model

We make a pretrained and fine-tuned model available on our S3 [here](https://s3.amazonaws.com/models.huggingface.co/transfer-learning-chatbot/finetuned_chatbot_gpt.tar.gz). The easiest way to download and use this model is just to run the `interact.py` script to talk with the model. Without any argument, this script will automatically download and cache our model.


## Citation

If you use this code in your research, you can cite our NeurIPS CAI workshop [paper](http://arxiv.org/abs/1901.08149):

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
