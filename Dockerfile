FROM python:3.11.12-alpine3.21

RUN adduser -D -h /home/appuser appuser

WORKDIR /home/appuser

RUN apk add --no-cache curl build-base libffi-dev openssl-dev

ENV POETRY_HOME="/home/appuser/.poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false

COPY --chown=appuser:appuser . .

RUN python3 -m pip install --upgrade pip setuptools==70.0.0

RUN poetry install --no-root

USER appuser

ENV TERM=xterm

CMD ["python", "./main.py", "--config-dir", "config", "-e", "TERM=xterm"]
