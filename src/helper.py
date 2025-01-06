#  create a Simpliefied Function FOR THE CHATBOT 


# IMPROTS NEEDED TO RUN 
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import streamlit as st
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
 

#  FUNCTIONS NEEDED TO RUN - Extracr the data from the PDF File and load it 

def load_pdf(file):
    loader = DirectoryLoader(data,
                            glob='*.pdf',
                            loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

#  fucntion to split the loaded data extracted - Split the Data into text chuncks

def split_data(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


# Download the Embeddding from HuggingFace 

def get_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
