FROM python:3.9.13
COPY requirements.txt /
COPY snow-wake.py /app/snow-wake.py
RUN chmod +x /app/snow-wake.py
RUN pip install -r /requirements.txt