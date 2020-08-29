from urllib import response

from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/<name>/<location>/<phone>/<highqual>/<ten>/<twelve>') #http://127.0.0.1:5000/Priyank/Delhi
def pdf_template(name, location, phone, highqual, ten, twelve):

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    rendered = render_template('pdf_template.html', name=name, location=location, phone=phone, highqual=highqual, ten=ten, twelve=twelve)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline;  filename=output.pdf' #attachment

    return response

if __name__ == '__main__':
    app.run(debug=True)