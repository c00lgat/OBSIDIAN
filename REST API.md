https://www.youtube.com/watch?v=faMdrSCVDzc
###### How are REST APIs Stateless?
Statefulness, Statelessness. 

A <mark style="background: #FF5582A6;">Stateful</mark> application API or webservice is considered Stateful if it stores data from the Client on its own servers.
For example, if a Client sends username and password to the Server for authentication purposes, and the Server stores that data; then the server is Stateful.
The Server is storing data from the Client. Thus it is a Stateful API/Webservice.


On the other hand, the REST architecture requires that the Client's state is not stored on the Server.
Instead, each request made by the Client must contain all necessary information for that particular HTTP method. And that is how REST API is <mark style="background: #BBFABBA6;">Stateless</mark>.

###### Explain the HTTP methods
RESTful web services will use HTTP methods and client requests.
Most common methods are:
- GET
	<mark style="background: #ABF7F7A6;">Fetches</mark> a resource from the Server 
- POST
	Requests for a resource to be <mark style="background: #ABF7F7A6;">created</mark> on the Server
- PUT
	 Requests for a resource to be <mark style="background: #ABF7F7A6;">updated</mark>
- DELETE
	Requests for a resource to be <mark style="background: #ABF7F7A6;">deleted</mark>  

These four methods correspond to *CRUD* operations.

###### Explain the HTTP status codes
RESTful API services use HTTP status codes in server responses. 

Most common types of status codes are 200 codes.

200 codes represent a successful request and response. 

400 codes represent a client-side error.

500 codes represent a server-side error.

###### What is a URI?
Stands for Uniform Resource Identifier.

Uniform Resource Identifiers identify every resource in the REST architecture. 

Two types or URI:
- URN: identifies a resource through a unique and persistent name like a book's ISBN.
- URL: typical web address. URLs will typically be used when designing web APIs.

###### What are best practices in making the URI for RESTful web-services?
URIs should mostly be standardized 