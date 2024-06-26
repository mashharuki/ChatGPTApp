import openai
import streamlit as st

st.title("simple chat")

user_message = st.text_input(label="どうしましたか？")

if user_message:
    # OpenAI Chat API を使って、ユーザーの入力に対して返答を生成
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system", 
                "content": "You are a helpful assistant."
            },
            {
                "role": "user", 
                "content": user_message
            },
        ],
    )

    st.write(completion)
