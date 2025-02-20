FROM ghcr.io/astral-sh/uv:python3.13-alpine
WORKDIR /main
RUN apk add --no-cache tzdata
ENV TZ=Europe/London

COPY .env .env
COPY app app
COPY configs/gunicorn.conf.py gunicorn.conf.py
COPY .python-version .python-version
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "gunicorn"]
