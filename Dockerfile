FROM python:3.7-alpine3.9

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev tzdata
RUN cp /usr/share/zoneinfo/Europe/Kiev /etc/localtime && echo "Europe/Kiev" >  /etc/timezone
ADD . /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt
CMD ["python", "main.py"]