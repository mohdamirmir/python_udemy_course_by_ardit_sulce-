from fpdf import FPDF 

pdf = FPDF(orientation="P",unit="mm",format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)

pdf.cell(w=0, h=12, txt="Hello World", align="C", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi  There", align="C", ln=1, border=1)


pdf.add_page()

pdf.cell(w=0, h=12, txt="Hello World", align="C", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi  There", align="C", ln=1, border=1)




pdf.output("./Day_21_pdf_generator/output.pdf")
