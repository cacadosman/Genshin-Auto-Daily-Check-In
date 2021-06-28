#!/bin/bash

echo "* * * * * /daily_check.py >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f