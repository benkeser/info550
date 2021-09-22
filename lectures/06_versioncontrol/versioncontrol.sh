
### git-config ###
# set user name
git config --global user.name "Jane Doe"
# set email
git config --global user.email "janedoe@emory.edu"

### git-init } ###
# make a directory (tmp_gitdir is "git repository")
mkdir ~/tmp_gitdir
# move into directory
cd ~/tmp_gitdir
# initialize repository
git init

### show-gitfile ###
# see what it did
ls -lha ~/tmp_gitdir

### git-status ###
# make a README.md file from the command line
echo "## My first repository" >> README.md
echo "This is just a toy repository for demonstration." >> README.md

# make a silly bash script
echo "#! /bin/bash" >> silly_shell.sh
echo "echo 'Hello world'" >> silly_shell.sh

# check what has changed
git status

### git-add1 ###
# add the README to the commit
git add README.md
git status

### git-commit1 } ###
# make a commit
git commit -m "added README to repo"

### git-log } ###
# view history of commits
git log

### make-gitignore } ###
# make a sandbox folder
mkdir sandbox
# add a (blank) file to it
touch sandbox/a_test_file.sh
# make a .gitignore file that ignores a sandbox folder
echo "sandbox/*" >> .gitignore
# check status of repo 
git status

### branching } ###
# make a branch called devel
git branch devel
# checkout that branch
git checkout devel
# see all branches
git branch

### modify-files } ###
# add a line to README and commit
echo "Some cool new info for the README!" >> README.md
git add README.md 
git commit -m "update the README"

### cat-readme ###
# look at contents of README
cat README.md

### look-master } ###
# switch back to master
git checkout master

### look-readme } ###
# look at contents of README
cat README.md

### merge-devel } ###
# **!! on the master branch !!**
git merge devel

### check-merge ###
cat README.md

### check-merge1 ###
git checkout master
git merge new-idea

### create-conflict ###
git checkout devel
# replace a word in README
# if on mac use this version of sed
sed -i "" 's/cool/great/g' README.md
# if on linux use this version
sed -i 's/cool/great/g' README.md
git add README.md
git commit -m "great info, not cool info."

### cat-it-devel } ###
cat README.md

### create-conflict-again ###
git checkout master
# if on mac use this version of sed
sed -i "" 's/cool/excellent/g' README.md
# if on linux use this version
sed -i 's/cool/excellent/g' README.md
git add README.md
git commit -m "excellent info, not cool info."

### cat-it-master } ###
cat README.md

### create-conflict3 ###
git merge devel

### cat-it-conflict } ###
cat README.md

### fix-conflict ###
# remove lines 3-5 and 7
# if on mac use this version of sed
sed -i "" '3,5d;7d' README.md
# if on linux use this version of sed
sed -i '3,5d;7d' README.md
cat README.md

### merge-fixed-conflicts } ###
git add README.md
git commit -m "fixed merge conflicts"

### add-origin ###
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

### git-amend ###
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

### git-reset ###
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

### pull-error ###
## To https://github.com/username/repo.git
##  ! [rejected]        master -> master (fetch first)
## error: failed to push some refs to 'https://github.com/YOU/REPO.git'
## hint: Updates were rejected because the remote contains work that you do
## hint: not have locally. This is usually caused by another repository pushing
## hint: to the same ref. You may want to first integrate the remote changes
## hint: (e.g., 'git pull ...') before pushing again.
## hint: See the 'Note about fast-forwards' in 'git push --help' for details.
