FROM python:3.12.3-slim

WORKDIR /app
COPY . .

# Optional: install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Your script with the while True loop
CMD ["python", "loop.py"]
