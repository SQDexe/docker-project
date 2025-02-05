FROM python:3.13.1

COPY . /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["fastapi", "run", "/code/app.py"]