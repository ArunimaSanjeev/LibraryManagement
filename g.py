print("git init")
print("git add .")
print('git commit -m "initial commit"')

print('git remote add origin https://github.com/ArunimaSanjeev/LibraryManagement.git')
print("git branch -M main")
print("git push -u origin main")

print("git diff  - check differences")
print("git log  - check history")

print("git branch login-feature  - create new branch")
print("git checkout login-feature  - switch to branch")
print("Add login code to the file")

print("git add .  - stage changes")

print("git checkout main")
print("git merge login-feature  - merge branch")

print("git restore library.py  - restore previous version")
print("git diff  - check changes")

print("Handling merge conflict:")
print("git checkout main")
print("git merge login-feature")
print("git add <file>")
print('git commit -m "Resolved merge conflict"')
print("git log")

print("git fetch origin  - get changes from remote")
print("git pull origin main")

print("git tag v1.0  - mark final version")
print("git push origin v1.0")

print("git clone https://github.com/username/repo.git")

print("git checkout -b feature  - create and switch branch")

'''Pipeline Task 1:
pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Show Files') {
 steps {
 bat 'dir'
 }
 }
 }
}
Pipeline Task 2:
pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Print Directory') {
 steps {
 bat 'cd'
 }
 }
 }
}
Pipeline task 3:
pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Print Message') {
 steps {
 echo 'Hello! Jenkins Pipeline executed successfully'
 }
 }
 }
}
Pipeline task 4:
pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Create File') {
 steps {
 bat 'echo This file is created by Jenkins > demo.txt'
 }
 }
 }
}
Pipeline task 5:
pipeline {
 agent any
 stages {
 stage('Checkout Code') {
 steps {
 git 'https://github.com/your-username/your-repo.git'
 }
 }
 stage('Read File') {
 steps {
 bat 'type README.md'
 }
 }
 }
}'''