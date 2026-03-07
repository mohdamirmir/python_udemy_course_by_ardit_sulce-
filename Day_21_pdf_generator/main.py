from fpdf import FPDF 

pdf = FPDF(orientation="P",unit="mm",format="A4")

print(type(pdf))

pdf.add_page()

pdf.output("output.pdf")