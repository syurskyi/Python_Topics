_____ yagmail
_____ pandas
____ news _____ NewsFeed
_____ d__
_____ t__


___ send_email():
    today  d__.d__.n...strftime('%Y-%m-%d')
    yesterday  (d__.d__.n.. - d__.t..(days1)).strftime('%Y-%m-%d')
    news_feed  NewsFeed(interestrow['interest'],
                         from_dateyesterday,
                         to_datetoday)
    email  yagmail.SMTP(user"YOUR GMAIL ADDRESS", password"PASSWORD OF YOUR GMAIL ADDRESS")
    email.send(torow['email'],
               subjectf"Your {row['interest']} news for today!",
               contentsf"Hi {row['name']}\n See what's on about {row['interest']} today. \n{news_feed.get()}\nArdit")


w___ T...
    __ d__.d__.n...hour __ 13 a.. d__.d__.n...minute __ 28:
        df  pandas.read_excel('people.xlsx')

        ___ index, row __ df.iterrows():
            send_email()

    t__.sleep(60)
