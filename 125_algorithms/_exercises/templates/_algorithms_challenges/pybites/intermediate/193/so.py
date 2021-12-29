_______ requests
____ bs4 _______ BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


___ top_python_questions(url=cached_so_url):
   """Use requests to retrieve the url / html,
      parse the questions out of the html with BeautifulSoup,
      filter them by >= 1m views ("..m views").
      Return a list of (question, num_votes) tuples ordered
      by num_votes descending (see tests for expected output).
   """
   response = requests.get(url)
   soup = BeautifulSoup(response.text, "html.parser")
   ge_1m    # list
   lt_1m    # list

   question_summary = soup.find_all("div", class_="question-summary")
   ___ question __ question_summary:
      views = int(question.find("div", class_="views").get("title").s..(" ")[0].r..(",", ""))
      _question = question.find("a", class_="question-hyperlink").get_text()
      votes = int(question.find("span", class_="vote-count-post").get_text())
      
      __ views >= 1000000:
         ge_1m.a..((_question, votes))
      ____:
         lt_1m.a..((_question, votes))

   r.. s..(ge_1m, key=l.... x: x[1], r.._T..


__ __name__ __ "__main__":
   print(top_python_questions())