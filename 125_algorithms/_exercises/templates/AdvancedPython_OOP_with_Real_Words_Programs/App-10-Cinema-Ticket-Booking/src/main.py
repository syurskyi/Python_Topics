____ fpdf _____ FPDF
_____ random
_____ string
_____ sqlite3


c_ User:
    """Represents a user that can buy a cinema Seat"""

    ___  -    name):
        name = name

    ___ buy   seat, card):
        """Buys the ticket if the card is valid"""
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                ticket = Ticket(user = self, price=seat.get_price(), seat_number=seat_id)
                ticket.to_pdf()
                r_ "Purchase successful!"
            else:
                r_ "There was a problem with your card!"
        else:
            r_ "Seat is taken!"


c_ Seat:
    """Represents a cinema seat that can be taken from a User"""

    database = "cinema.db"

    ___  -    seat_id):
        seat_id = seat_id

    ___ get_price _
        """Get the price of a certain seat"""
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [seat_id])
        price = cursor.fetchall()[0][0]
        r_ price

    ___ is_free _
        """Check in the database if a Seat is taken or not"""
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [seat_id])
        result = cursor.fetchall()[0][0]

        if result == 0:
            r_ True
        else:
            r_ False

    ___ occupy _
        """Change value of taken in the database from 0 to 1 if Seat is free"""
        if is_free():
            connection = sqlite3.connect(database)
            connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
            """, [1, seat_id])
            connection.commit()
            connection.close()

c_ Card:
    """ Represents a bank card needed to finalize a Seat purchase"""

    database = "banking.db"

    ___  -    type, number, cvc, holder):
        holder = holder
        cvc = cvc
        number = number
        type = type

    ___ validate   price):
        """Checks if Card is valid and has balance.
        Subtracts price from balance.
        """
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
        """, [number, cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number"=? and "cvc"=?
                """, [balance - price, number, cvc])
                connection.commit()
                connection.close()
                r_ True


c_ Ticket:
    """Represents a cinema Ticket purchased by a User"""

    ___  -    user, price, seat_number):
        user = user
        price = price
        id = "".join([random.choice(string.ascii_letters) for i in range(8)])
        seat_number = seat_number

    ___ to_pdf _
        """Creates a PDF ticket"""
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", border=1, ln=1, align="C")

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Name: ", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=st_(price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family="Times", style="", size=12)
        pdf.cell(w=0, h=25, txt=st_(seat_number), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output("sample.pdf", 'F')


if __name__ == "__main__":

    name = i__("Your full name: ")
    seat_id = i__("Preferred seat number: ")
    card_type = i__("Your card type: ")
    card_number = i__("Your card number: ")
    card_cvc = i__("Your card cvc: ")
    card_holder = i__("Card holder name: ")

    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

    print(user.buy(seat=seat, card=card))




