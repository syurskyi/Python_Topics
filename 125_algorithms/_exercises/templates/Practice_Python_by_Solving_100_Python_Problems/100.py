# #Please create a web app that let's users submit a username and password
# #The app checks if the username exists and the password satisfies three conditions as in exercise 81
# ____ flask _______ Flask, render_template_string, request
#
# app = Flask(__name__)
#
# html = """
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
# ___ index():
#     r.. render_template_string(html)
#
# @app.route("/sent", methods=['GET', 'POST'])
# ___ sent():
#     line = None
#     __ request.method __ 'POST':
#         w__ ?
#             usr = request.form['username']
#             w.. o..("users.txt", ?   __ file:
#                 users = file.readlines()
#                 users = [i.s..("\n") ___ i __ users]
#             __ usr __ users:
#                 r.. render_template_string(html, message="Username exists!"+"<br>")
#                 c__
#             ____
#                 print("Username is fine!")
#                 b__
#         w__ ?
#             notes = ?  #list
#             psw = request.form['password']
#             __ n__ a..(i.isd.. ___ i __ psw):
#                 notes.a..("You need at least one number")
#             __ n__ a..(i.isu ___ i __ psw):
#                 notes.a..("You need at least one uppercase letter")
#             __ l..(psw) < 5:
#                 notes.a..("You need at least 5 characters")
#             __ l..(notes) __ 0:
#                 print("Password is fine"+"<br>")
#                 b__
#             ____
#                 r.. render_template_string(html, message="Please check password!")
#         r.. render_template_string(html, message="Success"+"<br>")
# __ __name__ __ "__main__":
#     app.run(debug=True)
