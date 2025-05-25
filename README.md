# 📊 Pattern Learner API

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-brightgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

🚀 **Pattern Learner API** is the most complete deterministic pattern detection API built with FastAPI.  
Predict, analyze, validate, and learn all kinds of number patterns—no machine learning involved.

---

## ✨ Features

- ✅ Learn number sequences (`/learn`)
- ✅ Predict next number(s) from learned pattern (`/predict`)
- ✅ Analyze any sequence without learning (`/analyze`)
- ✅ Validate predictions (`/validate`)
- ✅ Get current pattern state (`/state`)
- ✅ Reset learning state (`/reset`)
- 🧩 Modular, testable, and blazing-fast

---

## 🧠 Supported Patterns

- Arithmetic ➕  
- Second-order difference 🔁  
- Prime numbers 🔢  
- Geometric sequences 📈  
- Fibonacci numbers 🌀  
- Even numbers 🔵  
- Odd numbers 🔺  
- Factorials (!)  
- Triangular numbers 🔺🔺  
- Cubic numbers 🧊  
- Polynomial patterns (deg ≥2) 🧮  
- Pascal triangle 📐  
- Flattened Pascal grid 📊  
- Power series (baseⁿ) ⚡  
- Bit-pattern (2ⁿ−1) 💡  
- Interleaved multi-way 🔀  
- Repeating/cyclic ⏸️  
- Palindromes 🔁  
- Digit-sequence growth 🔼  
- Digit-compression sum ♻️  
- Noise-tolerant arithmetic 🌫️  
- Mirror/mountain digits ⛰️  
- Digit logic 🧠  
- Digit multiplication & odd count 🧩

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/pattern-ai-fastapi.git
cd pattern-ai-fastapi
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://localhost:8000/docs

---

## 📮 Example Requests

### /learn

```json
POST /learn
{
  "numbers": [2, 4, 6, 8]
}
```

### /predict

```http
GET /predict
```

### /analyze

```json
POST /analyze
{
  "numbers": [3, 6, 9],
  "count": 3
}
```

### /validate

```json
POST /validate
{
  "numbers": [2, 3, 4, 5, 6, 8, 8, 11, 16, 11, 18, 32],
  "prediction": [14, 27, 64]
}
```

---

## 🏗️ Project Structure

```
app/
├── core/               # All analyzers and logic
│   ├── patterns/
│   └── pattern_learner.py
├── models/             # Request/response schemas
├── services/           # Core service layer
├── api.py              # Route handler
├── main.py             # FastAPI entrypoint
tests/
└── test_patterns.py    # Pytest suite
```

---

## 🧪 Testing

```bash
pytest
```

All patterns are tested including arithmetic, interleaved, factorials, and edge cases.

---

## 🤝 Contributing

Pull requests are welcome. Add new analyzers inside `app/core/patterns/` and register in `ALL_ANALYZERS`.

---

## 📄 License

MIT License © 2024

---

**Pattern Learner API** — Built with ❤️ using FastAPI.
