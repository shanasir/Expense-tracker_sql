# 1. Use official Python image as base
FROM python:3.11

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy all files into the container
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#5. Port binding
EXPOSE 8080

# 6. Run the app when container starts
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]
