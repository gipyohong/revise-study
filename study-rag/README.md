# 📚 Study RAG — 나만의 AI 공부 도우미

LangChain, Ollama, Chroma, Streamlit을 활용하여 만든 **로컬 RAG(검색 증강 생성) 챗봇** 프로젝트입니다.

`.txt` 및 `.md` 형식의 공부 자료를 등록하고, 해당 자료를 검색하여 AI가 질문에 답변하도록 구현했습니다.

## 🛠️ 실행 환경

- 운영체제: Windows
- 개발 환경: VS Code
- 패키지 관리: uv
- LLM: Ollama (Qwen3.5 4B)
- 임베딩 모델: EmbeddingGemma
- 벡터 데이터베이스: Chroma
- 웹 인터페이스: Streamlit

## 🚀 설치 및 실행 방법

### 1. Ollama 설치

Python 코드를 실행할 컴퓨터에 Ollama를 설치하고 실행합니다.

### 2. AI 모델 다운로드

터미널에서 다음 명령어를 실행합니다.

```bash
ollama pull qwen3.5:4b-q4_K_M
ollama pull embeddinggemma
```

### 3. Python 패키지 설치

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
uv sync
```

### 4. 공부 자료 추가

`data/` 폴더에 UTF-8 인코딩의 `.txt` 또는 `.md` 파일을 추가하거나 수정합니다.

### 5. 벡터 데이터베이스 생성

```bash
uv run python index.py
```

등록한 공부 자료를 분할하고 임베딩하여 Chroma 벡터 데이터베이스에 저장합니다.

### 6. 챗봇 실행

```bash
uv run streamlit run app.py
```

터미널에 표시된 로컬 주소를 브라우저에서 열면 챗봇을 사용할 수 있습니다.

## ⚠️ 주의사항

- 공부 자료를 수정한 경우 `index.py`를 다시 실행해야 합니다.
- `index.py`는 기존 `chroma_db/` 폴더를 초기화하므로, 재실행하기 전에 Streamlit을 종료해야 합니다.
- 재인덱싱 후에는 Streamlit을 다시 실행하거나 캐시를 초기화해야 합니다.
- 현재 버전은 PDF 파일 검색을 지원하지 않습니다.
- 이전 대화를 기억하는 기능은 없으며, 각 질문을 독립적으로 검색합니다.
- AI가 제시하는 출처 표시는 자동 검증되지 않으므로, 화면에 표시된 원문을 직접 확인해야 합니다.
- `.venv/`와 `chroma_db/`는 로컬에서 생성되는 폴더이므로 GitHub에 업로드하지 않는 것을 권장합니다.

## 🎯 향후 개발 계획

- [ ] PDF 및 Jupyter Notebook 파일 검색 지원
- [ ] 이전 대화를 기억하는 멀티턴 챗봇
- [ ] 검색 품질 평가 (Hit@k, Recall@k, MRR)
- [ ] LangGraph 기반 검색 및 답변 개선
- [ ] 검색 결과의 관련성 검증 기능
