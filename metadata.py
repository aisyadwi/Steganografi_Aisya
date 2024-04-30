from PyPDF2 import PdfReader

# Buka file PDF yang ingin Anda periksa metadata-nya
file_pdf = "jurnalku.pdf"

# Baca metadata dari file PDF
pdf = PdfReader(file_pdf)

# Tampilkan metadata
print("Metadata PDF:")
metadata = pdf.trailer["/Info"]
for key, value in metadata.items():
    print(f"{key}: {value}")