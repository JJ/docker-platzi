FROM python:3

WORKDIR /src

ADD main.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /src/Hitos
ADD Hitos/Hitos.py Hitos
RUN rm requirements.txt
EXPOSE 80

CMD ['hug', '-p', '80', '-f', 'main.py'] 


