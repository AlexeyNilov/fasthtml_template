# Fasthtml template

This template provides a quick setup for building simple web application prototypes (PoCs) using Fasthtml, Fastlite, and HTMX. It is designed for rapid development, helping you streamline the process of testing and iterating on ideas.

## Install

TODO add creating from template and renaming
TODO rename TEMPLATE_DB_PATH and db name

```
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements_dev.txt
pre-commit install
python -m coverage run -m pytest test/test_*.py
python -m coverage html -i --omit=conf/settings.py
mypy .
```

## Run

```
cd ui && uvicorn main:app --reload
```

## For Cursor users

Add to Cursor docs:
* https://docs.fastht.ml/llms-ctx.txt
* https://answerdotai.github.io/fastlite/index.html.md
* https://htmx.org/docs/
