import streamlit as st
import tempfile
from pathlib import Path
from langchain.chat_models import ChatOpenAI
from llama_index import ServiceContext, VectorStoreIndex
from llama_index.readers.file.docs_reader import PDFReader
import logging

logging.basicConfig(level=logging.DEBUG)

st.title("PDFへのQ&A")
# セッションステートからインデックスを取得
index = st.session_state.get("index")

# ファイルがアップロードされたときに呼び出される関数


def on_change_file():
    if "index" in st.session_state:
        # インデックスを削除
        st.session_state.pop("index")


uploaded_file = st.file_uploader(
    label="Q&A対象のファイル",
    type="pdf",
    on_change=on_change_file
)

# ファイルがアップロードされたときに、ファイルを読み込んでインデックスを作成
if uploaded_file and index is None:
    with st.spinner(text="準備中..."):
        with tempfile.NamedTemporaryFile() as f:
            f.write(uploaded_file.getbuffer())

            documents = PDFReader().load_data(file=Path(f.name))
            # GPT-3.5 Turbo を使用してインデックスを作成
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
            # サービスコンテキストを作成(llmindexは langchain の ChatOpenAI を使用しているため、llm を渡す必要がある)
            service_context = ServiceContext.from_defaults(llm=llm)
            # ドキュメントからインデックスを作成
            index = VectorStoreIndex.from_documents(
                documents=documents, service_context=service_context
            )
            st.session_state["index"] = index

if index is not None:
    question = st.text_input(label="質問")

    if question:
        with st.spinner(text="考え中..."):
            # クエリエンジンを作成
            query_engine = index.as_query_engine()
            answer = query_engine.query(question)
            # 回答を表示
            st.write(answer.response)
            st.info(answer.source_nodes)
