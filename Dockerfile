FROM python:3.13.0b4-slim-bullseye



RUN echo ls
COPY dsa /backend/dsa
COPY scripts /backend/scripts
COPY tests /backend/tests

WORKDIR /backend

CMD ["python", "/backend/scripts/add.py"]





