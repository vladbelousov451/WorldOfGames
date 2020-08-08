FROM docker.io/library/python:3


COPY ./ /



RUN pip install -r ./requirements.txt
RUN chmod 777 /test/chromedriver

CMD [ "python", "MainGame.py" ]
