#!python3
#save_screenshot.py is a script to take a screenshot and save it to a specified directory.

______ os
______ pyscreeze

#the save path is only necessary if you need to save the file anywhere
#other than where the script is being run from
SAVE_PATH = "/Users/pybites/screenshots"

___ change_dir(
    os.chdir(SAVE_PATH)

___ take_screenshot(
    filename = input("What do you want to name the screenshot? ")
    pyscreeze.screenshot(filename + ".png")

__ __name__ __ '__main__':
    change_dir() #comment out if you don't need a specific path
    take_screenshot()
	
