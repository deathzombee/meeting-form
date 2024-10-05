import json

from PyPDFForm import PdfWrapper

pdf_form_schema = PdfWrapper("template.pdf").schema

print(json.dumps(pdf_form_schema, indent=4, sort_keys=True))

