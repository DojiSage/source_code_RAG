from git import Repo
from langchain.text_splitter import Language
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain


#clone any github repositoy
def load_repo(repo_path):
    loader = GenericLoader.from_filesystem(repo_path,
                                        glob = "**/*",
                                       suffixes=[".py"],
                                       parser = LanguageParser(language=Language.PYTHON, parser_threshold=500)
                                        )
    
    documents = loader.load()

    return documents




#Creating text chunks 
def text_splitter(documents):
    documents_splitter = RecursiveCharacterTextSplitter.from_language(language = Language.PYTHON,
                                                             chunk_size = 2000,
                                                             chunk_overlap = 200)
    
    text_chunks = documents_splitter.split_documents(documents)

    return text_chunks



#loading embeddings model
def load_embedding():
    embeddings=OpenAIEmbeddings(disallowed_special=())
    return embeddings