# Study RAG

A minimal local RAG chatbot for `.txt` and `.md` study notes, using LangChain, Ollama, Chroma and Streamlit.

## Windows / VS Code / uv

1. Install and start Ollama on the machine running the Python code.
2. `ollama pull qwen3.5:4b-q4_K_M`
3. `ollama pull embeddinggemma`
4. Open a terminal in this folder and run `uv sync`.
5. Add or edit UTF-8 `.txt` / `.md` files under `data/`.
6. `uv run python index.py`
7. `uv run streamlit run app.py`
8. Open the localhost URL displayed by Streamlit.

Stop Streamlit before re-running `index.py`, which resets the project-local `chroma_db/` directory. Restart Streamlit or clear its cache after reindexing.

This MVP does not support PDF indexing or multi-turn conversational memory. It searches the current question independently. The cited excerpts are unverified LLM citations; inspect the excerpts shown in the UI.

`chroma_db/` and `.venv/` are generated locally and should not be committed.
