from bs4 import BeautifulSoup
import re
# source: https://www.virgin.com/richard-branson/my-top-10-quotes-living-life-better
HTML = """<!DOCTYPE html>
<head>
  <meta charset="utf-8" />
  <title>My top 10 quotes on living life better | Virgin</title>
</head>
<body>
  <div class="content">
    <p>I’m striving this year to maintain my fitness and to always be learning new things. The new theme on Virgin.com is Live Life Better – a series shining a spotlight on how we can all lead happier, healthier and more fulfilled lives. Virgin has always wanted to make things better for our team and customers and to improve their experiences.</p>
    <p>Here are my top 10 quotes on living life better for some New Year inspiration:</p>
    <p>10. "The beautiful thing about learning is nobody can take it away from you." - B.B King</p>
    <p>9. "Inexperience is an asset. Embrace it." - Wendy Kopp</p>
    <p>8. "Change will not come if we wait for some other person, or if we wait for some other time. We are the ones we’ve been waiting for. We are the change that we seek." - Barack Obama</p>
    <p>7. "The sky is not my limit… I am." - T.F. Hodge</p>
    <p>6. "Life is either a daring adventure or nothing at all." - Helen Keller</p>
    <p>5. "It does not matter how slowly you go as long as you do not stop." - Confucius</p>
    <p>4. "Too many of us are not living our dreams because we are living our fears." - Les Brown</p>
    <p>3. "Continuous efforts – not strength or intelligence – is the key to unlocking our potential." - Winston Churchill</p>
    <p>2. "Believe you can and you’re halfway there." - Theodore Roosevelt</p>
    <p>1. "Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be." - Zig Ziglar</p>
    <p>How do you try and live a healthier, happier life?</p>
  </div>
</body>
</html>"""


___ extract_quotes(html: str = HTML) -> dict:
    """See instructions in the Bite description"""
    soup = BeautifulSoup(html)

    author_to_quotes = {}

    quotes = soup.find_all('p')
    for quote in quotes:
        quote_text = quote.getText(strip=True)
        match = re.search(r'"(.+)"',quote_text)
        __ match:
            a = match.group(1)
        else:
            continue
        author = re.search(r'-\s?(.+)$',quote_text).group(1)


        author_to_quotes[author] = a


    return author_to_quotes





__ __name__ == "__main__":
    extract_quotes()

