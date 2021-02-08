FROM python:3.6

WORKDIR /app
COPY . /app

RUN apt update -y && apt upgrade -y
RUN apt install cron -y 
RUN (crontab -l ; echo "* * * * * echo "hello world" >> /var/log/cron.log ") | crontab
RUN pip install discord.py requests pandas html5lib bs4 lxml  

CMD python bot.py 