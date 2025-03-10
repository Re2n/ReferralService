FROM python:3.12

WORKDIR /aipresentationbackend

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

EXPOSE 5466

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5466"]