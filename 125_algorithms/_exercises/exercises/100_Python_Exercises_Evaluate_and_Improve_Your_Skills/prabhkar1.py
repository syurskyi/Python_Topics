w__ o.. 'requests1.py','w+' __ file:

    file.writelines 'import requests \
                  r = requests.get("http://www.pythonhow.com") \
                    print(r.text[:100])'