import pdfplumber

with pdfplumber.open("resume-sample.pdf") as pdf:
    for page in pdf.pages:
        print(pdf.pages)
        # print (page.extract_text())




