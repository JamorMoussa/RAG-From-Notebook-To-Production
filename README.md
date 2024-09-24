# RAG From Notebook To Production

This is an implimentation of the RAG Model for Question Answering - QA


## 01. Requirements

- Python 3.8 or later.

### 1.1 Install  MiniConda

1. Download and install MiniConda from [https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)

2. Create a new envirorement using the following command:

```bash
$ conda create -n rag-app-env python=3.8
```

3. You need to activate the enviroment:
```bash
$ conda activate rag-app-env
```

### 1.2 Install Requirements:

To install all requirements, run the following command: 
```bash
$ pip install -r requirements.txt
```

### 1.3 Setup the enviroment variables

```bash
$ cp .env.example .env
```

Set up you enviroment varibales in the `.env`. Like `OPENAI_API_KEY` value.