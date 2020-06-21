#!/bin/bash
# Ask the user for their name
echo Insert source file name
read varname
# echo It\'s nice to meet you $varname
pyuic5 -x $varname.ui -o $varname.py