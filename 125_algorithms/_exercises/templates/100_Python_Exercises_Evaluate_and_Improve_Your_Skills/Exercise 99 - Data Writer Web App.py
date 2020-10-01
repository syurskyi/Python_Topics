# #Create a program that asks the user to submit text a web app
# ____ flask ______ Flask, render_template_string, request
# app _ Flask( -n)
# html _ """
#   		      <div class="form">
#               <form action="{{url_for('sent')}}" method="POST">
#   			        <input title="Your email address will be safe with us." placeholder="Enter a line" type="text" name="line" required> <br>
#                 <button class="go-button" type="submit"> Submit </button>
#   		        </form>
#           </div>
# """
# @app.route("/")
# ___ index
#     r_ render_template_string(html)
# @app.route("/sent", methods_['GET', 'POST'])
# ___ sent
#     line _ N..
#     __ request.method __ 'POST':
#         line _ request.form['line']
#         w__ o..("user_input_flask.txt", "a+") __ file:
#             file.w..(line + "\n")
#         r_ render_template_string(html)
# __  -n __ "__main__":
#     app.run(debug_True)
