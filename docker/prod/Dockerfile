FROM python:3.11.4-slim-buster
LABEL mantainer="contato@jonathacarlos.dev.br"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./djangoapp /djangoapp
COPY ./docker/prod/scripts /scripts

WORKDIR /djangoapp

EXPOSE 8000
EXPOSE 8001

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y libmagic1 \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install python dependencies
RUN python -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install setuptools wheel --upgrade \
    && /venv/bin/pip install --no-cache-dir -r /djangoapp/requirements.txt \
    && adduser --disabled-password --no-create-home duser \
    && mkdir -p /data/web/static \
    && mkdir -p /data/web/media \
    && chown -R duser:duser /venv \
    && chown -R duser:duser /data/web/static \
    && chown -R duser:duser /data/web/media \
    && chmod -R 755 /data/web/static \
    && chmod -R 755 /data/web/media \
    && chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["start.sh"]
