#!/bin/bash

# Aktifkan virtual environment
source venv/bin/activate

# Jalankan FastAPI dengan jalur modul modular
PYTHONPATH=. uvicorn app.main:app --reload
