_____ yagmail
_____ pandas
____ news _____ NewsFeed
_____ datetime
_____ t__


___ send_email():
    today  datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday  (datetime.datetime.now() - datetime.timedelta(days1)).strftime('%Y-%m-%d')
    news_feed  NewsFeed(interestrow['interest'],
                         from_dateyesterday,
                         to_datetoday)
    email  yagmail.SMTP(user"YOUR GMAIL ADDRESS", password"PASSWORD OF YOUR GMAIL ADDRESS")
    email.send(torow['email'],
               subjectf"Your {row['interest']} news for today!",
               contentsf"Hi {row['name']}\n See what's on about {row['interest']} today. \n{news_feed.get()}\nArdit")


w___ T...
    __ datetime.datetime.now().hour __ 13 and datetime.datetime.now().minute __ 28:
        df  pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    t__.sleep(60)
