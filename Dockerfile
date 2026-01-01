ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required by Prophet
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY prophet_model.joblib .

EXPOSE 8000

CMD ["python", "app.py"]
