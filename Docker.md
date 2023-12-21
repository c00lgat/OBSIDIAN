https://hub.docker.com/
https://www.youtube.com/watch?v=pTFZFxd4hOI


Allows us to run different versions of packages and development environments on the same machine. 

$ docker-compose up

Docker isolates containers. 
One app can use Node 9, and another can run Node 14 and they can run on the same machine at the same time.

Without docker, our machine could get cluttered and we could have too many tools that mess up other application behaviors.

Since docker isolates, deleting apps and packages wont be dangerous or wont influence other apps. 

Makes work quicker and more efficient.

---
Dockerfile is a plain text file that includes instructions that docker uses to package up an image. 
An image: cut-down OS, runtime environment, app files, libraries and environment variables.

We tell docker to start a container with that image. Our image is loaded into a container.

<mark>Docker hub is a storage for docker images.</mark>

No need to maintain long complex release documents. Package apps in containers and run it anywhere and everywhere. 

---

![[Pasted image 20231221222519.png]]
In order to run a docker container, we do so with the following command: 
`docker run hello-world`

But before that, we run the command `docker ps` in order to list any containers running on the Docker host. 
![[Pasted image 20231221222951.png]]
As the list shows, there are no containers currently running on the Docker host.

Running `docker images` will return all the docker images that are currently downloaded onto this Docker Host:
![[Pasted image 20231221223136.png]]
As we can see, we currently have one Docker image that is downloaded on the Docker Host, which is a container called `hello-world`.

Upon running the first command mentioned, `docker run hello-world`, Docker will return a message saying Unable to find image 'hello-world:latest' locally, meaning that it is not stored on our local host. Docker will then proceed to pull it from Docker Hub and run the container.
![[Pasted image 20231221223501.png]]

When we try to run `docker run [insert image name here]`