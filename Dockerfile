FROM python:3.11.7-alpine3.19

WORKDIR /flask_app

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --no-cache-dir --upgrade -r requirements.txt

COPY /flask_app .

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "app:app"]
