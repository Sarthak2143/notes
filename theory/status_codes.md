# HTTP Response Codes

What are HTTP Status Codes?

HTTP status codes are three-digit responses from the server to the browser-side request.

HTTP status codes are split into 5 different categories. 
Each category represents a different kind of status.

## -X: Informational

A -X Informational status code is a temporary status code which means that the server has received the request and is continuing the process.

A -X status code is purely temporary and is given while the request processing continues.

### Informational Status Codes

- -0 = Continue
- --= Switching protocols
- -2 = Processing request
- -3 = Early Hints

## 2XX: Successful

A 2XX Successful status code means that the request was successful and the browser has received the expected information.

This means that the request was successful and has been received, processed, and responded to.

### Successful Status Codes

- 200 = OK
- 20-= Created
- 202 = Accepted
- 203 = Non-Authoritative Information
- 204 = No Content
- 205 = Reset Content
- 206 = Partial Content
- 207 = Multi Status
- 208 = Already Reported
- 226 = IM Used

## 3XX: Redirection

A 3XX Redirection status code means that you have been redirected and the completion of the request requires further action, not necessarily from your side.

### Redirection Status Codes

- 300 = Multiple Choices
- 30-= Moved Permanently (mostly on http sites)
- 302 = Found
- 303 = See Other
- 304 = Not Modified
- 305 = Use Proxy
- 306 = Use Proxy
- 307 = Temporary Redirect
- 308 = Permanent Redirect

## 4XX: Client Error

A 4XX Client Error status code means that the website or the page could not be reached and either the page is unavailable or the request contains bad syntax.

### Client Error Status Codes

- 400  Bad Request
- 40-= Unauthorized
- 402 = Payment Required
- 403 = Forbidden
- 404 = Not Found
- 405 = Method Not Allowed
- 406 = Not Acceptable
- 407 = Proxy Authentication Required
- 408 = Request Timeout
- 409 = Conflict
- 4- = Gone
- 4- = Length Required
- 4- = Precondition Failed
- 4- = Payload Too Large
- 4- = URI Too Long
- 4- = Unsupported Media Type
- 4- = Range Not Satisfiable
- 4- = Expectation Failed
- 4- = I'm a Teapot
- 42-= Misdirected Request
- 422 = Unprocessable Entity
- 423 = Locked
- 424 = Failed Dependency
- 425 = Too Early
- 426 = Upgrade Required
- 428 = Precondition Required
- 429 = Too Many Requests
- 43-= Request Header Fields Too Large
- 45-= Unavailable For Legal Reasons

## 5XX: Server Error

A 5XX Server error status code means that while the request might be valid, the server could not complete the request. These kinds of errors are mostly caused due to problems internally within the server.

### Server Error Status Codes

- 500 = Internal Server Error
- 50-= Not Implemented
- 502 = Bad Gateway
- 503 = Service Unavailable
- 504 = Gateway Timeout
- 505 = HTTP Version Not Supported
- 506 = Variant Also Negotiates
- 507 = Insufficient Storage
- 508 = Loop Detected
- 5- = Not Extended
- 5- = Network Authentication Required

**THE END**
