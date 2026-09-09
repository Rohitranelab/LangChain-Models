from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions = 32)

documents = [
    "Delhi is the captial of India", 
    "Kolkata is the captial of West Bengal",
    "Paris is the captial of France"
]
result = embeddings.embed_documents(documents)

print(str(result))