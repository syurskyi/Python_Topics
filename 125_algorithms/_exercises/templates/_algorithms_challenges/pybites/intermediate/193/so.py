_______ r__
____ ___ _______ B..

cached_so_url 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


___ top_python_questions url_?
   """Use requests to retrieve the url / html,
      parse the questions out of the html with BeautifulSoup,
      filter them by >= 1m views ("..m views").
      Return a list of (question, num_votes) tuples ordered
      by num_votes descending (see tests for expected output).
   """
   response r__.g.. url)
   soup B..(?.t.., "html.parser")
   ge_1m    # list
   lt_1m    # list

   question_summary ?.f.. "div", c.._"question-summary")
   ___ question __ question_summary:
      views i..(question.f.. "div", c.._"views").g.. "title").s..(" " 0.r..(",", ""
      _question question.f.. "a", c.._"question-hyperlink").g.. 
      votes i..(question.f.. "span", c.._"vote-count-post").get_text
      
      __ views >_ 1000000:
         ge_1m.a..((_question, votes
      ____
         lt_1m.a..((_question, votes

   r.. s..(ge_1m, k.._l.... x: ? 1 r.._T..


__ _______ __ _______
   print(top_python_questions