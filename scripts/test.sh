#!/bin/env sh

DATE=`date +"%Y-%m-%d-%H-%M"`
echo "Date is $DATE"

USERS=`who | wc -l`
echo "Logged in user are $USERS"

UP=`date ; uptime`
echo "Uptime is $UP"
