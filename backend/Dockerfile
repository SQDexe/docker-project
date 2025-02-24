FROM python:3.13.2-alpine3.21

WORKDIR /code

COPY . ./
RUN apk add --no-cache mariadb-dev gcc musl-dev python3-dev && \
    pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["fastapi", "run", "app.py"]