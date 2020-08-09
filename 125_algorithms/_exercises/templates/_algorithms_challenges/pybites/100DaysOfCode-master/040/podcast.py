from email.mime.text ______ MIMEText
______ os
______ random
______ shelve
______ smtplib
______ sys
______ time

______ feedparser
______ schedule

CACHE = 'cache'


class Episode:

    ___ __init__(self, id, title, link
        self.id = id
        self.title = title
        self.link = link
        self.done = False

    ___ __str__(self
        status = 'done' __ self.done else 'not done'
        r_ 'Podcast {}: {} - {} (status: "{}")'.format(self.id, self.title, self.link, status)


___ store_new_episodes(feed
    episodes = _parse_feed(feed)
    _update_cache(episodes)


___ _parse_feed(feed
    ___ e in feedparser.parse(feed)['entries']:
        id, title, link = e.get('id'), e.get('title'), e.get('link')
        yield Episode(id, title, link)


___ _update_cache(episodes
    with shelve.open(CACHE) as s:
        ___ ep in episodes:
            __ ep.id not in s:
                s[ep.id] = ep


___ get_random_episode(
    with shelve.open(CACHE) as s:
        episodes = list(s.keys())
        random.shuffle(episodes)
        ___ key in episodes:
            ep = s[key]
            __ ep.done:
                print('Nope cannot take this episode as already listened ({})'.format(ep))
                continue
            print('Episode to listen to next: {}'.format(ep))
            ep.done = True
            s[key] = ep
            r_ ep
        ____
            print('No unplayed episodes, stay tuned')


___ mail_episode(ep
    # ok did cheat here, got this from cverna
    # https://github.com/pybites/challenges/blob/community/17/cverna/podcast.py
    # TODO: test on server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_account = os.environ.get('MAIL_ACCOUNT') or sys.exit('Need mail user')
    smtp_password = os.environ.get('MAIL_PASSWORD') or sys.exit('Need mail pw')
    mailto = os.environ.get('MAILTO') or sys.exit('Need mail to')
    smtp_server.ehlo()
    smtp_server.starttls()
    try:
        smtp_server.login(smtp_account, smtp_password)
    except smtplib.SMTPAuthenticationError:
        print('Could not login to the smtp server please check your username and password')
        sys.exit(1)
    msg = MIMEText('\nHi this week podcast is {} you can download it from here {}'.
                   format(ep.title, ep.link))
    msg['Subject'] = 'My podcast of the week'
    msg['From'] = smtp_account
    msg['To'] = mailto
    smtp_server.send_message(msg)
    smtp_server.quit()


__ __name__ __ '__main__':
    __ le.(sys.argv) < 2:
        print('Specify a feed rss feed please')
        sys.exit(1)

    feed = sys.argv[1]

    schedule.every().tuesday.at("9:00").do(store_new_episodes, feed)
    schedule.every().wednesday.at("10:52").do(get_random_episode)

    w___ True:
        schedule.run_pending()
        time.sleep(1)
