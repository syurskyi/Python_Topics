# What are these files?
These are the files of a Python program (a.k.a. App 10) built in the Udemy course  "The Complete Python Course in the Professional OOP Approach."
The course covers how to make this program step by step, plus nine other Python programs. 
If you want to learn Python, you can take the course for a high discount in the link below: 
https://www.udemy.com/course/the-python-pro-course/?referralCode=D1224FDF916B73D7E740
# What does the program do?
The program is written in Python. The program interacts with the user through a command line interface.
The user chooses a cinema seat they wish to buy (e.g., A1, A2, B1, or B2), enter their credit card credentials 
and finalize the purchase. The program accesses the Seat table of the cinema database to check
if the requested seat is available. It also accesses the Cards table of the banking database to check 
if the user has balance and subtracts the seat price from the balance.
# How to run the program
1. Either clone this repo or download all these files by going to _Code -> Download ZIP_.
2. Create a PyCharm (or other IDE) project and configure a Python interpreter for the project.
3. Open the terminal and install the required packages by running:
   `pip install -r requirements.txt`
3. Run _main.py_ with Python.
4. Enter the required input in the command line. For example:
```
Your full name: John Smith
Preferred seat number: A3
Your card type: Visa
Your card number: 12345678
Your card cvc: 123
Card holder name: John Smith
```
5. The output will be a _sample.pdf_ file containing the cinema ticket if the purchase was successful. 
   The program also updates the cinema.db and the banking.db databases.