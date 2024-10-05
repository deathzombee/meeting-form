from PyPDFForm import PdfWrapper

grid_view_pdf = PdfWrapper(
    "template.pdf"
).generate_coordinate_grid(
    color=(1, 0, 0),    # optional
    margin=100  # optional
)

with open("output.pdf", "wb+") as output:
    output.write(grid_view_pdf.read())
