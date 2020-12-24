An app to make sentence cards creation while reading a visual novel easier

# Features

- capture media (screenshots/audio recording) so it can be used within anki
- read text from clipboard
- create anki card through the anki api

# Status

This project is in active development.

# Getting started

Install anki connect and pipenv

```bash
pipenv install
python -m anki_vn_util
```

(Optional) build an executable

```bash
pyinstaller -F -n anki_vn_util  anki_vn_util/__main__.py
```