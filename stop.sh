#!/bin/bash
echo "Stopping uvicorn..."
pkill -f "uvicorn app.main:app"
