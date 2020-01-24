# Version 1
#
# Loop over donations, add all the VALUES together and store in a variable called total_donations

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0

for donation in donations.values():
    total_donations += donation

# Advanced Version 1 -
#
# This solution uses a built-in function called sum() which I cover in the "Lambdas and Built-In Functions" section.
# We haven't talked about how it works, but if you're curious...

total_donations = sum(donation for donation in donations.values())

# Advanced Version 2
#
# An even better solution using the same sum built-in function is just this nice little line:

total_donations = sum(donations.values())