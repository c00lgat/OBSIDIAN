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

Just like both Request 
