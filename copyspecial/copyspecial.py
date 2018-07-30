#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_spacial_paths(dir):
  result = []
  filenames = os.listdir(dir)
  for filename in filenames:
    match = re.search(r'__(\w+)__', filename)
    if match: 
      print filename
      result.append(os.path.abspath(os.path.join(dir, filename)))
  return result

def copy_to(source_files, destination):
  if not os.path.exists(destination):
    os.mkdir(destination)
  for source_file in source_files:
    base_name = os.path.basename(source_file)
    shutil.copy(source_file, os.path.join(destination, base_name))

def zip_to(source_files, zipfile):
  command = 'zip -j '+zipfile+' '+' '.join(source_files)
  print 'zip command: '+command
  (status, output) = commands.getstatusoutput(command)
  if status:
    sys.stderr.write(output)
    sys.exit(1)



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  # not args mean no arguments passed in
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  source_files = []
  for path in args:
    source_files.extend(get_spacial_paths(path))

  if todir:
    copy_to(source_files, todir)
  elif tozip:
    zip_to(source_files, tozip)
  else: 
    print "\n".join(source_files)


  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
