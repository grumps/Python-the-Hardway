#This script cleans up the temp files that get greated, when using a text editor on linux.
# Assumptions:
# 1. You follow the folder structure I have in Github
# 2. You storing the file's in your home directory. If not, then cd to the folder and execute.


find -name \*.py~ -exec rm -v {} \ >log;
find -name \*.pyc -exec rm -v {} \ >>log;