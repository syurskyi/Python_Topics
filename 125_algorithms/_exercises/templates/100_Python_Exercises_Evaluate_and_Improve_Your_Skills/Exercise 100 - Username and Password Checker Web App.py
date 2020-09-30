#Please create a web app that let's users submit a username and password
#The app checks if the username exists and the password satisfies three conditions as in exercise 81
from flask ______ Flask, render_template_string, request

app _ Flask( -n)

html _ """
  		      <div class="form">
              <form action="{{url_for('sent')}}" method="POST">
  			        <input title="Your email address will be safe with us." placeholder="Enter username" type="text" name="username" required> <br>
  			        <input title="Your email address will be safe with us." placeholder="Enter password" type="text" name="password" required> <br>
                    {{message|safe}}
                <button class="go-button" type="submit"> Submit </button>
  		        </form>
          </div>
"""

@app.route("/")
___ index
    r_ render_template_string(html)

@app.route("/sent", methods_['GET', 'POST'])
___ sent
    line _ None
    __ request.method __ 'POST':
        while T..:
            usr _ request.form['username']
            with open("users.txt", "r") as file:
                users _ file.readlines()
                users _ [i.strip("\n") ___ i __ users]
            __ usr __ users:
                r_ render_template_string(html, message_"Username exists!"+"<br>")
                continue
            ____
                print("Username is fine!")
                break
        while T..:
            notes _   # list
            psw _ request.form['password']
            __ not any(i.isdigit() ___ i __ psw):
                notes.ap..("You need at least one number")
            __ not any(i.isupper() ___ i __ psw):
                notes.ap..("You need at least one uppercase letter")
            __ le.(psw) < 5:
                notes.ap..("You need at least 5 characters")
            __ le.(notes) __ 0:
                print("Password is fine"+"<br>")
                break
            ____
                r_ render_template_string(html, message_"Please check password!")
        r_ render_template_string(html, message_"Success"+"<br>")
__  -n __ "__main__":
    app.run(debug_True)
