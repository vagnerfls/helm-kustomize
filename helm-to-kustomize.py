import subprocess
import os
import shutil

environments = ['int', 'hom', 'prd', 'test', 'job', 'dev']

app_name = 'test'

for env in environments:
    release_name = f'{app_name}-{env}'

    if env == 'int':
        os.makedirs('./int/', exist_ok=True)
        subprocess.run(f'helm template {release_name} . > ./int/{release_name}.yaml', shell=True)
        shutil.move('./int', 'C:/Users/vagne/workspaces/gitops-template/overlays/')

    if env == 'hom':
        os.makedirs('./hom/', exist_ok=True)
        subprocess.run(f'helm template {app_name} . > ./hom/{release_name}.yaml', shell=True)
        shutil.move('./hom', 'C:/Users/vagne/workspaces/gitops-template/overlays/')

    if env == 'prd':
        os.makedirs('./prd/', exist_ok=True)
        subprocess.run(f'helm template {app_name} . > ./prd/{release_name}.yaml', shell=True)
        shutil.move('./prd', 'C:/Users/vagne/workspaces/gitops-template/overlays/')

    if env == 'test':
        os.makedirs('./test/', exist_ok=True)
        subprocess.run(f'helm template {app_name} . > ./test/{release_name}.yaml', shell=True)
        shutil.move('./test', 'C:/Users/vagne/workspaces/gitops-template/overlays/')

    if env == 'job':
        os.makedirs('./job/', exist_ok=True)
        subprocess.run(f'helm template {app_name} . > ./job/{release_name}.yaml', shell=True)
        shutil.move('./job', 'C:/Users/vagne/workspaces/gitops-template/overlays/')

    if env == 'dev':
        os.makedirs('./dev/', exist_ok=True)
        subprocess.run(f'helm template {app_name} . > ./dev/{release_name}.yaml', shell=True)
        shutil.move('./dev', 'C:/Users/vagne/workspaces/gitops-template/overlays/')        