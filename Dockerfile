FROM python:3.11.7-alpine3.19

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --no-cache-dir --upgrade -r requirements.txt

VOLUME /flask_app

WORKDIR /flask_app

EXPOSE 8000

CMD ["gunicorn", "-b", ":8000", "-w", "2", "app:app"]
