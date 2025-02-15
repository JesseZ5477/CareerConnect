import nest_asyncio
import os
from llama_parse import LlamaParse
from pathlib import Path
from llama_index import VectorStoreIndex
from llama_index.core import Document
from DBTools.DB_Utils import get_index_path
from CareerConnect.Llama.ExtractMetadata import *


# Read files by files paths and parse file by using LlamaParse
def parse_files(pdf_files):
    """Function to parse the pdf files using LlamaParse in markdown format"""

    parser = LlamaParse(
        result_type="markdown",  # "markdown" and "text" are available
        num_workers=4,  # if multiple files passed, split in `num_workers` API calls
        verbose=True,
    )

    documents = []

    for index, pdf_file in enumerate(pdf_files):
        print(f"Processing file {index + 1}/{len(pdf_files)}: {pdf_file}")
        # Parsing and chunking pdf
        # document type object has text and metadata fields
        docs = parser.load_data(pdf_file)
        # Updating metadata with filepath
        for doc in docs:
          doc.metadata.update({'filepath': pdf_file})
        documents.append(docs)

    # documents is a list of lists of document type object
    # e.g. [[Doc1 chunk1, Doc1 chunk2], [Doc2 chunk1, Dock2 chunk2, Doc2 chunk3]]
    return documents

# function to extract metadata from parsed chunks
# documents become list of document, transformed from list of lists of documents
# e.g. [Doc1, Doc2]
def extract_metadata(documents):
    updated_documents = []
    for document_chunks in documents:
        updated_document = update_metadata(document_chunks)
        updated_documents.append(updated_document)
    return updated_documents



# initialize vector store index by documents
def create_vector_store(documents):
    index = VectorStoreIndex.from_documents(documents)

    # Or choose other vector store like PineCone
    # index = VectorStoreIndex.from_documents(
    #     documents, storage_context=storage_context
    # )

    # save vector store
    ...
    # save vector store path to database
    ...

    return index

# load vector store index from disk
def load_vector_store(mydb, job_id):
    index_path = get_index_path(mydb, job_id)
    return VectorStoreIndex.load_from_disk(index_path)


# save vector store index to disk
def save_vector_store(index):
    index_path = Path("index.json")
    index.storage_context.persist(index_path)

    # save vector store path to database
    ...
    
    return index_path