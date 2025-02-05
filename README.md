# ActionEngine Backend

This repository contains the backend for the ActionEngine project.

This is originally built off of [browser-use/web-ui](https://github.com/browser-use/web-ui), but modified to fit our usecase.

## Getting Started

Pre-requisites:

- uv

venv

```bash
uv venv --python 3.11
source venv/bin/activate
```

Set up vscode by hitting CTRL+P and typing `>Python: Select Interpreter` and selecting the venv python.

Install dependencies

```bash
uv pip install -r requirements.txt
```

Symlink the Google Chrome binary to your local bin directory. We reference this in supervisord.conf and expect that `google-chrome` is in your path.

```bash
sudo ln -s /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome /usr/local/bin/google-chrome
```
