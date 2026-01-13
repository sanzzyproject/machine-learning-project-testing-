# Base Image
FROM python:3.9-slim

# Set Working Directory
WORKDIR /app

# Copy Dependencies
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Expose Port
EXPOSE 8000

# Run Command
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
