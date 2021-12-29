_____ w___
_____ os

____ filestack _____ Client
____ fpdf _____ FPDF


c_ PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill.
    """

    ___  -    filename):
        filename  filename

    ___ generate   flatmate1, flatmate2, bill):

        flatmate1_pay  st_(r__(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay  st_(r__(flatmate2.pays(bill, flatmate1), 2))

        pdf  FPDF(orientation'P', unit'pt', f..'A4')
        pdf.add_page()

        # Add icon
        pdf.image("for_python_topic/house.png", w30, h30)

        # Insert title
        pdf.set_font(family'Times', size24, style'B')
        pdf.cell(w0, h80, txt"Flatmates Bill", border0, align"C", ln1)

        # Insert Period label and value
        pdf.set_font(family"Times", size14, style'B')
        pdf.cell(w100, h40, txt"Period:", border0)
        pdf.cell(w150, h40, txtbill.period, border0, ln1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family"Times", size12)
        pdf.cell(w100, h25, txtflatmate1.name, border0)
        pdf.cell(w150, h25, txtflatmate1_pay, border0, ln1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w100, h25, txtflatmate2.name, border0)
        pdf.cell(w150, h25, txtflatmate2_pay, border0, ln1)

        # Change directory to for_python_topic, generate and open the PDF
        os.chdir("files")
        pdf.output(filename)
        w___.open(filename)


c_ FileSharer:

    ___  -    filepath, api_key"AViVqp7suSQWWEdrl6hf9z"):
        filepath  filepath
        api_key  api_key

    ___ share _
        client  Client(api_key)
        new_filelink  client.upload(filepathfilepath)
        r_ new_filelink.url