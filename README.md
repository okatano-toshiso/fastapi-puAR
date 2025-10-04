# 🚀 FastAPI-puAR

FastAPI-puAR は、**FastAPI** と **Hypercorn** を使用した軽量・高速な Python Web API サーバーです。  
このプロジェクトは、モダンな非同期 Web アプリケーション開発のベースとして利用できます。

---

## 📖 目次

- [概要](#概要)
- [主な機能](#主な機能)
- [環境構築](#環境構築)
- [実行方法](#実行方法)
- [ディレクトリ構成](#ディレクトリ構成)
- [デプロイ](#デプロイ)
- [ライセンス](#ライセンス)
- [参考リンク](#参考リンク)

---

## 🧩 概要

FastAPI-puAR は、Python 3 と FastAPI をベースに構築された API サーバーです。  
開発・検証・本番環境での利用を想定しており、**Railway** などのクラウド環境にも簡単にデプロイできます。

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-NvLj4?referralCode=CRJ8FE)

---

## ✨ 主な機能

- ⚡ **FastAPI** による高速な非同期 API 処理  
- 🌀 **Hypercorn** による ASGI サーバー実行  
- 🧱 **Alembic** によるデータベースマイグレーション対応  
- 🧰 **環境変数管理** による柔軟な設定  
- 🧪 **開発モード** でのホットリロード対応  

---

## 🛠 環境構築

### 1. リポジトリをクローン

```bash
git clone https://github.com/your-username/fastapi-puAR.git
cd fastapi-puAR
```

### 2. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### 3. 環境変数を設定

`.env` ファイルを作成し、必要な設定を記述します。

例:
```env
DATABASE_URL=sqlite:///./test.db
```

---

## ▶️ 実行方法

### 開発モードで起動

```bash
hypercorn app.main:app --reload
```

### 本番モードで起動

```bash
hypercorn app.main:app
```

ブラウザで以下にアクセスして動作確認できます：

👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 ディレクトリ構成

```
fastapi-puAR/
├── app/
│   ├── main.py          # エントリーポイント
│   ├── crud.py          # データ操作ロジック
│   ├── database.py      # DB接続設定
├── alembic/             # マイグレーション設定
├── requirements.txt     # 依存パッケージ
├── LICENSE.md           # ライセンス情報
└── README.md            # 本ドキュメント
```

---

## ☁️ デプロイ

Railway を使用して簡単にデプロイできます。

1. Railway アカウントを作成  
2. 「Deploy on Railway」ボタンをクリック  
3. 自動的に環境が構築され、アプリがデプロイされます

---

## 📜 ライセンス

このプロジェクトは [MIT License](./LICENSE.md) のもとで公開されています。

---

## 🔗 参考リンク

- [FastAPI 公式ドキュメント](https://fastapi.tiangolo.com/)
- [Hypercorn ドキュメント](https://hypercorn.readthedocs.io/)
- [GitHub README 書き方ガイド](https://docs.github.com/ja/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Qiita: READMEの書き方まとめ](https://qiita.com/dfalcon0001/items/843b93d90f21b9e99d50)
- [C++ Learning: READMEの作り方](https://cpp-learning.com/readme/)
