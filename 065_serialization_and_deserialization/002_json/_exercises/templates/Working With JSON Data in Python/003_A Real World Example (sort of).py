# # -*- coding: utf-8 -*-
#
# # A Real World Example (sort of)
# # For your introductory example, you’ll use JSONPlaceholder, a great source of fake JSON data for practice purposes.
# # First create a script file called scratch.py, or whatever you want. I can’t really stop you.
# # You’ll need to make an API request to the JSONPlaceholder service, so just use the requests package to do the heavy
# # lifting. Add these imports at the top of your file:
#
# ______ ____
# ______ req..
#
# # Now, you’re going to be working with a list of TODOs cuz like…you know, it’s a rite of passage or whatever.
# # Go ahead and make a request to the JSONPlaceholder API for the /todos endpoint. If you’re unfamiliar with requests,
# # there’s actually a handy json() method that will do all of the work for you, but you can practice using
# # the json library to deserialize the text attribute of the response object. It should look something like this:
# #
# response = req__.g.. https://jsonplaceholder.typicode.com/todos
# todos = ____.l.. ?.t..
#
# # You don’t believe this works? Fine, run the file in interactive mode and test it for yourself. While you’re at it,
# # check the type of todos. If you’re feeling adventurous, take a peek at the first 10 or so items in the list.
# #
# print(t.. __ r__.____
# # True
# print(ty.. t..
# # <class 'list'>
# print(t.. ;10
# # ...
#
# # See, I wouldn’t lie to you, but I’m glad you’re a skeptic.
# # What’s interactive mode? Ah, I thought you’d never ask! You know how you’re always jumping back and forth between
# # the your editor and the terminal? Well, us sneaky Pythoneers use the -i interactive flag when we run the script.
# # This is a great little trick for testing code because it runs the script and then opens up an interactive command
# # prompt with access to all the data from the script!
# # All right, time for some action. You can see the structure of the data by visiting the endpoint in a browser,
# # but here’s a sample
#
# {
#     "userId": 1,
#     "id": 1,
#     "title": "delectus aut autem",
#     "completed": False
# }
# # There are multiple users, each with a unique userId, and each task has a Boolean completed property. Can you determine which users have completed the most tasks?
# #
# # # Map of userId to number of complete TODOs for that user
# todos_by_user = {}
# #
# # # Increment complete TODOs count for each user.
# ___ todo __ t..
#     __ ?["completed"]
#         ___
#             # Increment the existing user's count.
#             ?|t.. "userId'|| += 1
#         ____ K..
#             # This user has not been seen. Set their count to 1.
#             ? t.. "userId"|| _ 1
#
# # Create a sorted list of (userId, num_complete) pairs.
# top_users = so.. ?.i..
#                    k.._ l___ x ? 1| re.. _ T..
#
# # Get the maximum number of complete TODOs.
# max_complete = ? 0 1
#
# # Create a list of all users who have completed
# # the maximum number of TODOs.
# users = []
# ___ user, num_complete __ to..
#     __ nu_c. < ma_c.
#         b..
#     ?.ap.. st. ?
#
# max_users = " and ".jo.. ?
#
# # Yeah, yeah, your implementation is better, but the point is, you can now manipulate the JSON data as a normal
# # Python object!
# # I don’t know about you, but when I run the script interactively again, I get the following results:
# #
# s = "s" __ le. ? > 1 else ""
# print(_ *user@ @m_u. completed @m_c. TODOs
# # users 5 and 10 completed 12 TODOs
# # That’s cool and all, but you’re here to learn about JSON. For your final task, you’ll create a JSON file that contains
# # the completed TODOs for each of the users who completed the maximum number of TODOs.
# # All you need to do is filter todos and write the resulting list to a file. For the sake of originality, you can call
# # the output file filtered_data_file.json. There are may ways you could go about this, but here’s one:
# #
# # # Define a function to filter out completed TODOs
# # # of users with max completed TODOS.
# ___ keep todo
#     is_complete _ ? "completed"|
#     has_max_count _ st. ? "userId"|| __ u..
#     r_ ? an. ?
#
# # # Write filtered TODOs to file.
# w___ o.. filtered_data_file.json _ __ data_file
#     filtered_todos _ li.. fi. k.. t..
#     ____.d.. ? d.. i.. _ 2
# # Perfect, you’ve gotten rid of all the data you don’t need and saved the good stuff to a brand new file! Run the script
# # again and check out filtered_data_file.json to verify everything worked. It’ll be in the same directory as scratch.py
# # when you run it.
# # Now that you’ve made it this far, I bet you’re feeling like some pretty hot stuff, right? Don’t get cocky: humility is
# # a virtue. I am inclined to agree with you though. So far, it’s been smooth sailing, but you might want to batten down
# # the hatches for this last leg of the journey.
