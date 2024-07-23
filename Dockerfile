FROM python:3.12.3-slim-bullseye



RUN echo ls
#COPY dsa /product/dsa
#COPY scripts /product/scripts
#COPY tests /product/tests
#COPY backend /product/backend

COPY . /product/



WORKDIR /product
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN chmod +x /product/start.sh

CMD ["/product/start.sh"]





