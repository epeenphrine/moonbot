# Custom Bot for a different server 

## quick description

* bot.py takes user inputs and returns market data based on user input
* botscript.py designed to run on cronjob. Basically turns on sends message to channel and turns off.

## things to do before running

* change main_chat_id variable in bot.py to your channel
* you need to give your token. In my case I am importing the token key from config.py which is in .gitignore 

## bot.py

main bot that takes commands from users 

## botscript.py

runs a script posts a message and then turns off. (Not continuous like bot.py)

## run in docker 

`
docker-compose up -d
`

## set cronjob for botscript.py

Example: \
“At 09:25 on every day-of-week from Monday through Friday.” \
`
25 9 * * 1-5 docker start myfxbook_script
`
