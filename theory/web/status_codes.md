# HTTP Response Codes

What are HTTP Status Codes?

HTTP status codes are three-digit responses from the server to the browser-side request.

HTTP status codes are split into 5 different categories. 
Each category represents a different kind of status.

## 1XX: Informational

A 1XX Informational status code is a temporary status code which means that the server has received the request and is continuing the process.

A 1XX status code is purely temporary and is given while the request processing continues.

### Informational Status Codes

1. 100 = Continue
1. 101 = Switching protocols
1. 102 = Processing request
1. 103 = Early Hints

## 2XX: Successful

A 2XX Successful status code means that the request was successful and the browser has received the expected information.

This means that the request was successful and has been received, processed, and responded to.

### Successful Status Codes

1. 200 = OK
1. 201 = Created
1. 202 = Accepted
1. 203 = Non-Authoritative Information
1. 204 = No Content
1. 205 = Reset Content
1. 206 = Partial Content
1. 207 = Multi Status
1. 208 = Already Reported
1. 226 = IM Used

## 3XX: Redirection

A 3XX Redirection status code means that you have been redirected and the completion of the request requires further action, not necessarily from your side.

### Redirection Status Codes

1. 300 = Multiple Choices
1. 301 = Moved Permanently (mostly on http sites)
1. 302 = Found
1. 303 = See Other
1. 304 = Not Modified
1. 305 = Use Proxy
1. 306 = Use Proxy
1. 307 = Temporary Redirect
1. 308 = Permanent Redirect

## 4XX: Client Error

A 4XX Client Error status code means that the website or the page could not be reached and either the page is unavailable or the request contains bad syntax.

### Client Error Status Codes

1. 400  Bad Request
1. 401 = Unauthorized
1. 402 = Payment Required
1. 403 = Forbidden
1. 404 = Not Found
1. 405 = Method Not Allowed
1. 406 = Not Acceptable
1. 407 = Proxy Authentication Required
1. 408 = Request Timeout
1. 409 = Conflict
1. 410 = Gone
1. 411 = Length Required
1. 412 = Precondition Failed
1. 413 = Payload Too Large
1. 414 = URI Too Long
1. 415 = Unsupported Media Type
1. 416 = Range Not Satisfiable
1. 417 = Expectation Failed
1. 418 = I'm a Teapot
1. 421 = Misdirected Request
1. 422 = Unprocessable Entity
1. 423 = Locked
1. 424 = Failed Dependency
1. 425 = Too Early
1. 426 = Upgrade Required
1. 428 = Precondition Required
1. 429 = Too Many Requests
1. 431 = Request Header Fields Too Large
1. 451 = Unavailable For Legal Reasons

## 5XX: Server Error

A 5XX Server error status code means that while the request might be valid, the server could not complete the request. These kinds of errors are mostly caused due to problems internally within the server.

### Server Error Status Codes

1. 500 = Internal Server Error
1. 501 = Not Implemented
1. 502 = Bad Gateway
1. 503 = Service Unavailable
1. 504 = Gateway Timeout
1. 505 = HTTP Version Not Supported
1. 506 = Variant Also Negotiates
1. 507 = Insufficient Storage
1. 508 = Loop Detected
1. 510 = Not Extended
1. 511 = Network Authentication Required

**THE END**
