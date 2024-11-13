from PyPDF2 import PdfReader, PdfWriter

# Define the input and output file paths
input_pdf_path = "corp.pdf"
output_pdf_path = "corp_split_pages_51_to_96.pdf"

# Open the input PDF file
reader = PdfReader(input_pdf_path)
writer = PdfWriter()

# Select pages 51 to 96 (Page 51 is at index 50, Page 96 is at index 95)
for page_num in range(50, 96):
    writer.add_page(reader.pages[page_num])

# Save the new PDF to the output file
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"PDF split from pages 51 to 96 saved as {output_pdf_path}")
