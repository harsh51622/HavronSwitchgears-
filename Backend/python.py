from flask import Flask, request, redirect
from flask_cors import CORS
import csv, os

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    product = request.form.get('product')

    file_path = 'data.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Name', 'Phone', 'Email', 'Product'])
        writer.writerow([name, phone, email, product])

    # 👇 Alert + wapas same page
    return f"""
        <script>
            alert("Your enquiry is received. Our team will contact you shortly.");
              return redirect"{request.referrer}"
        </script>
    """

if __name__ == '__main__':
    app.run(debug=True)