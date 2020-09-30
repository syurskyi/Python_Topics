from collections ______ namedtuple
from datetime ______ datetime
from email.mime.multipart ______ MIMEMultipart
from email.mime.text ______ MIMEText
______ os
______ smtplib
______ sys

from bs4 ______ BeautifulSoup as Soup
______ requests

FROM_MAIL = os.environ.get('FROM_MAIL') or sys.exit('set FROM_MAIL in env')

BASE_URL = 'https://www.packtpub.com'
FREE_LEARNING_PAGE = 'free-learning'
PACKT_FREE_LEARNING_LINK = BASE_URL + '/packt/offers/' + FREE_LEARNING_PAGE

TIME_LEFT = '{} hours and {} minutes'
SUBJECT = 'Free Packt ebook of the day: {} (time left: {})'
HEADERS = {'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

Book = namedtuple('Book', 'title description summary image link timeleft')


___ retrieve_page_html(
    __ os.path.isfile(FREE_LEARNING_PAGE
        with open(FREE_LEARNING_PAGE) as f:
            r_ f.read()
    ____
        r_ requests.get(PACKT_FREE_LEARNING_LINK, headers=HEADERS).text


___ _create_time_left_string(countdown_unix_tstamp
    expires = datetime.fromtimestamp(int(countdown_unix_tstamp))
    now = datetime.now()
    left = str(expires - now)
    hh, mm, _ = left.split(':')
    r_ TIME_LEFT.format(hh, mm)


___ extract_book_data_page(content
    soup = Soup(content, 'html.parser')
    book_image = soup.find('div', {'class': 'dotd-main-book-image'})
    link = BASE_URL + book_image.find('a').get('href')
    image = 'https:' + book_image.find('img').get('src')
    book_main = soup.find('div', {'class': 'dotd-main-book-summary'})
    title_div = book_main.find('div', {'class': 'dotd-title'})
    title = title_div.find('h2').text.strip()
    descr_div = title_div.find_next_sibling("div")
    description = descr_div.text.strip()
    summary_html = descr_div.find_next_sibling("div")
    # sometimes 2nd paragraph = form, then don't include it
    __ 'dotd-main-book-form' __ str(summary_html
        summary_html = ''
    js_countdown = book_main.find('span', {'class': 'packt-js-countdown'})
    countdown = js_countdown.get('data-countdown-to')
    timeleft = _create_time_left_string(countdown)
    r_ Book(title=title,
                description=description,
                summary=summary_html,
                image=image,
                link=link,
                timeleft=timeleft)


___ generate_mail_msg(book
    r_ '''<h2><a href='{link}'>{title}</a></h2>
        <div>{description}</div>
        {summary_html}
        <hr>
        <img src='{image}' title='{title}'>
        <hr>
        <h2>Download</h2>
        <p>Automating Captchas sucks. Just go to 
        <a href='{url}'>{url}</a>, login and grab 
        your copy. <strong>Enjoy!</strong></p>'''.format(
                link=book.link,
                title=book.title,
                description=book.description,
                image=book.image,
                summary_html=book.summary,
                url=PACKT_FREE_LEARNING_LINK)


___ mail_html(recipients, subject, content
    sender = FROM_MAIL
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    part = MIMEText(content, 'html')
    msg.attach(part)
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()


__  -n __ '__main__':
    __ le.(sys.argv) < 2:
        print('Usage {} email1 email2 ...'.format(sys.argv[0]))
        sys.exit(1)

    recipients = sys.argv[1:]

    content = retrieve_page_html()
    book = extract_book_data_page(content)

    subject = SUBJECT.format(book.title, book.timeleft)
    msg_body = generate_mail_msg(book)

    mail_html(recipients, subject, msg_body)
