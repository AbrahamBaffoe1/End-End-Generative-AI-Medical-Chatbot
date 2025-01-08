from src.helper import load_pdf, get_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "einseinnmedicalchatbot"

# Create index if it doesn't exist
try:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
except Exception as e:
    print(f"Index might already exist: {e}")

# Load and process data
extracted_data = load_pdf(data_path='Data/')
embeddings = get_embeddings()

# Create vector store
vector_store = LangchainPinecone.from_documents(
    documents=extracted_data,
    embedding=embeddings,
    index_name=index_name
)

print("Data successfully loaded and indexed in Pinecone")
