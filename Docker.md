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

