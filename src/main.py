import subprocess
import sys
import pandas as pd

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO
class GitData:
  def __init__(self):
    self.__branches__ = self.__fetch_branches__()

  def __fetch_branches__(self):
    proc = subprocess.run(['git branch -a | cat'], shell=True, capture_output=True)
    rmv_chars = [' ', '*']
    branches_raw = proc.stdout.decode().split('\n')

    current_branch = ''
    all_branches = []
    left_branches = []

    for item in branches_raw:
      branch = item

      if('*' in item):
        current_branch=item.replace('*', '').replace(' ','')

      for char in rmv_chars:
        branch = branch.replace(char, '')

      if(item != ''):  
        all_branches.append(branch)
    
    all_branches = all_branches[0:-2]

    for branch in all_branches:
      if(branch != current_branch):
        left_branches.append(branch)

    return {
      'current_branch': current_branch,
      'all_branches': all_branches,
      'left_branches': left_branches
      }

  def get_branches(self):
    return self.__branches__
  
  def get_log(self, branch):
    """
      \"hash\",\"author_date\",\"author_name\",\"author_email\",\"committer_date\",\"committer_name\",\"committer_email\",\"subject\",\"body\"
      \\n
      \"%h\",\"%ai\",\"%an\",\"%ae\",\"%ci\",\"%cn\",\"%ce\",\"s\",\"b\"\n
    """
    options = '--pretty=format:\\\"hash\\\",\\\"author_date\\\",\\\"author_name\\\",\\\"author_email\\\",\\\"committer_date\\\",\\\"committer_name\\\",\\\"committer_email\\\",\\\"subject\\\",\\\"body\\\""%n"\\\""%h"\\\",\\\""%ai"\\\",\\\""%an"\\\",\\\""%ae"\\\",\\\""%ci"\\\",\\\""%cn"\\\",\\\""%ce"\\\",\\\""%s"\\\",\\\""%b"\\\"##end'
    rawstring = ''
    
    proc = subprocess.run(f'git log --no-merges {branch} {options} | cat', shell=True, capture_output=True)
    rawstring = proc.stdout.decode()
    
    array = rawstring.split('##end')

    data = []

    for x in array[0:-1]:
      file = StringIO(x)
      df = pd.read_csv(file, sep=',')
      data.append(df.iloc[0])

    df = pd.DataFrame(data,)
    df.reset_index(inplace=True)
    
    del df['index']
    return df

  def saveCsvFile(self, df, path):
    df.to_csv(path)

a = GitData()

print(a.get_branches())

for x in a.get_branches()['all_branches']:
  logDf = a.get_log(x)
  print(logDf)
  a.saveCsvFile(logDf, f'./{x}.csv')