_____ webbrowser
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
        filename = filename

    ___ generate   flatmate1, flatmate2, bill):

        flatmate1_pay = st_(r__(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = st_(r__(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("for_python_topic/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Change directory to for_python_topic, generate and open the PDF
        os.chdir("files")
        pdf.output(filename)
        webbrowser.open(filename)


c_ FileSharer:

    ___  -    filepath, api_key="AViVqp7suSQWWEdrl6hf9z"):
        filepath = filepath
        api_key = api_key

    ___ share _
        client = Client(api_key)
        new_filelink = client.upload(filepath=filepath)
        r_ new_filelink.url