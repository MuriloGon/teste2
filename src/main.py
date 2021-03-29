import subprocess

def get_branches():
  proc = subprocess.run(['git branch -a'], shell=True, capture_output=True)
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
      all_branches.append(branch.replace(char, ''))

    if(item != ''):  
      all_branches.append(branch)
  
  for branch in all_branches:
    if(branch != current_branch):
      left_branches.append(branch)

  return {'CurrentBranch': current_branch, 'AllBranches': all_branches, 'LeftBranches': left_branches}

a = get_branches()

print('atual', a['CurrentBranch'])
print('todos', a['CurrentBranch'])
print('restantes', a['CurrentBranch'])
