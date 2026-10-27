"""Index local .txt/.md study notes into a persistent Chroma database."""
from pathlib import Path
import shutil

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
DB_DIR = ROOT / "chroma_db"
COLLECTION = "study_notes"
EMBED_MODEL = "embeddinggemma"


def main():
    paths = sorted(
        path
        for path in DATA_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in {".txt", ".md"}
    )
    if not paths:
        raise SystemExit("data/ folder has no .txt or .md files.")

    documents = []
    for path in paths:
        content = path.read_text(encoding="utf-8").strip()
        if content:
            documents.append(
                Document(
                    page_content=content,
                    metadata={"source": path.relative_to(DATA_DIR).as_posix()},
                )
            )
    if not documents:
        raise SystemExit("All study note files are empty.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=650,
        chunk_overlap=100,
        add_start_index=True,
    )
    chunks = splitter.split_documents(documents)

    # Rebuild rather than duplicating chunks on repeated indexing.
    # Stop the Streamlit app before running this script on Windows.
    if DB_DIR.exists():
        shutil.rmtree(DB_DIR)

    Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=EMBED_MODEL),
        collection_name=COLLECTION,
        persist_directory=str(DB_DIR),
    )
    print(f"Indexed {len(documents)} files / {len(chunks)} chunks")
    print(f"Saved DB: {DB_DIR}")


if __name__ == "__main__":
    main()
