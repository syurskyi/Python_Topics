____ fpdf _____ FPDF
_____ random
_____ string
_____ sqlite3


c_ User:
    """Represents a user that can buy a cinema Seat"""

    ___  -    name):
        name  name

    ___ buy   seat, card):
        """Buys the ticket if the card is valid"""
        __ seat.is_free():
            __ card.validate(priceseat.get_price()):
                seat.occupy()
                ticket  Ticket(user  self, priceseat.get_price(), seat_numberseat_id)
                ticket.to_pdf()
                r_ "Purchase successful!"
            ____:
                r_ "There was a problem with your card!"
        ____:
            r_ "Seat is taken!"


c_ Seat:
    """Represents a cinema seat that can be taken from a User"""

    database  "cinema.db"

    ___  -    seat_id):
        seat_id  seat_id

    ___ get_price _
        """Get the price of a certain seat"""
        connection  sqlite3.connect(database)
        cursor  connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [seat_id])
        price  cursor.fetchall()[0][0]
        r_ price

    ___ is_free _
        """Check in the database if a Seat is taken or not"""
        connection  sqlite3.connect(database)
        cursor  connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [seat_id])
        result  cursor.fetchall()[0][0]

        __ result __ 0:
            r_ T..
        ____:
            r_ F..

    ___ occupy _
        """Change value of taken in the database from 0 to 1 if Seat is free"""
        __ is_free():
            connection  sqlite3.connect(database)
            connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
            """, [1, seat_id])
            connection.commit()
            connection.close()

c_ Card:
    """ Represents a bank card needed to finalize a Seat purchase"""

    database  "banking.db"

    ___  -    t.., number, cvc, holder):
        holder  holder
        cvc  cvc
        number  number
        t..  t..

    ___ validate   price):
        """Checks if Card is valid and has balance.
        Subtracts price from balance.
        """
        connection  sqlite3.connect(database)
        cursor  connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [number, cvc])
        result  cursor.fetchall()

        __ result:
            balance  result[0][0]
            __ balance > price:
                connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number"=? and "cvc"=?
                """, [balance - price, number, cvc])
                connection.commit()
                connection.close()
                r_ T..


c_ Ticket:
    """Represents a cinema Ticket purchased by a User"""

    ___  -    user, price, seat_number):
        user  user
        price  price
        id  "".j..([random.choice(string.ascii_letters) ___ i __ r..(8)])
        seat_number  seat_number

    ___ to_pdf _
        """Creates a PDF ticket"""
        pdf  FPDF(orientation'P', unit'pt', f..'A4')
        pdf.add_page()

        pdf.set_font(family"Times", style"B", size24)
        pdf.cell(w0, h80, txt"Your Digital Ticket", border1, ln1, align"C")

        pdf.set_font(family"Times", style"B", size14)
        pdf.cell(w100, h25, txt"Name: ", border1)
        pdf.set_font(family"Times", style"", size12)
        pdf.cell(w0, h25, txtuser.name, border1, ln1)
        pdf.cell(w0, h5, txt"", border0, ln1)

        pdf.set_font(family"Times", style"B", size14)
        pdf.cell(w100, h25, txt"Ticket ID", border1)
        pdf.set_font(family"Times", style"", size12)
        pdf.cell(w0, h25, txtid, border1, ln1)
        pdf.cell(w0, h5, txt"", border0, ln1)

        pdf.set_font(family"Times", style"B", size14)
        pdf.cell(w100, h25, txt"Price", border1)
        pdf.set_font(family"Times", style"", size12)
        pdf.cell(w0, h25, txtst_(price), border1, ln1)
        pdf.cell(w0, h5, txt"", border0, ln1)

        pdf.set_font(family"Times", style"B", size14)
        pdf.cell(w100, h25, txt"Seat Number", border1)
        pdf.set_font(family"Times", style"", size12)
        pdf.cell(w0, h25, txtst_(seat_number), border1, ln1)
        pdf.cell(w0, h5, txt"", border0, ln1)

        pdf.output("sample.pdf", 'F')


__ __name__ __ "__main__":

    name  i__("Your full name: ")
    seat_id  i__("Preferred seat number: ")
    card_type  i__("Your card type: ")
    card_number  i__("Your card number: ")
    card_cvc  i__("Your card cvc: ")
    card_holder  i__("Card holder name: ")

    user  User(namename)
    seat  Seat(seat_idseat_id)
    card  Card(typecard_type, numbercard_number, cvccard_cvc, holdercard_holder)

    print(user.buy(seatseat, cardcard))




