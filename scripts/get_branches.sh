DATA_DIR=data
DATA_LOGS=$DATA_DIR/logs
DATA_BRANCHES=$DATA_DIR/branches

rm -r $DATA_DIR

mkdir $DATA_DIR
mkdir $DATA_LOGS
mkdir $DATA_BRANCHES

git branch -a | grep remotes | tr -d '[:blank:]' | cat > $DATA_BRANCHES/branches.txt

# get branches
IFS=$'\n' read -d '' -ra branches < $DATA_BRANCHES/branches.txt
for branch_raw in "${branches[@]}"
do
  IFS='/' read -ra branch <<< "$branch_raw"
  git log -a $branch_raw | cat > $DATA_LOGS/${branch[2]}.txt 
done

