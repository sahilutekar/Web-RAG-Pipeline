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


┌───────────────┐
│   Web Sources │
│  (URLs list)  │
└───────┬───────┘
        │
        ▼
┌────────────────┐
│ Load & Clean   │
│ (SimpleWebPage │
│ Reader)        │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ Vectorize Docs │
│ (Embeddings)   │
└───────┬────────┘
        │
        ▼
┌─────────────────────┐
│ Index in ChromaDB   │
│ (Persistent Storage)│
└───────┬─────────────┘
        │
        ▼
┌─────────────────────┐
│ Query Engine Setup  │
│ (tree_summarize)    │
└───────┬─────────────┘
        │
        ▼
┌─────────────────────┐
│ Run Advanced Query  │
│ (Summarization)     │
└───────┬─────────────┘
        │
        ▼
┌─────────────────────┐
│ Summarized Output   │
│ (Structured Text)   │
└─────────────────────┘


Output glimpse 
--- Summarized Response ---

 Common Types of Cancer
---------------------

### Breast Cancer
Breast cancer typically begins in the breast tissue. It is the most common type of cancer in women and the second most common type of cancer in men. Early detection through regular mammograms and self-exams can increase the chances of successful treatment.

### Lung Cancer
Lung cancer typically begins in the lung tissue. It is the leading cause of cancer death in both men and women. Early detection through regular chest X-rays and CT scans can increase the chances of successful treatment.

### Colorectal Cancer
Colorectal cancer typically begins in the colon or rectum. It is the third most common type of cancer in both men and women. Early detection through regular colonoscopies and fecal occult blood testing can increase the chances of successful treatment.

### Prostate Cancer
Prostate cancer typically begins in the prostate gland. It is the most common type of cancer in men. Early detection through regular prostate-specific antigen (PSA) tests and digital rectal exams can increase the chances of successful treatment.

### Melanoma
Melanoma typically begins in the skin. It

--- Pipeline Enhancements Summary ---

Enhancements made:
- Added 2 new authoritative web sources about cancer (American Cancer Society, CDC)
- Loaded cleaned text of the new web pages using SimpleWebPageReader
- Created a new persistent ChromaDB collection and indexed the expanded documents
- Configured the query engine to summarize retrieved documents (tree_summarize)
- Executed an advanced summarization query to validate the pipeline

