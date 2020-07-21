FROM python:3


COPY ./* /


RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install  google-chrome-stable  -y
RUN pip install -r ./requirements.txt

CMD [ "python", "MainGame.py" ]
