# #Please create a web app that let's users submit a username and password
# #The app checks if the username exists and the password satisfies three conditions as in exercise 81
# ____ flask ______ Flask, render_template_string, request
#
# app _ Flask( -n)
#
# html _ """
#   		      <div class="form">
#               <form action="{{url_for('sent')}}" method="POST">
#   			        <input title="Your email address will be safe with us." placeholder="Enter username" type="text" name="username" required> <br>
#   			        <input title="Your email address will be safe with us." placeholder="Enter password" type="text" name="password" required> <br>
#                     {{message|safe}}
#                 <button class="go-button" type="submit"> Submit </button>
#   		        </form>
#           </div>
# """
#
# @app.route("/")
# ___ index
#     r_ render_template_string(html)
#
# @app.route("/sent", methods_['GET', 'POST'])
# ___ sent
#     line _ N..
#     __ request.method __ 'POST':
#         w___ T..:
#             usr _ request.form['username']
#             w__ o..("users.txt", _ __ file:
#                 users _ file.r_l_()
#                 users _ [i.s..("\n") ___ i __ users]
#             __ usr __ users:
#                 r_ render_template_string(html, message_"Username exists!"+"<br>")
#                 c..
#             ____
#                 print("Username is fine!")
#                 b..
#         w___ T..:
#             notes _   # list
#             psw _ request.form['password']
#             __ no. an.(i.isd.. ___ i __ psw):
#                 notes.ap..("You need at least one number")
#             __ no. an.(i.isu.. ___ i __ psw):
#                 notes.ap..("You need at least one uppercase letter")
#             __ le.(psw) < 5:
#                 notes.ap..("You need at least 5 characters")
#             __ le.(notes) __ 0:
#                 print("Password is fine"+"<br>")
#                 b..
#             ____
#                 r_ render_template_string(html, message_"Please check password!")
#         r_ render_template_string(html, message_"Success"+"<br>")
# __  -n __ "__main__":
#     app.run(debug_True)
