from PyPDF2 import PdfEtiter
merger = PdfWriter()
pdfs = []
n = int(input("How many pdfs you want to merge?"))
for i in range(0, n):
  name = input(f"Enter the name of your pdf{i+1}:\n")
  pdfs.append(name)

for pdf in pdfs:
  merger.append(pdf)
merger.Write("Merged-pdf.pdf")
merger.close()
