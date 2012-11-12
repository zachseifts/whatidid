#!/bin/bash

if [ $# -ne 1 ];
then
  echo "usage: mail.sh user@example.com"
fi

week=$(date +%V)
year=$(date +%Y)
updates=/Users/$(whoami)/Dropbox/.whatidid/updates/$year
file=$updates/$week.md
subject="Weekly Update: $(date +"%A %B %d, %Y")"

/usr/bin/mail -s "$subject" $1 < $file

