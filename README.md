# Fasthtml template

This template provides a quick setup for building simple web application prototypes (PoCs) using Fasthtml, Fastlite, and HTMX. It is designed for rapid development, helping you streamline the process of testing and iterating on ideas.

## Features

- **DDD-Ready Folder Structure**: Organized to support Domain-Driven Design. See details in [`doc/repo_structure.md`](doc/repo_structure.md).
- **User Story-Driven Development**: Begin with user stories for focused development. Reference [`doc/user_story.md`](doc/user_story.md).
- **Pre-Configured Testing and Code Quality**: Includes tests, pre-commit hooks, and linters, all set up for streamlined quality assurance.
- **Cursor-Ready Environment**: `.cursorrules` and documentation links included for immediate cursor customization.

## Install

* TODO add creating from template and renaming instructions/scripts
* TODO rename TEMPLATE_DB_PATH and db name

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
