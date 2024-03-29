https://www.youtube.com/watch?v=iYM2zFP3Zn0

###### HTTP is Stateless
Every request is completely independent.
Every time we reload the page, visiting another page etc., HTTP does not remember anything about the previous transaction. 
We can look at each request as a single transaction.
 
###### HTTPS: Hyper Text Transfer Protocol Secure
All data that is sent back and forth is encrypted via SSL.
Each time users are sending sensitive information, it should always be over HTTPS; things like credit card data, social security numbers etc. 

Nowadays, apps are enforcing HTTPS on every page, this can be done by installing an SSL certificate on the web host. 
There are different levels of certificates. 

###### HTTP Methods

*GET*
When we want to get or fetch data from the server. Could be just loading a standard HTML page, loading assets like CSS, images, JSON data, XML data and so on. 

*POST*
Usually used when we are posting data, adding something to the Server, adding a resource, typically when we submit a form like a Contact form as an example; we will be making a POST request if we are submitting a blog post, we will be using the POST method to send data to the Server and that data will be stored in a database somewhere.

*PUT*
Used to update data that is already on the Server. 
When we want to edit a post that we already posted, maybe change the image, change the text; that is usually done with a PUT request.

*DELETE*
Deletes data from the server.

###### HTTP Header Fields
Each request and response using HTTP contains a *Header* and a *Body*.

The body of the response is usually the HTML page that we are trying to load, the JSON data, whatever is being sent from the server.

The body of the request is for instance, when we submit a form, the form fields we are submitting are part of the request body. 

Both requests and responses have HTTP bodies.

Just like both Requests and Responses have bodies, they both also have Requests and Responses headers. 

There are three parts to each HTTP header, and there's also different fields on each part. 
![[Pasted image 20240216171527.png]]
HTTP headers will look something like the picture above. 
There is the method GET, being made to the specific path as in the picture, using the HTTP 1.1 protocol version.

Then we have all kinds of different header fields. There are the General fields such as:
- Request URL
- Request Method
- Status Code
- Remote Address
- Referrer Policy

Then we have Response fields:
- Server (nginx for example)
- Set-Cookie (used for servers to send small pieces of data from the server to the client)
- Content-Type (every response has a content type; for instance: 
	  - If its an HTML page, it'll have a content type of text/html
	  - CSS files would be text/CSS 
	  - Images would be image/png, image/jpeg 
	  - JSON data it will be application/JSON
- Content-Length (length, which is in octets- 8 bit bytes)
- Date

Requests fields:
- Cookies 
	  If we had a cookie previously sent by the server and we need to sent it back to the server, it would be done in this field.
- Accept-xxx 
	  Accepting coding, accept character set, accept language. Different encodings and languages the client is able to understand.
- Content Type
	  If we are sending data, JSON for example, we set it to application/JSON
- Content Length
- Authorization 
	  Since HTTP is stateless; so we might need to send some type of token within the authorization in the header so that we can for instance validate a user to access a protected route or protected page. (Unless sessions are being used on the server).
- User Agent
	  Typically a long string that has to do with the software that the user is using such as the operating system, the browser, and metadata like that
- Referrer
	  Has info regarding the referring site; typically when we click on a link and we get a pop-up that loads another website etc. 

###### HTTP Status Codes
*1xx: Informational*
It means the request has been received and the process is currently running. 

*2xx: Success*
Means that it was successful; successfully received, understood and accepted.

*3xx: Redirect*
Usually has to do with redirection or further action must be taken.

*4xx: Client Error*
The request doesn't have what it needs from the client. 
For example, let's say the server needs a name field sent in the request body that was not sent by the Client, the client will receive a 400 error.

*5xx: Server Error*
A Server error. The Server failed to fulfil an apparent valid request. 
Everything seems okay as far as what the Client sent to the Server but the Client still got an error. 
Something's wrong on the server side. 

>Important Status Codes:
*200 - OK*
*201 - OK created*. Also means everything passed through, but that something was created in the process. If we created a blog post and everything went okay, then we might get a 201 response. 
*301 - Moved to new URL*. Has to do with redirection.
*304 - Not modified (Cached version)*. Meaning that if we visited a page and it got cached, and it hasn't changed at all, then we get a 304 status.
*400 - Bad request*. If the Client is not sending the correct data to the Server.
*401 - Unauthorized*. If the Client is missing a token or something like that. 
*404 - Not found*. Not found; when the Client is looking for a page on the server that doesn't exist. 
*500 - Internal server error*. Could mean anything on the server side.

###### HTTP V2
- Responds with more data
- Reduce latency by enabling full request and response multiplexing
- Fast, efficient and secure
 ![[Pasted image 20240216180702.png]]


13:30

