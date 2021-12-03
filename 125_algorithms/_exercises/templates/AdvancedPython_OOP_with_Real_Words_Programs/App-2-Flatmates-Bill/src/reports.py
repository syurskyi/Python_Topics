# _____ webbrowser
# _____ __
#
# ____ filestack _____ Client
# ____ fpdf _____ FPDF
#
#
# c_ PdfReport
#     """
#     Creates a Pdf file that contains data about
#     the flatmates such as their names, their due amounts
#     and the period of the bill.
#     """
#
#     ___  -    filename
#         ? = ?
#
#     ___ generate   flatmate1, flatmate2, bill
#
#         flatmate1_pay = st_ r__ f_1.p.. b.. f__2) 2
#         flatmate2_pay = st_ r__ f_2.p.. b.. f__1) 2
#
#         pdf = F.. orientation='P', unit='pt', format='A4')
#         ?.a..
#
#         # Add icon
#         ?.image("for_python_topic/house.png", w=30, h=30)
#
#         # Insert title
#         ?.set_font(family='Times', size=24, style='B')
#         ?.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
#
#         # Insert Period label and value
#         ?.set_font(family="Times", size=14, style='B')
#         ?.cell(w=100, h=40, txt="Period:", border=0)
#         ?.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
#
#         # Insert name and due amount of the first flatmate
#         ?.set_font(family="Times", size=12)
#         ?.cell(w=100, h=25, txt=flatmate1.name, border=0)
#         ?.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)
#
#         # Insert name and due amount of the first flatmate
#         ?.cell(w=100, h=25, txt=flatmate2.name, border=0)
#         ?.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)
#
#         # Change directory to for_python_topic, generate and open the PDF
#         __.c.. "files"
#         ?.o.. f..
#         w__.o.. f..
#
#
# c_ FileSharer
#
#     ___  -    filepath, api_key="INSERT YOUR API KEY HERE"
#         ? = ?
#         ? = ?
#
#     ___ share _
#         client = C.. a..
#         new_filelink = ?.u.. filepath _ f..
#         r_ ?.u..