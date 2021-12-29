# #Create a program that asks the user to submit text a web app
# ____ flask _______ Flask, render_template_string, request
# app = Flask(__name__)
# html = """
#   		      <div class="form">
#               <form action="{{url_for('sent')}}" method="POST">
#   			        <input title="Your email address will be safe with us." placeholder="Enter a line" type="text" name="line" required> <br>
#                 <button class="go-button" type="submit"> Submit </button>
#   		        </form>
#           </div>
# """
# @app.route("/")
# ___ index():
#     r.. render_template_string(html)
# @app.route("/sent", methods=['GET', 'POST'])
# ___ sent():
#     line = None
#     __ request.method __ 'POST':
#         line = request.form['line']
#         w.. o..("user_input_flask.txt", "a+") __ file:
#             file.w..(line + "\n")
#         r.. render_template_string(html)
# __ __name__ __ "__main__":
#     app.run(debug=True)
