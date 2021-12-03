# What are these files?
These are the files of a Python program (a.k.a. App 2) built in the Udemy course  "The Complete Python Course in the Professional OOP Approach."
The course covers how to make this program step by step, plus nine other Python programs. 
If you want to learn Python, you can take the course for a high discount in the link below: 
https://www.udemy.com/course/the-python-pro-course/?referralCode=D1224FDF916B73D7E740
# What does the program do?
The program is written in Python and its purpose is to calculate the electricity bill share of two people 
living in the same flat. The app works through the command line interface. 
It gets as input the bill amount for a particular period
and the number of days that each of the flatmates stayed in the house for that period
and returns how much each flatmate has to pay. It also generates a PDF report
stating the names of the flatmates, the period, and how much each of them had to pay.
# How to run the program
1. Either clone this repo or download all these files by going to _Code -> Download ZIP_.
2. Create a PyCharm (or other IDE) project and configure a Python interpreter for the project.
3. Open the terminal and install the required packages by running:
   `pip install -r requirements.txt`
4. Go to https://www.filestack.com/, and create a Filestack account to get an API key.
5. Go to _reports.py_, and change the "INSERT YOUR API KEY HERE" string to your own Filestack API key.
6. Run _main.py_ with Python.
7. The expected output is a PDF created inside _files_ folder.