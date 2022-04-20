FROM python:latest
RUN python --version
RUN python -m pip install --upgrade pip
RUN python -m pip install flask
COPY ./source /app
WORKDIR /app
ENTRYPOINT python main.py
