FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pandas numpy matplotlib seaborn

CMD ["python", "data_analysis.py"]