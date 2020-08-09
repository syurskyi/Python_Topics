#!python3
#This Flask app displays photos in a directory. The app will eventually allow you to display photos
#based on file name search criteria. ie: Searching for "2017" will display all photos with 2017 in their
#file name.

from flask ______ Flask, render_template
______ glob

PATH = "static/images/"

app = Flask(__name__)

@app.route('/')
___ index(
    photo_list = get_photos()
    r_ render_template('index.html',
                            photo_list=photo_list)


___ get_photos(
    photo_list = []
    for name in sorted(glob.glob(PATH + "*")):
        photo_list.append(name)
    r_ photo_list

__ __name__ __ "__main__":
    app.run()
