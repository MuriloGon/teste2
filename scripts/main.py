BRANCHES_PATH = './data/branches/branches.txt'
BRANCHES = open(BRANCHES_PATH, "r").read().split('\n')[0:-1]
GIT_REPO = 'https://github.com/MuriloGon/teste2/'

def get_branches():
    output = []
    for branch in BRANCHES:
        output.append(branch.split('/')[-1])
    return output
    
def branch_url(branch):
    return GIT_REPO + 'tree/' + branch

def write_readme(arrays):
    try:
        file = open("README.asc", "x")
    except:
        file = open("README.asc", 'w')

    for x in arrays:
        for y in x:
            file.write(y+'\n')
            
    file.close()

def header():
    output = []
    branches = get_branches()

    output.append(f'=== Trybe Projects')
    output.append(f'== Summary')
    
    for branch in branches:
        output.append(f'. {branch_url(branch)}[{branch}]')
    return output

print(header())

write_readme([header()])