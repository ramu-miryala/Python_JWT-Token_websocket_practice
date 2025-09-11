from flask import Flask, request, render_template

app = Flask(__name__)

# GET: Show form
@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

# POST: Handle form data
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    qualification = request.form['qualification']
    location = request.form['location']

    return f"""
    <h2>Form Submitted Successfully!</h2>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Qualification:</strong> {qualification}</p>
    <p><strong>Location:</strong> {location}</p>
    <a href="/">Back to form</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
