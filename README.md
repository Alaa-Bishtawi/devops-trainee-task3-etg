## Exalt Devops Trainee Final Task

###### Introduction
Flask files
There is two files where the first file that is called main.py contains the routes and the flask server initalization, while the second file metricsRetrive.py contains the the database connection , the queries , the string processing and the final functions that are going to be called from the main.py by the routes for the corresponding command wheither it being about cpu or ram or disk(hdd) or day which returns a 24 values (as a the hourly usage for the day) or the current usage , while each value will be pared with the time and followed by the usage .
###### PreRequirment

- This task has been created for Centos or Redhat distibuation

- Ansible
###### Setup The Enviroment
- Install Ansible From official website https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

- if you are using centos 7
```
sudo yum -y update
sudo yum -y install epel-repo
sudo yum -y update
sudo yum -y install ansible
```
You can check if Ansible is installed successfully by finding its version.
```
ansible --version    
```

- Clone The Repo
- run the code
```ansible
ansible-playbook playbook.yml -i inventory.txt
```
