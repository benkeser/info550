
### exercise1 ###
# make a directory named tmp
mkdir tmp
# move into tmp 
cd tmp
# add an empty file named tmp_file
touch tmp_file
# add an empty directory named another_tmp
mkdir another_tmp
# add an empty file to another_tmp directory
touch another_tmp/another_tmp_file

### bash-profile ###
# modify PATH
export PATH=.:/usr/local/bin:$PATH
# shortcut for listing
alias ll='ls -lh'
# shortcut for opening chrome from browser
alias chrome="open -a 'Google Chrome'"

### hamlet ###
# download hamlet text from web and save 
# in file called hamlet.txt
curl -L http://bit.ly/hamlet_txt > hamlet.txt

# lines the string "Ham" mentioned
grep "Ham" hamlet.txt

# lines with "Oph" and "Ham"
grep "Ham" hamlet.txt | grep "Oph"

# count Hamlet's lines
grep "Ham\." hamlet.txt | wc -l

# see the start of Hamlet's first 5 lines
grep "Ham\." hamlet.txt | head -5

# see the start of Hamlet's last line
grep "Ham\." hamlet.txt | tail -1 

### wildcards ###
# files in cwd with .txt extension
ls -l *.txt
# all files in cwd named a_file with three character extension
ls a_file.???
# .txt files in cwd name a_file, b_file, ..., e_file
ls [a-e]_file.txt

### variables ###
# bad -- no spaces!
a = "some"
# good
a="some"

# references a
echo a
echo $a
echo "The value of a is $a"

# curly braces are for avoiding ambiguity
echo "I am printing $athing"
echo "I am printing ${a}thing"

### command-subst ###
# a sequence
seq 1 10
# save the sequence as a variable
my_sequence=$(seq 1 10)
echo $my_sequence

### command-subst2 ###
b=$((12 + 2))
((b + 2))
((b++))

### for-loops ###
for name in Ronald Ozzie Freddie
do
  echo "My name is $name."
done

### if-statements ###
for i in {1..5}
do
  if [ "$i" == "3" ]
  then 
    echo "This is a special iteration"
  else
    echo "This is iteration $i"
  fi
done

### where-bash ###
which bash

### my-shebang ###
#! /bin/bash

### bash-script ###
#! /bin/bash
# comments use # symbol
# you may need to replace shebang!

# define a variable
a="bash"

for i in "very" "so much" "incredibly"
do
  echo "$a is $i fun"'!'
done

### chmod ###
chmod +x first_script.sh

### run-script ###
first_script.sh
