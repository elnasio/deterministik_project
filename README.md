![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)

# 📊 Pattern Learner API

🚀 A simple and powerful API built with FastAPI to detect, learn, and predict mathematical number patterns.

---

## 📦 Features

✅ Learn number sequences (`/learn`)  
✅ Predict next number based on last learned pattern (`/predict`)  
✅ Analyze any number sequence without learning it (`/analyze`)  
✅ Support for rich pattern detection:
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
- Polynomial patterns (deg 2+) 🧮  
- Pascal triangle row 📐  
- Flattened Pascal grid 📊  
- Power series (baseⁿ) ⚡  
- Bit-pattern (2ⁿ−1) 💡  
- Interleaved patterns 🔀  
- Interleaved multi-way patterns 🔀🔀  
- Digit repetition ⏸️  
- Palindromes 🔁  
- Digit-sequence growth (e.g. 123, 1234) 🔼  
- Digit-compression sum (e.g. 10 → 1) ♻️  
- Noise-tolerant arithmetic 🌫️  
- Mirror/mountain digits ⛰️  
- Digit-sequential logic (first+last=middle) 🧠  
- Edge digit multiplication & odd digit count 🧩  
- Debug/fallback analysis 🐞  

---

## 🧠 How It Works

- **/learn**: Teaches the system a sequence.
- **/predict**: Predicts the next number from the last learned pattern.
- **/analyze**: Tests any sequence (even without learning it) and returns its pattern type and prediction.
- **/state**: Returns the current learned state.
- **/reset**: Clears the learned sequence.

---

## 🚀 Getting Started

### 1. Clone & Install
```bash
git clone https://github.com/your-username/pattern-ai-fastapi.git
cd pattern-ai-fastapi
pip install -r requirements.txt
```

### 2. Run Locally
```bash
uvicorn app.main:app --reload
```

### 3. Open in Browser
```
http://localhost:8000/docs
```
Use Swagger UI to interact with all endpoints 🎯

---

## 📮 Example Requests

### 🔹 Learn
```json
POST /learn
{
  "numbers": [2, 4, 6, 8]
}
```

### 🔹 Predict
```http
GET /predict
```

### 🔹 Analyze
```json
POST /analyze
{
  "numbers": [3, 6, 9],
  "count": 3
}
```

Response:
```json
{
  "pattern": "arithmetic",
  "next_number": [12, 15, 18]
}
```

---

## 🏗️ Project Structure
```
app/
├── core/               # Core pattern logic
├── models/             # Request/response models
├── services/           # Learner service layer
├── api.py              # FastAPI router
├── main.py             # App entry point
```

---

## 🤝 Contributing
Pull requests are welcome! Open an issue first to discuss your idea.

---

## 📄 License
MIT License

---

Made with ❤️ using FastAPI
