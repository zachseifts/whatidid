#!/bin/bash

week=$(date +%V)
year=$(date +%Y)
updates=/Users/$(whoami)/Dropbox/whatidid/updates/$year
file=$updates/$week.md

if [ ! -d $updates ];
then
  mkdir -p $updates
fi

if [ ! -f $file ];
then
  echo "# Week of $(date +%B) $(date +%d), $(date +%Y)" > $file
fi

if [ -z "$1" ];
then
  echo 'usage: weekly_update.sh "This is something I did today"'
  exit 1
fi

echo "$(date +%A), $(date +%m/%d/%Y): $1" >> $file

