

# Air Quality Prediction API

**FastAPI · Docker · Prophet**

Predict air quality index (AQI) using a pre-trained Prophet model. This REST API is containerized with Docker and ready for deployment on Railway or any cloud platform.

---

## Features

- Predict AQI based on historical data  
- REST API built with **FastAPI**  
- Pre-trained **Prophet** model  
- Dockerized for reproducible deployment  

---

## Quick Start

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AirQuality.git
cd AirQuality
````

### Install dependencies

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the API

```bash
python app.py
```

### Open documentation in your browser

```
http://127.0.0.1:8000/docs
```

> Ensure `app.py` reads the port from the environment:

```python
import os
port = int(os.environ.get("PORT", 8000))
app.run(host="0.0.0.0", port=port)
```

---

## Test Endpoints

### Home

```
GET https://YOUR_DOMAIN/
```

### Predict

```
POST https://YOUR_DOMAIN/predict
```

Example JSON:

```json
[
  {"ds": "2025-01-01"},
  {"ds": "2025-01-02"}
]
```

---

## Tech Stack

* Python 3.10+
* FastAPI
* Prophet
* Docker



