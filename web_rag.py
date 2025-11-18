import time
from hashlib import sha256

# Import the reader that will fetch and parse web pages
# Updated import path for latest LlamaIndex versions
from llama_index.readers.web import SimpleWebPageReader

# ChromaDB + Llama Index imports
import chromadb
# Updated ChromaVectorStore import
from llama_index.vector_stores.chroma import ChromaVectorStore
# Updated LlamaIndex core import
from llama_index.core import VectorStoreIndex


def main():
    # -----------------------------
    # 1) Define URLs to index
    # -----------------------------
    urls = [
        "https://www.cancer.gov/about-cancer/understanding/what-is-cancer",
        "https://www.cancer.org/cancer/types/common-types-of-cancer.html",
        "https://www.cdc.gov/cancer/dcpc/about/what-is-cancer.htm",
    ]

    # -----------------------------
    # 2) Read web documents
    # -----------------------------
    # Instantiate the web reader with html_to_text=True to get clean text
    reader = SimpleWebPageReader(html_to_text=True)

    print("Loading web pages (this may take a moment)...")
    web_documents = reader.load_data(urls=urls)
    print(f"Loaded {len(web_documents)} web documents from the specified URLs.")

    if len(web_documents) == 0:
        print("No documents were loaded. Exiting.")
        return

    # Preview the first document (small preview)
    print("\nFirst document preview (first 200 chars):")
    print(web_documents[0].text[:200] + "\n")

    # -----------------------------
    # 3) Initialize persistent ChromaDB client and collection
    # -----------------------------
    # Use a timestamped collection name to avoid accidental duplicates when re-running
    collection_name = f"web_cancer_collection_{int(time.time())}"

    # Create a persistent client. This creates/uses a local ChromaDB at ./chroma_db
    client = chromadb.PersistentClient(path="./chroma_db")

    # Create (or get) collection. We intentionally create a new collection name so
    # re-running the script won't append duplicates to an existing collection.
    chroma_collection = client.get_or_create_collection(collection_name)

    print(f"Using Chroma collection: {collection_name}")

    # -----------------------------
    # 4) Wrap the Chroma collection for Llama-Index and re-index
    # -----------------------------
    # Initialize Llama-Index's ChromaVectorStore wrapper with the collection
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    # Build a VectorStoreIndex from the web documents. This will embed each document
    # and add vectors to the Chroma collection.
    print("Indexing documents into ChromaDB (this may take a while depending on your embeddings setup)...")
    web_index = VectorStoreIndex.from_documents(
        web_documents,
        vector_store=vector_store
    )

    print("Indexing complete. Vector store now contains vectors for the provided web documents.")

    # -----------------------------
    # 5) Create a query engine that summarizes results
    # -----------------------------
    # 'tree_summarize' mode asks the index to assemble a hierarchical summary of
    # retrieved content. You can change response_mode to other supported modes.
    web_query_engine = web_index.as_query_engine(response_mode="tree_summarize")

    # -----------------------------
    # 6) Perform an advanced summarization query
    # -----------------------------
    advanced_query = (
        "Summarize the common types of cancer described in the indexed web pages, "
        "explain how these cancers typically begin (cellular origin / tissue of origin), "
        "and highlight any preventative or early-detection strategies mentioned. "
        "Please structure the summary with clear headings for each cancer type."
    )

    print("\nRunning advanced summarization query...")
    response_web_summarized = web_query_engine.query(advanced_query)

    # The returned `response_web_summarized` is typically a response object with a
    # textual summary representation when printed.
    print("\n--- Summarized Response ---\n")
    print(response_web_summarized)

    # -----------------------------
    # 7) Final summary of enhancements to the pipeline
    # -----------------------------
    enhancements_summary = (
        "Enhancements made:\n"
        "- Added 2 new authoritative web sources about cancer (American Cancer Society, CDC)\n"
        "- Loaded cleaned text of the new web pages using SimpleWebPageReader\n"
        "- Created a new persistent ChromaDB collection and indexed the expanded documents\n"
        "- Configured the query engine to summarize retrieved documents (tree_summarize)\n"
        "- Executed an advanced summarization query to validate the pipeline\n"
    )

    print("\n--- Pipeline Enhancements Summary ---\n")
    print(enhancements_summary)


if __name__ == "__main__":
    main()
