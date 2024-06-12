import streamlit as st
from langchain.chat_models import ChatOpenAI
from llama_index import ServiceContext, SQLDatabase
from llama_index.indices.struct_store import NLSQLTableQueryEngine
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.DEBUG)
# データベースファイル
DB_FILE = "sample.db"

st.title("Text-to-SQL")

question = st.text_input(label="質問")

if question:
    # モデルを読み込む
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    # langchainのServiceContextを作成
    service_context = ServiceContext.from_defaults(llm=llm)
    # SQLiteデータベースを作成
    engine = create_engine(f"sqlite:///{DB_FILE}")
    sql_database = SQLDatabase(engine)
    # NLSQLTableQueryEngineを作成
    query_engine = NLSQLTableQueryEngine(
        sql_database=sql_database,
        service_context=service_context
    )
    # 質問を解析してSQLを生成(内部でSQLが実行される)
    response = query_engine.query(question)
    st.info(response.metadata["sql_query"])
    st.info(response.metadata["result"])
    st.success(response.response)
