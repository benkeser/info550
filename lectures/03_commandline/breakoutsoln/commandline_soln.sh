## Breakout 1
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

## list all files with sizes displayed in bytes/kilobyes/megabytes
ls -lh
## remove tmp_file
rm tmp_file
## rename another_tmp_file to such_a_cool_file
mv another_tmp/another_tmp_file another_tmp/such_a_cool_file
## remove tmp directory and all its contents
# move up a directory
cd ..
# remove tmp directory
rm -rf tmp

## Breakout 2
curl -L http://bit.ly/hamlet_txt > hamlet.txt

## find "To be, or not to be" and write the contents of this monologue 
## to a file speech.txt (hint: the speech is 35 lines)
grep -A 34 'To be, or not to be' hamlet.txt  

## make a file called greatest_hits.txt that includes:
## - the "To be, or not to be" speech
## - the line that includes "know not what we may be"
## - all lines that include the word "doubts" or "Doubts"
grep -A 34 'To be, or not to be' hamlet.txt > greatest_hits.txt
# add a blank line
echo "" >> greatest_hits.txt
grep "know not what may be" hamlet.txt >> greatest_hits.txt
echo "" >> greatest_hits.txt
grep -i "doubts" hamlet.txt >> greatest_hits.txt

## replaces all instances of the string "doubts" with "uncertainties" in your 
## greatest_hits.txt file (hint: sed or awk)
# look at last 5 lines of files
cat greatest_hits | tail - 5
# modify file in place
sed -i "" "s/doubts/uncertainties/g" greatest_hits.txt
# look again at last 5 files of files
cat greatest_hits | tail - 5


## Breakout 3

## Write a script that
## 
## - uses curl to download the text of Romeo and Juliet from Project Gutenberg
##   http://www.gutenberg.org/files/1112/1112.txt ;
## - counts the number of lines for characters Romeo ("Rom."), Juliet ("Jul."), and 
##   the Apothecary ("Apoth.");
## - saves a plain text file that for each of these characters says:
##   "[character] has [num] lines".

# Put the contents between #---# and #---# below in a file called script.sh
#--- script.sh ---#
#! /bin/bash

# download
curl -L http://www.gutenberg.org/files/1112/1112.txt > rj.txt
# create empty file 
touch num_lines.txt
for name in "Rom" "Jul" "Apoth"
do
	lines=$(grep "$name\." rj.txt | wc -l)
	echo "$name has $lines lines" >> num_lines.txt
done
#--- end script.sh ---#

# cd to folder containing script.sh
chmod +x script.sh 
./script.sh
cat num_lines.txt


