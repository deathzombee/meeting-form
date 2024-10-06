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

        # Set default values for fields that are not provided
        form_data = set_default_values(form_data)

        # Remove any '\r' characters from the meeting notes
        if 'Meeting notes' in form_data:
            form_data['Meeting notes'] = form_data['Meeting notes'].replace('\r', '')

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

# Function to set default values for missing form fields
def set_default_values(data):
    # Check if required fields are empty or missing, and set default values
    defaults = {
        'Title': 'Group 2',
        'Date': '', #todays date
        'Time': '', # time.now
        'Location': 'discord',
        'Purpose': 'Progress',
        'Recorded by': 'Lisa Miao',
        'Attendees': 'Gabriel Calderon',
        'Attendees 1': 'Lisa Miao',
        'Attendees 2': 'Peter Vang',
        'Agenda': '',
        'Meeting notes': '',
        'Task': '',
        'Owner': '',
        'Due': '' # the next monday
    }

    # Loop through the defaults and apply them to the form data
    for key, value in defaults.items():
        if not data.get(key):  # If field is missing or empty
            data[key] = value

    return data

if __name__ == '__main__':
    app.run(debug=True)

