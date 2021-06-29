#!/bin/bash

# Default time zone in UTC
echo "0 18 * * * /daily_check_api.py >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f