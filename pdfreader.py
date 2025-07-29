import pdfplumber

with pdfplumber.open("hotels-pdf.pdf") as pdf:
    for page in pdf.pages:
        # print(page)
        print (page.extract_text())
