# Fasthtml template

I use this template for rapid PoC of simple web application based on fasthtml, fastlite, htmx

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

## For Cursor users

Add to Cursor docs:
* https://docs.fastht.ml/llms-ctx.txt
