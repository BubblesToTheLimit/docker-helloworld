FROM python:latest
COPY main.py /main.py
RUN pip install flask
RUN pip show flask
CMD python /main.py
