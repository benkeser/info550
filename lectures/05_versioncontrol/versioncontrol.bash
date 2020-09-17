
### eval = FALSE} ###
# set user name
git config --global user.name "Jane Doe"
# set email
git config --global user.email "janedoe@emory.edu"

###  ###
# make a directory (tmp_gitdir is "git repository")
mkdir ~/tmp_gitdir
# move into directory
cd ~/tmp_gitdir
# initialize repository
git init

### highlight.output=4} ###
# see what it did
ls -lha ~/tmp_gitdir

### tidy=TRUE ###
# make a README.md file from the command line
echo "## My first repository" >> README.md
echo "This is just a toy repository for demonstration." >> README.md

# make a silly bash script
echo "#! /bin/bash" >> silly_shell.sh
echo "echo 'Hello world'" >> silly_shell.sh

# check what has changed
git status

### highlight.output=5} ###
# add the README to the commit
git add README.md
git status

###  ###
# make a commit
git commit -m "added README to repo"

###  ###
# view history of commits
git log

###  ###
# make a sandbox folder
mkdir sandbox
# add a (blank) file to it
touch sandbox/a_test_file.sh
# make a .gitignore file that ignores a sandbox folder
echo "sandbox/*" >> .gitignore
# check status of repo 
git status

###  ###
# make a branch called devel
git branch devel
# checkout that branch
git checkout devel
# see all branches
git branch

###  ###
# add a line to README and commit
echo "Some cool new info for the README!" >> README.md
git add README.md 
git commit -m "update the README"

### highlight.output=3} ###
# look at contents of README
cat README.md

###  ###
# switch back to master
git checkout master

###  ###
# look at contents of README
cat README.md

###  ###
# **!! on the master branch !!**
git merge devel

### highlight.output=3} ###
cat README.md

### eval = FALSE} ###
git checkout master
git merge new-idea

### create-conflict1-mac ###
git checkout devel
# replace a word in README
sed -i "" 's/cool/great/g' README.md
git add README.md
git commit -m "great info, not cool info."

### create-conflict1-notmac ###
git checkout devel
# replace a word in README
sed -i 's/cool/great/g' README.md
git add README.md
git commit -m "great info, not cool info."

### cat-it-devel} ###
cat README.md

### create-conflict2-mac ###
git checkout master
sed -i "" 's/cool/excellent/g' README.md
git add README.md
git commit -m "excellent info, not cool info."

### create-conflict2-notmac ###
git checkout master
sed -i 's/cool/excellent/g' README.md
git add README.md
git commit -m "excellent info, not cool info."

### cat-it-master} ###
cat README.md

### create-conflict3 ###
git merge devel

### cat-it-conflict} ###
cat README.md

### fix-conflict-mac ###
# remove lines 3-5 and 7
sed -i "" '3,5d;7d' README.md
cat README.md

### fix-conflict-notmac ###
# remove lines 3-5 and 7
sed -i '3,5d;7d' README.md
cat README.md

### merge-fixed-conflicts} ###
git add README.md
git commit -m "fixed merge conflicts"

### eval = FALSE} ###
# replace username with your user name and repo with 
# your repository name
git remote add origin https://github.com/username/repo
# push the repository
git push -u origin master

### git-fetch-demo ###
# add friend's repo as a remote branch
git remote add friend https://github.com/friend/repo
# downloads friend's branch, but do not merge it yet
git fetch friend master
# view all local and remote branches
git branch -a
# checkout friends remote branch
git checkout remotes/friend/master
# make a local branch based on friend's repo
git checkout -b friend
# test out the branch; make sure it works as expected
[...]
# checkout local master, merge, push
git checkout master
git merge friend
git push origin master

### eval = FALSE} ###
# assume project starts in functional state
# make a small change to project
[...]
# commit current changes under WIP heading BUT DON'T PUSH!
git add * && git commit -m "WIP"
# make more changes
[...]
# amend past commit
git commit --amend --no-edit
# make more changes
[...]
# amend past commit
git commit --amend --no-edit
...
# push only after confirming everything works
git commit --amend -m "awesome new feature that fixes everything"
git push origin master

### eval = FALSE} ###
# assume project starts in functional state
# make a small change to project
[...]
# commit current changes under WIP heading BUT DON'T PUSH!
git add * && git commit -m "WIP"
# make more changes
[...]
# amend past commit
git commit --amend --no-edit
# make more changes
[...]
# !!! UH OH EVERYTHING BROKE !!! #
git reset --hard

### eval = FALSE} ###
## To https://github.com/username/repo.git
##  ! [rejected]        master -> master (fetch first)
## error: failed to push some refs to 'https://github.com/YOU/REPO.git'
## hint: Updates were rejected because the remote contains work that you do
## hint: not have locally. This is usually caused by another repository pushing
## hint: to the same ref. You may want to first integrate the remote changes
## hint: (e.g., 'git pull ...') before pushing again.
## hint: See the 'Note about fast-forwards' in 'git push --help' for details.
