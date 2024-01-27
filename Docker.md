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

---
#### \[DEMO] Interacting with Docker Engine
https://learn.cantrill.io/courses/docker-fundamentals/lectures/44706186
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

When we try to run `docker run [insert image name here]` and had no copy of the relevant image, then Docker will pull that image automatically for us.

If we run the command `docker ps` after running the `hello-world` docker container, we see that there are currently no containers running. 
![[Pasted image 20231221224046.png]]
And that is because all the container did was output the text shown above and then stopped.

Running the command `docker ps -a` will show any containers which were previously running. 
![[Pasted image 20231221224233.png]]

---
#### Container and Image Architecture
https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151202

Docker images are <mark style="background: #FFB86CA6;">read only immutable</mark> templates
If we do change the images, we are actually making a new image.

Container images are used to run containers, and containers need storage.

When we run a container image, what actually happens is a writable layer is added.
![[Pasted image 20231221225114.png]]

Images are a collection of independent file system layers.
![[Pasted image 20231221225444.png]]

---
#### \[DEMO] Working with existing docker images
https://learn.cantrill.io/courses/docker-fundamentals/lectures/44151206

We can either access docker images by going to the docker hub website, find the image we need, copy the `docker pull` (`docker pull acantril/containerofcats`) command, pull the image into our local machine and then run the `docker run` command (`docker run -p 8081:80 acantril/containerofcats)`.
Alternatively, we can simply run the `docker run` command without previously pulling the image own to our local machine. If we run an image that does not exist locally on our local machine, Docker is going to attempt to pull that image down from the registry. 

Running the `docker run -p 8081:80 acantril/containerofcats` command without the `-d` option, the container image is not going to load once we close our terminal session.
And so, by using the `-d` command as the following; we will successfully run the container image without having it attached to the terminal session and thus terminating the terminal session will not affect the container image that is running: `docker run -p 8081:80 -d acantril/containerofcats`.
Usually, when we want to run containers, we will want to detach them so that we won't have to keep the terminal open.

If we wanted to know the port being used for a container, we can run the command `docker port faf82ca79d4a` where `faf82ca79d4a` is the container ID.
![[Pasted image 20240124192847.png]]
On the left, we have the port that is used within the running container. On the right we can see how its mapped onto the Docker host. Its mapped onto any IP on the Docker host and then port 8081.
Since the container is running, we can run commands within the container.

`docker exec -it [containerID]`
The above command will run commands inside the running container. 
For example:
`docker exec it [containerID] ps` will list all of the processes running inside the container. 

---
# Docker Container Storage

A container is comprised of a number of File System Layers bunched up together. In this example, a container made up of three layers is shown. Conceptually, they are represented as a single file system.  
When a container is ran, a writeable layer is added on top of the read-only layer (that makes up the container image). The added writeable layer uses the <mark style="background: #FFB86CA6;">Union</mark> File System.
The Union File System allows files and directories from different file systems to be overlaid into one conceptual single file system.

The writeable layer is what makes every container it's own unique thing.  

This architecture requires a <mark style="background: #BBFABBA6;">File System Driver</mark>. This has overhead and <mark style="background: #FF5582A6;">impacts</mark> performance.  

Layers from the docker image can be read from but any writes go into the writable layer. And the container sees both of the writeable layer and the original layers as _one filesystem_.  

The writable layer in Containers is not something which can be migrated around so any data written is conceptually, part of that one single container.  

### Storage options:
`tmpfs`: is a file system which is accessible to a specific container, which uses the memory in the Docker Host. Simply put, fast, in memory storage that is not persistent since its not being stored on disk. It also cant be shared by containers.
Should only be used for temporary storage. For example, files that we do not need to be stored on disk such as sensitive files that should not be stored on disk for any length of time, data that we are holding for a short time while processing or accessing.
![[Pasted image 20240127164511.png]]

`Bind mounts`: we also can mount folders onto containers. 
Bind Mound map host (or remote) folders to a container folder.
One host folder can be accessed by multiple containers at the same time. 
Good type of storage for shared data which is stored on the host. 
One downside is that Bind mounts rely on a *host folder structure* and is not managed by Docker. This can <mark style="background: #FF5582A6;">reduce portability</mark>.
