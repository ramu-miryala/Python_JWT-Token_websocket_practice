## Code Explanation

# Storage

users = [] → In-memory list to store registered users (gets cleared if server restarts).

product s = [...] → Predefined product list with id, name, price.

# Routes

/ → Home page (renders home.html).

/register

GET → shows registration form.

POST → registers new user if email doesn’t already exist, then redirects to /login.

/login

GET → shows login form.

POST → verifies credentials → if valid, redirects to /products, else returns Invalid credentials.

/products

GET → returns products in JSON format.

# Templates

You’ll need home.html, register.html, login.html inside a templates/ folder.

# Example:

<!-- templates/register.html -->
<form method="POST">
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Register</button>
</form>


# Flask Run

Run the app:

python app.py


Visit:

http://127.0.0.1:5000/ → Home

http://127.0.0.1:5000/register → Registration

http://127.0.0.1:5000/login → Login

http://127.0.0.1:5000/products → Products JSON

