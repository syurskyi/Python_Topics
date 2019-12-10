# wealth-maneger
This program is going to calculate 
how many years will it take to generate a passive given income from renting apts.

How to use this program: 

Step 1: write down the answers to the following questions: <br />
1- How much passive income do you want in a year?<br /> 
2- How much money you can invest in a year? <br />
3- What is the year when you are going to start investing? <br />
4- How much does it cost to buy an apt where you're from? <br />
5- How much money yearly you will get from renting the apt that you have bought? 


Step 2: create an object from the Calculator class, and pass in all the above answers. 
Ex. My answers are: <br />
For question one is: 300000<br />
For question two is: 70000<br />
For question three is: 2019<br />
For question four is: 80000<br />
For question five is: 6666<br />

calculator_obj = Calculator(300000, 70000, 2019, 80000, 6666)

Step 3: use the the name of the object to call the method print_results() to print the results.
Ex. calculator_obj.print_results()

Now you should see the results. These results will show you how many years you will need to invest to get to your passive
income goal. 

Here is the output: 

Year number: 2019, Apt number owned 0 Passive Income $70000<br />
Year number: 2020, Apt number owned 1.0 Passive Income $66666<br />
Year number: 2021, Apt number owned 2.0 Passive Income $69998<br />
Year number: 2022, Apt number owned 3.0 Passive Income $79996<br />
Year number: 2023, Apt number owned 4.0 Passive Income $96660<br />
Year number: 2024, Apt number owned 6.0 Passive Income $46656<br />
Year number: 2025, Apt number owned 7.0 Passive Income $83318<br />
Year number: 2026, Apt number owned 8.0 Passive Income $126646<br />
Year number: 2027, Apt number owned 10.0 Passive Income $103306<br />
Year number: 2028, Apt number owned 12.0 Passive Income $93298<br />
Year number: 2029, Apt number owned 14.0 Passive Income $96622<br />
Year number: 2030, Apt number owned 16.0 Passive Income $113278<br />
Year number: 2031, Apt number owned 18.0 Passive Income $143266<br />
Year number: 2032, Apt number owned 20.0 Passive Income $186586<br />
Year number: 2033, Apt number owned 23.0 Passive Income $169904<br />
Year number: 2034, Apt number owned 25.0 Passive Income $246554<br />
Year number: 2035, Apt number owned 28.0 Passive Income $263202<br />
Year number: 2036, Apt number owned 32.0 Passive Income $226514<br />
Year number: 2037, Apt number owned 35.0 Passive Income $289824<br />
Year number: 2038, Apt number owned 39.0 Passive Income $299798<br />
Year number: 2039, Apt number owned 43.0 Passive Income $336436<br />
Year number: 2040, Apt number owned 48.0 Passive Income $326404<br />
You can reach a passive income of $300000, but it will take: 22 years<br />

So, based on the information that I have passed here: Calculator(300000, 70000, 2019, 80000, 6666). 
It will take me 22 years to get a passive income of $300000. 
