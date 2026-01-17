from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=100)

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



DATA_DIR = Path("data")

all_docs = []

for pdf in DATA_DIR.glob("*.pdf"):
    loader = PyPDFLoader(str(pdf))
    docs = loader.load()
    all_docs.extend(docs)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)


chunks = splitter.split_documents(all_docs)

print(f"Loaded {len(all_docs)} pages")
print(f"Created {len(chunks)} chunks")

