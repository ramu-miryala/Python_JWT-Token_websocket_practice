## Flask JWT Authentication Example

This project demonstrates how to implement JWT (JSON Web Token) authentication in a Flask application with support for access tokens, refresh tokens, and a protected route.

# Features

Login with basic username & password authentication

Issue Access Token (short-lived)

Issue Refresh Token (longer-lived)

Refresh expired access tokens using refresh tokens

Protect routes with a @token_required decorator

# Requirements

Python 3.8+

Flask

PyJWT

**Install dependencies:**

pip install flask pyjwt

 Project Structure
ACCESS_REFRESH_TOKEN/
│── Token.py          # Main Flask application
│── README.md       # Project documentation

# Running the Application

Run the app:

python Token.py


By default, the app will run at:

http://127.0.0.1:5000

# Endpoints
1️ Login

POST /login

Authenticate with username and password (admin / password).
Returns an access token (1 min validity) and a refresh token (1 hour validity).

Example (using curl):

curl -X POST -u admin:password http://127.0.0.1:5000/login


Response:

{
  "access_token": "<ACCESS_TOKEN>",
  "refresh_token": "<REFRESH_TOKEN>"
}

2️ Protected Route

GET /protected

Requires a valid access token in headers.

Headers:

x-access-token: <ACCESS_TOKEN>


Example:

curl -H "x-access-token: <ACCESS_TOKEN>" http://127.0.0.1:5000/protected


Response:

{
  "message": "You have accessed a protected route"
}

3️ Refresh Token

POST /refresh

Generates a new access token using the refresh token.

# Headers:

x-refresh-token: <REFRESH_TOKEN>


Example:

curl -X POST -H "x-refresh-token: <REFRESH_TOKEN>" http://127.0.0.1:5000/refresh


# Response:

{
  "access_token": "<NEW_ACCESS_TOKEN>"
}

 Config

Inside Token.py, the secrets are stored in:

app.config['SECRET_KEY'] = "Ramu"        # Access token secret
app.config['REFRESH_SECRET'] = "miriyala"  # Refresh token secret


For production, use strong secrets and load them from environment variables.

 Notes

Access token expires in 1 minute.

Refresh token expires in 1 hour.

If the refresh token also expires, you must log in again.

# Example Flow

Login → Get access_token & refresh_token.

Use access_token to call /protected.

If access_token expires → call /refresh with refresh_token to get a new one.

If refresh_token expires → login again.