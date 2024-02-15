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
URIs should mostly be standardized when developing a RESTful webservice. 
This way, clients can more easily work with the web service. 

Five best practices when making RESTful URIs:
- Develop them with the understanding that forward slashes indicate hierarchy
- Plural nouns for branches 
- Use hyphens (-) for multiple words
- Use lowercase 
- Refrain from using file extensions


###### What are the differences between REST and SOAP?
REST is an architecture used to develop web services

SOAP stands for Simple Object Access Protocol, serves as a protocol for exchanging structured information.
While REST has flexible standards, SOAP standards are much more strict, their implementation and statefulness often means that the Client and Server are closer connected.  

REST allows data transfer in JSON, XML and other formats, SOAP only supports XML.

SOAP is stricter and more niche alternative to REST.

Used in cases where more regulated and staple data needs to be transferred. 


###### What are the differences between REST and AJAX
AJAX refers to Asynchronous Javascript and XML.

A collection of web technologies that allow for asynchronous web application using the built-in XML HTTP request object. 

REST API refers to an architecture for handling HTTP requests, AJAX refers to a collection of web technologies for making asynchronous web requests. 
Meaning, a REST API may handle AJAX clients and that AJAX may be used to send RESTful requests but, a REST API could not be implemented nor replaced by AJAX.


###### What are some tools used to develop and test REST APIs?
POSTMAN is used to ensure resources are being delivered and each facet of a REST API is performing as designed.

###### What are some real world examples of REST APIs?
REST APIs are used to manipulate data using the four main HTTP methods.

Operations like retrieving file data, accessing images and even hosting a website all require the use of REST APIs.

###### Advantages of REST APIs
- Easy to learn
- Wide range on data transfers like JSON and XML
- Statelessness, allowing for a simpler client experience 
- Scalability due to the independent nature of client and server

###### Disadvantages of REST APIs
- Lack of built-in security
- Need to be versioned for backwards compatibility when being updates
- Consistency in URIs difficult to maintain for complex projects 