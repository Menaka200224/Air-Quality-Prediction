
```markdown
# Air Quality Prediction API

This project provides an **Air Quality Prediction API** using **FastAPI** and a pre-trained model with **Prophet**. The project is containerized with **Docker** for easy deployment.

---

## Features

- Predict air quality index (AQI) based on input features
- RESTful API endpoints using FastAPI
- Pre-trained model saved as `prophet_model.joblib`
- Dockerized for easy deployment

---

## Project Structure

```

Air-Quality-Prediction/
│
├─ app.py                  
├─ Dockerfile             
├─ requirements.txt        
├─ prophet_model.joblib     
└─ README.md               

````

---

## Setup and Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Air-Quality-Prediction.git
cd Air-Quality-Prediction
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run API Locally

```bash
uvicorn app:app --reload
```

Open browser: `http://127.0.0.1:8000/docs` to see **Swagger UI** and test endpoints.

---

## Docker Deployment

### 1. Build Docker Image

```bash
docker build -t air-quality-api .
```

### 2. Run Docker Container

```bash
docker run -d -p 8000:8000 air-quality-api
```

API will be available at `http://localhost:8000`.

---

## Git Synchronization Notes

If you encounter Git issues:

```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

Ensure your local repository is in sync with GitHub.

---

## Author

**Menaka Karunathilaka**

```
```

