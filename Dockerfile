FROM python:3

COPY ./* /
RUN pip install -r ./requirements.txt

CMD [ "python", "Live.py" ]