# QuantumScape Genealogy API Demo - Meeting 1

This is a simple demo respository created for CSE120 - Team 420 meeting on 09/21/2026.

I created simple dummy data and API to get an idea of what type of functionality we can expect for this project. [See REFERENCES.md](REFERENCES.md)

## Getting started

### Create Virtual Env:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Start API

```bash
uvicorn app.main:app --reload --port 8420
```

Access at http://localhost:8420/docs
