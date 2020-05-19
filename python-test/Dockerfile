FROM glagnar/opencv:amd64-3.8-4.2.0

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ADD . .

CMD ["python", "main.py"]
