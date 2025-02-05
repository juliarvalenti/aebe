# ActionEngine Backend

This repository contains the backend for the ActionEngine project.

This is originally built off of [browser-use/web-ui](https://github.com/browser-use/web-ui), but modified to fit our usecase.

Do not use the Dockerfile for now. It is not up to date. The instructions below are for MacOS.

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

Update .env file with the correct values. Add your own values for OPENAI_API_KEY, OPENAI_ENDPOINT, OPENAI_MODEL_NAME

```bash
cp .env.example .env
```

Ensure Google Chrome is installed in the default location `/Applications/Google Chrome.app`

Clone NoVNC into the `opt` directory

````bash
git clone https://github.com/novnc/noVNC.git /opt/novnc \
    && git clone https://github.com/novnc/websockify /opt/novnc/utils/websockify \
    && ln -s /opt/novnc/vnc.html /opt/novnc/index.html
```

Install supervisord

```bash
uv pip install supervisor
```

Source the environment variables and run the server

```bash
source .env && supervisord -c supervisord.conf
````
