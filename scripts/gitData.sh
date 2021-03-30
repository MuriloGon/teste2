#!/bin/bash

DATA_DIR=data
DATA_LOGS=$DATA_DIR/logs
DATA_BRANCHES=$DATA_DIR/branches

rm -r $DATA_DIR

mkdir $DATA_DIR
mkdir $DATA_LOGS
mkdir $DATA_BRANCHES

# check out to main branch
git checkout main 

# get all branches
git branch -a | grep remotes | tr -d '[:blank:]' | cat > $DATA_BRANCHES/branches.txt

# write git logs
OPTIONS='--pretty=format:"%h","%ai","%an","%ae","%ci","%cn","%ce","%s","%b"'
HEADER='"hash","author_date","author_name","author_email","committer_date","committer_name","committer_email","subject","body"'
IFS=$'\n' read -d '' -ra branches < $DATA_BRANCHES/branches.txt
for i in "${!branches[@]}"
do
  IFS='/' read -ra branch <<< "${branches[$i]}"
  
  echo $HEADER | cat >> $DATA_LOGS/${branch[2]}.txt 

  git log -a "${branches[$i]}" $OPTIONS | cat >> $DATA_LOGS/${branch[2]}.txt 
done

