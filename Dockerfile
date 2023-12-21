FROM python:3.11.7-alpine3.19

RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

COPY /flask_app .

EXPOSE 5000

CMD ["flask", "run"]
