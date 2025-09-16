 ## Http Status codes
 
 ## 1xx – Informational
These codes are provisional responses, rarely used by most applications.

 100 Continue
•	When it occurs: The server informs the client to continue with the request.
•	Why it occurs: The client has sent headers and is waiting to send the body.
•	Examples:
1.	Client sends headers first and waits for the server to allow sending the body (e.g., large file upload).
2.	The Expect: 100-continue header was used by the client.

 101 Switching Protocols
•	When it occurs: Server switches to a different protocol as requested (e.g., WebSocket).
•	Why it occurs: The client requested a protocol upgrade.
•	Examples:
1.	Client requests upgrade to WebSocket via HTTP.
2.	Protocol version upgrade (e.g., HTTP/1.1 to HTTP/2).

 ## 2xx – Success
Indicates that the request was successfully received, understood, and accepted.

 200 OK
•	When it occurs: Successful GET or POST request.
•	Why it occurs: The resource was found and sent successfully.
•	Examples:
1.	Successful retrieval of a web page.
2.	Data successfully posted to an API.

 201 Created
•	When it occurs: A resource is successfully created (commonly POST).
•	Why it occurs: Server processed the creation request and created a new resource.
•	Examples:
1.	User successfully created via API (e.g., POST /users).
2.	New file successfully uploaded to cloud storage.

204 No Content
•	When it occurs: Request succeeded but no data is returned (commonly DELETE).
•	Why it occurs: No response body is needed.
•	Examples:
1.	Successful deletion of a resource.
2.	Update operation that doesn't return content.

3xx – Redirection
The client must take additional action to complete the request.

 301 Moved Permanently
•	When it occurs: Resource URL permanently changed.
•	Why it occurs: Resource now lives at a new URL.
•	Examples:
1.	Old domain redirects to new domain.
2.	Permanent change of API version (e.g., /v1 → /v2).

 302 Found (Temporary Redirect)
•	When it occurs: Temporary redirection to another URL.
•	Why it occurs: Server temporarily redirects due to maintenance or load balancing.
•	Examples:
1.	Redirect to a login page if not authenticated.
2.	Temporary redirect for A/B testing.


304 Not Modified
•	When it occurs: Client uses cached copy since resource has not changed.
•	Why it occurs: Server indicates no change in resource since last request.
•	Examples:
1.	Conditional GET using If-None-Match.
2.	Conditional GET using If-Modified-Since.

 ## 4xx – Client Errors
Indicates issues caused by the client.
 400 Bad Request
•	When it occurs: Malformed syntax or invalid parameters.
•	Why it occurs: Client sent an invalid or incomplete request.
•	Examples:
1.	Missing required field in JSON payload.
2.	Invalid query parameter (e.g., wrong data type).

401 Unauthorized
•	When it occurs: Missing or invalid authentication.
•	Why it occurs: Client failed to provide valid credentials.
•	Examples:
1.	Missing Authorization header in request.
2.	Invalid or expired access token.
403 Forbidden
•	When it occurs: Client is authenticated but not authorized.
•	Why it occurs: User doesn’t have permission for the requested resource.
•	Examples:
1.	Attempt to access admin-only endpoint as a normal user.
2.	IP is blocked by firewall rules.

 404 Not Found
•	When it occurs: Resource does not exist.
•	Why it occurs: URL is wrong or resource was deleted.
•	Examples:
1.	Typo in URL (e.g., /user/1234 when 1234 doesn’t exist).
2.	Resource deleted from the database.

 405 Method Not Allowed
•	When it occurs: HTTP method not supported.
•	Why it occurs: Trying to use POST where only GET is allowed.
•	Examples:
1.	Sending PUT to a read-only endpoint.
2.	Using DELETE where only GET is supported.

 409 Conflict
•	When it occurs: Request conflicts with the current state of the resource.
•	Why it occurs: Duplicate resource creation or version mismatch.
•	Examples:
1.	Trying to create a user that already exists.
2.	Updating a resource with an outdated version number.

 429 Too Many Requests
•	When it occurs: Client exceeds rate limits.
•	Why it occurs: Too many requests in a time window.
•	Examples:
1.	Hitting an API more than allowed per minute.
2.	Sending multiple login attempts in a short time.

## 5xx – Server Errors
The server failed to fulfill a valid request.


 500 Internal Server Error
•	When it occurs: Generic server error.
•	Why it occurs: Unexpected server exception.
•	Examples:
1.	Null reference exception in code.
2.	Database connection failure.

 502 Bad Gateway
•	When it occurs: Invalid response from upstream server.
•	Why it occurs: Proxy server gets a bad response from backend.
•	Examples:
1.	Backend server is down.
2.	Misconfigured reverse proxy.

 503 Service Unavailable
•	When it occurs: Server temporarily unavailable.
•	Why it occurs: Server overloaded or undergoing maintenance.
•	Examples:
1.	Database under maintenance.
2.	High traffic causing overload.

 504 Gateway Timeout
•	When it occurs: Upstream server did not respond in time.
•	Why it occurs: Long processing time or network issues.
•	Examples:
1.	Slow database query causes timeout.
2.	Backend API not responding.

