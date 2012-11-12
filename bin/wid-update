#!/bin/bash

week=$(date +%V)
year=$(date +%Y)
updates=/Users/$(whoami)/Dropbox/.whatidid/updates/$year
file=$updates/$week.md

if [ -z "$1" ];
then
  echo 'usage: weekly_update.sh "This is something I did today"'
  exit 1
fi

if [ ! -d $updates ];
then
  mkdir -p $updates
fi

if [ ! -f $file ];
then
  touch $file
fi

echo "$(date +%A) $(date +%m) $(date +%d) $(date +%Y) $(date +%s): $1" >> $file

