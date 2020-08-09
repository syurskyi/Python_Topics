from datetime ______ datetime
from email.mime.multipart ______ MIMEMultipart
from email.mime.text ______ MIMEText
______ os
______ smtplib
______ sys

from themoviedb ______ get_genres_cache

BASE_IMG_URL = 'http://image.tmdb.org/t/p/w92{}'
BASE_MOVIE_URL = 'https://www.themoviedb.org/{}/{}'
SUBJECT = 'Movies / Series Digest'
GENRES = get_genres_cache()

FROM_MAIL = os.environ.get('FROM_MAIL')
TO_MAIL = os.environ.get('TO_MAIL')

__ not FROM_MAIL or not TO_MAIL:
    print('set FROM_MAIL and TO_MAIL in env')
    sys.exit(1)

# I know: html tables suck, but necessary in html emails
# TODO: retrieve director and actors (and filters)
TEMPLATE = '''<tr>
                <td style='margin: 5px; vertical-align:top;'>
                    <img src="{img}" style="float: right;">
                </td>
                <td style='margin: 5px; vertical-align:top;'>
                    <ul>
                        <li><strong><a href="{link}">{title}</a></strong></li>
                        <li>Overview: {overview}</li>
                        <li>Genres: {genres}</li>
                        <li>(First) release: {release}</li>
                    </ul>
                </td>
              </tr>
            '''


___ generate_mail_msg(items
    output = []

    ___ kind in items:
        output.append('<h2>{}</h2>'.format(kind.upper()))

        ___ listing, entries in items[kind].items(
            listing_header = listing.replace('_', ' ').title()
            output.append('<h3>{}</h3>'.format(listing_header))

            __ not entries:
                output.append('No new items')
                continue

            output.append('<table>')
            ___ entry in sorted(entries,
                                key=lambda x: datetime.strptime(
                                              x.release_date, '%Y-%m-%d'),
                                reverse=True

                img = BASE_IMG_URL.format(entry.poster)
                kind_for_url = kind.replace('movies', 'movie')
                url = BASE_MOVIE_URL.format(kind_for_url, entry.id)
                genres = ', '.join([GENRES.get(gen) ___ gen in entry.genres
                                    __ GENRES.get(gen)])

                output.append(TEMPLATE.format(link=url,
                                              title=entry.title,
                                              overview=entry.overview,
                                              img=img,
                                              genres=genres,
                                              release=entry.release_date))
            output.append('</table>')

    r_ '\n'.join(output)


___ mail_msg(content, recipients=TO_MAIL, subject=SUBJECT
    __ isinstance(recipients, list
        recipients = ', '.join(recipients)

    sender = FROM_MAIL

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients

    part = MIMEText(content, 'html')
    msg.attach(part)

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipients, msg.as_string())
    s.quit()
