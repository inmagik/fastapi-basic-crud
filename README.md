# Basic FastApi CRUD

This repository contains a basic CRUD example written with FastApi. The full description of the concept behind this code is available [on our blog](https://inmagik.com/en/blog/fastapi-basic-crud)

## Running

```sh
$ git clone git@github.com:inmagik/fastapi-basic-crud.git
$ cd fastapi-basic-crud
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ uvicorn items_app.main:app --reload
```