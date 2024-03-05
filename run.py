import logging

import sys

import os
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(stream=sys.stdout, level=logging.INFO)


logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))




from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.llms.huggingface import HuggingFaceLLM

from llama_index.core import Settings



documents = SimpleDirectoryReader("/home/ubuntu/Gemma-RAG/pdfs").load_data()



from llama_index.embeddings.fastembed import FastEmbedEmbedding



embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.embed_model = embed_model

Settings.chunk_size = 128



from llama_index.core import PromptTemplate
system_prompt = "You are a Q&A assistant. Your goal is to answer questions as accurately as possible based on the instructions and context provided."
query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")



from huggingface_hub.hf_api import HfFolder 
HfFolder.save_token(os.getenv('HF_KEY'))


import torch
llm = HuggingFaceLLM(

    context_window=4096,

    max_new_tokens=128,

    generate_kwargs={"temperature": 0.7, "do_sample": False},

    system_prompt=system_prompt,

    query_wrapper_prompt=query_wrapper_prompt,

    tokenizer_name="google/gemma-2b-it",

    model_name="google/gemma-2b-it",

    device_map="auto",

    tokenizer_kwargs={"max_length": 4096},

    model_kwargs={"torch_dtype": torch.float16}

)



Settings.llm = llm
Settings.chunk_size = 128

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

def predict(input, history):

  response = query_engine.query(input)

  return str(response)

import gradio as gr
gr.ChatInterface(predict).launch(share=True)