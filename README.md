# Web-RAG-Pipeline

Web RAG Pipeline Flow
1.	Define Web Sources
o	Original NCI URL + 2 new authoritative sources:
	American Cancer Society
	CDC
2.	Load Web Documents
o	Use SimpleWebPageReader(html_to_text=True) to fetch and clean HTML content.
o	Convert web pages into text Document objects.
3.	Preview & Validate
o	Check first document snippet to confirm proper loading.
4.	Initialize ChromaDB
o	Persistent local ChromaDB client (./chroma_db).
o	Create a timestamped collection to avoid duplicates.
5.	Build Llama-Index VectorStore
o	Wrap Chroma collection with ChromaVectorStore.
o	Build a VectorStoreIndex from loaded web documents.
o	This embeds documents into vectors and stores them in ChromaDB.
6.	Configure Query Engine
o	Use as_query_engine(response_mode="tree_summarize") to summarize retrieved content.
7.	Run Advanced Summarization Query
o	Query example: Summarize common cancer types, their cellular origins, and early-detection strategies.
o	LLM generates a structured summary with headings for each cancer type.
8.	Output & Validation
o	Print summarized results to confirm accurate content retrieval.
9.	Enhancements Summary
o	Added new authoritative web sources.
o	Cleaned text extraction using SimpleWebPageReader.
o	Indexed expanded documents into ChromaDB.
o	Configured query engine for hierarchical summarization (tree_summarize).
o	Validated pipeline via an advanced summarization query.

In short:

Web Source → Load & Clean → Vectorize → Index → Query Engine → Summarization → Output.
