import subprocess


class GitData:
  def __init__(self):
    self.__branches__ = self.__fetch_data__()

  def __fetch_data__(self):
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
    output = ''
    current_branch = self.__branches__['current_branch']
    subprocess.run(f'git checkout ${branch}', shell=True)
    
    a = subprocess.run(f'git log ${branch} | cat', shell=True, capture_output=True)
    output = a.stdout.decode()
    subprocess.run(f'git checkout ${current_branch}', shell=True)
    
    print(output)

a = GitData()

print('atual', a.get_branches())
a.get_log('main')

