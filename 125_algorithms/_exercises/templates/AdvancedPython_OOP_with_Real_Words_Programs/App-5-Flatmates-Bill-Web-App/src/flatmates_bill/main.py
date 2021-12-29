____ flatmates_bill.flat _____ Bill, Flatmate
____ flatmates_bill.reports _____ PdfReport, FileSharer

amount  f__(i__("Hey user, enter the bill amount: "))
period  i__("What is the bill period? E.g. December 2020: ")

name1  i__("What is your name? ")
days_in_house1  i..(i__(f"How many days did {name1} stay in the house during the bill period? "))

name2  i__("What is the name of the other flatmate? ")
days_in_house2  i..(i__(f"How many days did {name2} stay in the house during the bill period? "))


the_bill  Bill(amount, period)
flatmate1  Flatmate(name1, days_in_house1)
flatmate2  Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report  PdfReport(filenamef"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer  FileSharer(filepathpdf_report.filename)
print(file_sharer.share())