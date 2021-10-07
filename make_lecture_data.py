#! /usr/bin/env python3

# this script builds yaml data files for the lectures and homework
# subdirectories. 
#
# a single input is expected, which is the path of the build directory 
import yaml
import os
import sys

# function to get yaml front-matter from an open file
# f is an open file
# returns a dictionary containing the yaml front matter 
def get_yaml(f):
  pointer = f.tell()
  if f.readline() != '---\n':
    f.seek(pointer)
    return ''
  readline = iter(f.readline, '')
  readline = iter(readline.__next__, '---\n')
  return ''.join(readline)

# function to convert time_str to seconds
def get_sec(time_str):
  h, m, s = time_str.split(':')
  return int(h) * 3600 + int(m) * 60 + int(s)

# saves a file in the _data folder of the site that contains
# appropriately formatted yaml data for the lecture or homework
# page. 
#
# for this function to work as expected, certain yaml contents are
# expected in the lecture and homework Rmd files. 
# for lectures: 
# - title = title of lecture
# - tldr = tl;dr printed below lecture
# - recording = link to recording; can be ""
# - start = time that lecture starts in video recording
# - reading = hyphen-separated header from the readings page (see readings.md for 
#     these headings)
# - breakoutsoln = file name that contains breakout solutions in the breakoutsoln 
#     sub-directory of lecture directory
# for homeworks:
# - title = title of homework assignment
# - due = due date of homework assignment
# 
# it is also expected that there is only one Rmd or rmd file in each homework
# or lecture directory
#
# site_dir is the top level directory
# which_data should be either 'lecture' or 'homework'
def make_data(site_dir, which_data):
  # get directory from input
  top_dir=site_dir
  # find folders with lecture in title
  if which_data == "lecture":
    which_data_dir=os.path.join(top_dir, "lectures")
  else: 
    which_data_dir=os.path.join(top_dir, "homework")
  os.chdir(which_data_dir)
  all_files=sorted(os.listdir(which_data_dir))
  content_dirs = [f for f in all_files if os.path.isdir(f)]
  # declare empty dictionary
  content_dict_list=[]
  # loop over content directories to build dictionary that contains
  # proper yaml information
  for dir in content_dirs:
    os.chdir(dir)
    all_files_in_dir=os.listdir(".")
    # get rmd file name
    rmd_file = [f for f in all_files_in_dir if ('.Rmd' in f or '.rmd' in f)]
    # if more than one Rmd file, break 
    if len(rmd_file) > 1:
      sys.exit('More than one .Rmd file in ' + dir)
    # get yaml from rmd file
    with open(rmd_file[0]) as f:
      config = yaml.load(get_yaml(f), Loader=yaml.FullLoader)
    if which_data == "lecture":
      this_dict = { 
         "filename" : os.path.splitext(rmd_file[0])[0], 
         "dirname" : dir, 
         "title" : config['title'],
         "tldr" : config['tldr'],
         "recording" : config['recording'],
         "start" : config['start'],
         "reading" : config['reading'],
         "breakoutsoln" : config['breakoutsoln'],
         "recording_url" : ''.join(x if x.isalnum() else '-' for x in config['title']).lower()
      }
      # writing _recordings file
      text_list = ["---", "layout: default", "---", 
      '<div class="container">'
      '<iframe class="responsive-iframe" src="https://rsph.hosted.panopto.com/Panopto/Pages/Embed.aspx?id='+
      config['recording']+
      '&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start='+
      str(get_sec(config['start']))+
      '&interactivity=all" style="border: 5px solid #b58500;" allowfullscreen allow="autoplay"></iframe>',
      '</div>'
      ]
      save_file = os.path.join(top_dir, "website", "_recordings/", config['title']+".md")
      out_file = open(save_file, "w")
      for line in text_list:
        # write line to output file
        out_file.write(line)
        out_file.write("\n")
      out_file.close()
    elif which_data == "homework":
      this_dict = { 
         "filename" : os.path.splitext(rmd_file[0])[0], 
         "dirname" : dir, 
         "title" : config['title'],
         "due" : config['due'],
         "submit" : config['submit']
      }
    content_dict_list.append(this_dict)
    # back to top directory
    os.chdir(which_data_dir)
  yaml_contents = yaml.dump(content_dict_list, default_flow_style = False)
  # write to _data/lectures.yml file
  if which_data == "lecture":
    save_file = os.path.join(top_dir, "website", "_data/lectures.yml")
  else:
    save_file = os.path.join(top_dir, "website", "_data/homework.yml")
  with open(save_file, "wt") as f:
    f.write(yaml_contents)
    f.close()

# run function on inputted directory
input_dir = sys.argv[1]

make_data(input_dir, "lecture")
make_data(input_dir, "homework")

# make pages for additional videos
video_links = {
  "vim-survival-guide" : "16e493ae-2574-4eb9-b48e-ac2501201b59",
  "installing-wsl" : "b727d059-1996-4456-be5f-ad940005ea62",
  "installing-r-wsl" : "67d7ed3a-ca99-441e-8bd8-ac3300efb3cd",
  "wsl-in-sublime" : "4b6f4b7e-bb84-41ec-b04e-ada50141f670",
  "ssh-credentials-for-github" : "873afe7b-cad9-481d-abc8-adba01454266"
}

for key in video_links:
  text_list = ["---", "layout: default", "---", 
  '<div class="container">'
  '<iframe class="responsive-iframe" src="https://rsph.hosted.panopto.com/Panopto/Pages/Embed.aspx?id='+
  video_links[key]+
  '&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0'+
  '&interactivity=all" style="border: 5px solid #b58500;" allowfullscreen allow="autoplay"></iframe>',
  '</div>'
  ]
  save_file = os.path.join(input_dir, "website", "_recordings/", key + ".md")
  out_file = open(save_file, "w")
  for line in text_list:
    # write line to output file
    out_file.write(line)
    out_file.write("\n")
  out_file.close()
