# ChatGPTApp
ChatGPTを使ったサンプルアプリケーション学習用のリポジトリです。

## poetrypoetryよるプロジェクトの初期化

```bash
poetry init
```

設定

```bash
poetry config virtualenvs.in-project true --local
```

poetryでpythonコマンドを実行する。

```bash
poetry run python --version
```

poetryでライブラリをインストール

```bash
poetry add streamlit@1.25.0
```

streamlitで実行する方法

```bash
poetry run streamlit run home.py
```

## OpenAI API 実行結果

```json
{
"id":"chatcmpl-9Yw30bPDd1kafZqxZNIRnSAd1bpqV"
"object":"chat.completion"
"created":1718113314
"model":"gpt-3.5-turbo-0125"
"choices":[
0:{
"index":0
"message":{
"role":"assistant"
"content":"こんにちは、近藤晴輝さん！私はアシスタントです。お手伝いできることがあればお知らせくださいね。"
}
"logprobs":NULL
"finish_reason":"stop"
}
]
"usage":{
"prompt_tokens":42
"completion_tokens":44
"total_tokens":86
}
"system_fingerprint":NULL
}
```

### 参考文献
1. [streamlit](https://streamlit.io/)
2. [Dev Containerを使ってみよう](https://zenn.dev/bells17/articles/devcontainer-2024)
3. [PythonのコードフォーマッターのBlackの使い方](https://book.st-hakky.com/hakky/application-python-black/)