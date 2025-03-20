FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for Streamlit (default 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app/app.py"]
