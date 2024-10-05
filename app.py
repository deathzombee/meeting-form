from flask import Flask, request, render_template, send_file
from PyPDFForm import PdfWrapper
import io

app = Flask(__name__)

# Route to display the form for user input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data from the user
        form_data = request.form.to_dict()

        # Fill the PDF with the collected data
        filled_pdf = fill_pdf(form_data)

        # Send the filled PDF back to the user as a download
        return send_file(filled_pdf, as_attachment=True, download_name="filled_out.pdf")

    return render_template('pdf_form.html')

# Function to fill the PDF with data
def fill_pdf(data):
    # Fill the PDF using PyPDFForm
    filled = PdfWrapper("template.pdf").fill(data)

    # Create a BytesIO stream to hold the filled PDF in memory
    filled_pdf_stream = io.BytesIO()
    filled_pdf_stream.write(filled.read())
    filled_pdf_stream.seek(0)

    return filled_pdf_stream

if __name__ == '__main__':
    app.run(debug=True)

