FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app/


RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


COPY ./pyproject.toml ./poetry.lock* /app/


ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"


ARG INSTALL_JUPITER=false
RUN bash -c "if [ $INSTALL_JUPITER == 'true' ] ; then pip install jupyterlab ; fi"

COPY . /app
ENV PYTHONPATH=/app
