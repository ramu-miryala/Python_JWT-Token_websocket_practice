from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# In-memory storage
users = []
products = [
    {"id": 1, "name": "Smartphone XYZ", "price": 299.99},
    {"id": 2, "name": "Laptop Pro", "price": 999.99},
    {"id": 3, "name": "Smartphone ABC", "price": 199.99}
]

# Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Register API
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # Simple check to prevent duplicate registration
        if any(user['email'] == email for user in users):
            return "User already exists", 400

        users.append({"email": email, "password": password})
        return redirect(url_for('login'))

    return render_template('register.html')


# Login API
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = next((u for u in users if u['email'] == email and u['password'] == password), None)
        if user:
            return redirect(url_for('products_list'))

        return "Invalid credentials", 401

    return render_template('login.html')


# Products API
@app.route('/products', methods=['GET'])
def products_list():
    return jsonify({"products": products})


if __name__ == '__main__':
    app.run(debug=True)
