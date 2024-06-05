FROM python:3.11
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app.py ./
COPY mymodel.keras ./
COPY readme.md ./


EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]