https://hub.docker.com/
https://www.youtube.com/watch?v=pTFZFxd4hOI


Allows us to run different versions of packages and development environments on the same machine. 

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
#### Docker Architecture
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

Upon running the first command mentioned, `docker run hello-world`, Docker will return a message saying Unable to find image `hello-world:latest'` locally, meaning that it is not stored on our local host. Docker will then proceed to pull it from Docker Hub and run the container.
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
The folders used on the host could themselves be network-based folders, for example, mounted remotely using NFS.

#### Volumes:
These are like bind mounts in that they are storage accessible to a container but they are managed by Docker. So the volume is created by Docker as required. They also exist outside the lifecycle of the container. They can remain when the container is removed. They can be moved between containers and even attached by multiple containers.
Though there is not file locking, meaning we have to be careful having multiple containers accessing the files at the same time. 

---
# Docker Container Networking
## Host Networking
Containers share the network of the host. When running a container this way, the Host port is the same port that the container application uses.
<mark style="background: #FF5582A6;">Downsides</mark>: take a containerized application that uses port TCP 1337 for example. Said application is running with the Host Networking configuration on port TCP 1337.
A user can access the application using the Host IP and the given port TCP 1337.  
However, if we attempt to run another Container on the same host, using the same Docker Image, using the same Networking mode; its going to fail. Because port TCP 1337 is already used on the Host.

<mark style="background: #BBFABBA6;">Upsides</mark>: Great if we want to run lots of different **Containers** on a Host, which use different ports.
The problem starts when we need to run multiple containers of the same Container.
So, if we needed to scale horizontally or run multiple versions of the same service for different clients. This problem is solved by using the Bridge Networking mode that is mentioned down below.
![[Pasted image 20240127173314.png]]

## Bridge Networking
With this network type, a Bridge Network is created separately and containers can be connected to this Bridge Network. Each container gets its own unique IP address on this network and because of this, each container can use the same port because its IP is unique on this Network.
![[Pasted image 20240127173430.png]]
In that configuration, each container can communicate with each other directly because they are on the same bridge network. By default, each container on the same Bridge Network can communicate. But, they cant be reached from outside of the Docker Host. 
In order to have them reached from outside of the Docker Host, we need to publish them. We need to publish a container port to a host port. We will often see it written as `Host Port: Container Port`.

For example: we can run container 1 using `-p 1337:1337` and this would publish container one port 1337 through to host port 1337 at which point it will be accessible by outside customers.
![[Pasted image 20240127173846.png]]

We can also publish container 2 but we cant use host port 1337 because its already used. Instead, we can use this option: `-p 1338:1337` and this would publish container port 1337 through to host port 1338. And then our customers can access this container. So, by using Bridge Networking and publishing containers, we are able to publish the same container to different Host Ports.

#### Key takeaways:
We don't get to choose the Port mappings because they aren't needed.
Whatever a Container uses for its application port, is used on the Host. 
No configuration is needed, but it limits us to one of each Container on one Host. 
But, we can run many different containers on the same Host as long as they use different ports. 

Bridge Networking enables us to overcome this limitation but we need to publish the port mappings for every Container. 
So map a Container port to a Host port for every single Container which uses the Bridge Networking mode.

We can define many Bridge Networks.
There are also other types of more complicated Networking.

---
# DEMO: Extending our container application using Environment Variables. 

https://github.com/acantril/docker-fundamentals/blob/main/docker-container-environment-variables/instructions.md

First, we run a phpMyAdmin container by running the following command:
`docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin`

`docker inspect [imageNameHere]` allows us to explore a certain image's metadata.
In an image's metadata we will find an `"Env"` variable. These are environment variables.
![[Pasted image 20240128152503.png]]

Environment variables are key value pairs. 
![[Pasted image 20240128152615.png]]
When setting environment variables, we use all caps for the environment variable names as seen above.

Using the `-e` option while running a container lets us initialize environment variables that will run in the container. Example:
`docker run --name db -e MYSQL_ROOT_PASSWORD=somewordpress -e MY_SQL_PASSWORD=wordpress -e MYSQL_DATABASE=wordpress -e MYSQL_USER=wordpress -d mariadb:10.6.4:focal --default-authentication-plugin=mysql_native_password`

These environment variables are passed to the container when the container is first ran.
The MySQL_ROOT_PASSWORD is responsible for the root user password, the MYSQL_PASSWORD is responsible for the user's password , the MYSQL_DATABASE variable being set up as `wordpress` will create an additional database, in this case, Wordpress.
MYSQL_USER=wordpress creates a new MariaDB user called wordpress.
`--default-authentication-plugin=mysql_native_password` a way of specifying another argument to the Docker container, so additional configuration information.

Once we run the container using the above `docker run` command, we run the `docker ps -a` command to make sure the container is up and running. 

Running `docker inspect [insert docker ID]` will return all the metadata for that specific container.
Once ran, we should look at the `"IPAddress"` variable under `"Networks"`. This IP is the internal IP that the MariaDB Container that we spun up is using. That IP is the IP that we will be using in order to access the MariaDB database server.

Now once the MariaDB container is running, we go ahead and type in `http://localhost:8081` into our internet browser. 
This will take us to the phpMyAdmin container image that is running as we ran it right before we ran the MariaDB container.
![[Pasted image 20240128154600.png]]
The page should look like this.

phpMyAdmin is a tool that let's us manage database instances. 
Now, by entering the MariaDB's IP that we retrieved after running the `docker inspect [MariaDB's containerID]` 
 And then, we move on to use the username and password that we had set using the variable environments.

Running the command `docker exec -it db bash` will allow us to go into the container via a bash shell.
Once in, we run `df -k` in order to list all of the drives and volumes that are mounted within this container. 
![[Pasted image 20240128160648.png]]
As we can see, the container uses no external drives and volumes and only uses ones that are within the container. Meaning, the storage is linked to the life cycle of the container. If the container is deleted, then so is the Storage.
This is important because if we go to `cd /var/lib/mysql`, and run `ls -la`, we will be able to see all the files that actually store the data of the MariaDB database engine. And all of this is stored within the Container.
If the container is deleted, then all of the data within the container is also deleted.

This is a limitation that can be overcome by configuring separate Storage for our Container using named volumes and bind mounts. 

> Anything inside the Container is Ephemeral.

The storage will not persist past the lifetime of the Container. 

Finally, we run `docker stop db` in order to stop the Database Container.
`docker rm db` in order to delete the Database Container. 
`docker stop phpmyadmin` in order to stop the phpMyAdmin container.
`docker rm phpmyadmin` in order to delete the phpMyAdmin container. 

---
# DEMO: Docker Bind Mounts & Volumes.

First off, we are going to spin up a `phpMyAdmin` Container, by running the following command:
```bash
docker run --name phpmyadmin -d -p 8081:80 -e PMA_ARBITRARY=1 phpmyadmin/phpmyadmin
```
The Container up above is going to allow us to interact with MariaDB database Container if needed.

 The following commands will only apply to Linux/MacOS systems as these commands will
 cause problems on Windows. 

The instructions are split into two different components: <mark style="background: #FFF3A3A6;">Bind Mounts</mark> and <mark style="background: #FFF3A3A6;">Named Volumes</mark>.

## <mark style="background: #ABF7F7A6;">Bind Mounts</mark>
Bind mounts allow us to map a file or directory on the Docker host onto a Container.
Useful when we need to access any files within a certain part of the Container from the Docker host or access a shared collection of files between Containers or between Containers and other compute services.

In this example, we are going to create a bind mount for the MariaDB data folder within the Container and map it to a folder on our Docker Host. 
This can be done through two different command line options:
- `-v`
- `--mount`

First off, we go ahead and create a folder in our Home folder: `mariadb_data`

In order to use Bind Mounts with Docker; the following command is ran (<mark style="background: #D2B3FFA6;">Linux/MacOS</mark>):
```bash
docker run \
--name db \
-e MYSQL_ROOT_PASSWORD=somewordpress \
-e MYSQL_PASSWORD=wordpress \
-e MYSQL_USER=wordpress \
--mount type=bind,source="$(pwd)"/mariadb_data,target=var/lib/mysql \
-d \
mariadb:10.6.4-focal \
--default-authentication-plugin=mysql_native_password
```
The `source="$(pwd)"/maria_db` section of the code is going to return the `maria_db` folder that is in the current working directory.

The `target=/var/lib/mysql` is the Container folder in which the data folder for MariaDB resides.

In order to check whether the command worked as intended or not, we change directory into the `/maria_db` folder that we have created and run the `la` command.
![[Pasted image 20240130173939.png]]As we can see, all the data within the `/var/lib/mysql` folder that exists on the container has now been mapped into the `/maria_db` folder on the Docker host. 

Any changes in the `/var/lib/mysql` folder is going to be reflected within the `/maria_db` folder on the Docker host; and any changes done to the `/maria_db` folder on the Docker host, will be reflected in the `/var/lib/mysql` folder in the Container.

Now, we will be illustrating the other format.
Run `docker stop db` and then `docker rm db` in order to get rid of the running Container. 

### Variation 2 of Binding Mounts:
Instead of using the `--mount` command option, the other alternative is using the `-v` command option. And it is used as follows:
```bash
docker run \
--name db \
-e MYSQL_ROOT_PASSWORD=somewordpress \
-e MYSQL_PASSWORD=wordpress \
-e MYSQL_USER=wordpress \
-v "$(pwd)"/mariadb_data:/var/lib/mysql \
-d \
mariadb:10.6.4-focal \
--default-authentication-plugin=mysql_native_password
```

The `-v` is a slightly different format. A shorter way than using the `--mount`. Both of them do the exact same thing.

## <mark style="background: #ABF7F7A6;">Named Volumes</mark>
Volumes are the preferred way of adding storage to Docker Containers outside the lifecycle of a Container. 
*Managed entirely by Docker*, and they work whether we are using Windows Container hosts or Linux Container hosts.
Instead of mapping a Container folder to a folder on the Docker host, we essentially create a Volume, or let Docker do that on our behalf; which is entirely managed end-to-end by Docker, and this Volume exists outside the lifecycle of the Container. If the Container is deleted, this Volume continues to exist.

In order to create a volume, we use the following command: 
```bash
docker volume create mariadb_data
```
This command will create a new Volume called `mariadb_data`.

Running the command `docker volume ls` will display all the Volumes.
We can display the Metadata of any Volume by running `docker volume inspect mariadb_data`:
![[Pasted image 20240130175247.png]]

A Volume can be deleted by running `docker volume rm mariadb_data`.


Volumes get created either explicitly; e.g. when we run a docker volume create command.
Or alternatively, when we specify to use a Volume on the `docker run` command on a Volume that does not already exist. Then the Volume gets created as part of that process.

---
# Docker Compose
Docker Compose is used to <mark style="background: #BBFABBA6;">Create</mark>, <mark style="background: #FFB86CA6;">Manage</mark> and <mark style="background: #FF5582A6;">Cleanup</mark> multi-container applications.
Docker Compose let's us manage applications which consist of multiple Containers and associated things like Volumes and networking.

The way a Docker Compose works is that it reads a `docker compose file` which is usually a file called `compose.yaml` and for legacy purposes: `docker-compose.yaml`.
Docker <mark style="background: #BBFABBA6;">Creates</mark>, <mark style="background: #FFB86CA6;">Updates</mark> or <mark style="background: #FF5582A6;">deletes</mark> resources based on the contents of that file.
Resources include Containers, Networking, Volumes and other things Docker provides.

Docker Compose starts with the `compose.yaml` file which defines what Docker should do.
Generally, to start with this file is provided via the Docker Client to Docker via the `docker compose up` command.
Based on this, the **Docker Daemon (dockerd)** begins to create, adjust or delete resources. This might include Volumes, Network and even Containers.
These Containers will require Container Images. These are often pulled from registries such as Docker Hub. 
The `compose.yaml` file also configures how Containers are presented: the Networking of Containers such as the networking between containers, and how the Containers are accessible from outside of the Docker Host. 
![[Pasted image 20240130185602.png]]

---
# DEMO: Using Docker Compose with our application
Usually, `docker compose` is part of a multi-step process.
First, we define each of our container images using a Docker file. 
We push those container images to a repository.
And then we define a Docker Compose file and then use that file using the `docker compose`command.
https://github.com/acantril/docker-fundamentals/blob/main/docker-compose/instructions.md
```yaml
services:
  db:
    image: mariadb:10.6.4-focal
    command: '--default-authentication-plugin=mysql_native_password'
    volumes:
      - mariadb_data:/var/lib/mysql
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=somewordpress
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
    expose:
      - 3306
      - 33060
  wordpress:
    image: wordpress:latest
    volumes:
      - wordpress_data:/var/www/html
    ports:
      - 8081:80
    restart: always
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=wordpress
      - WORDPRESS_DB_NAME=wordpress
volumes:
  mariadb_data:
  wordpress_data:
```

> YAML files can't have tabs inside them. Convert tabs to spaces.

Now, the code listed above is the Docker Compose file.

Under `services`, two containers are defined:
###### `db` container: the database part is defined within this container.
We can see that the `mariadb_data` volume is mapped inside the container to the `/var/lib/mysql` folder inside the container.

###### `wordpress` container: the application part is defined within this container. 
We can see that the `wordpress_data` volume is mapped inside this container to the `/var/www/html` folder inside the Container. 


This is a multi container deployment of Wordpress. It requires the application part and the database part. 

The Docker compose file also defined two named volumes: `mariadb_data` and `wordpress_data`.

What we will be doing now is saving the YAML file as `compose.yaml`. Go to the folder where the Docker compose file was saved and run the following command: 
`docker compose up -d`. If nothing else is defined in the command, Docker is going to look for that Docker Compose file using one of its default valid names. `compose.yaml` is one of those names. 

The `up` option is going to tell Docker Compose to bring up the things defined in that file. Will have the effect of running containers and creating any named volumes.

The `-d` option is going to detach the command from the terminal, running it in the background.

Running the `docker ps` command is going to show us a list of the Containers that are currently running: ![[Pasted image 20240130233305.png]]

Running the `docker volume ls` command is going to show us the volumes that we have created:
![[Pasted image 20240130233343.png]]

Once all of that is done, we go to `http://localhost:8081/` and see that the Wordpress application is up and running.
Proceed with the registration, save the password and then login as admin into the Wordpress application that is running.

After that, we try to publish a post containing cat images. 

On the Wordpress Container, the actual images were stored. Whereas on the Database Container, the metadata and information about the post were stored.

Now, we are going to demonstrate how the data that we have stored in both of the Containers can live on past the lifecycle of the Containers.
We are going to be doing that using the *Multi Container Management* functionality provided by Docker Compose. 

Running `docker ps` command is going to show us the two containers that we are running: 
![[Pasted image 20240130234239.png]]

Now, while still being in the same folder as the `compose.yaml` file, we are going to go ahead and run the following command:
`docker compose down`
That is going to stop and remove any of the containers defined within the `composed.yaml` file. Its going to remove the MariaDB container and the Wordpress container. 

Running the `docker ps` command once again is going to show us that there are currently no running containers:
![[Pasted image 20240130234442.png]]

Running `docker ps -a` is going to show us that there are currently no stopped containers, either:
![[Pasted image 20240130234528.png]]
These have been completely removed.

However, running the `docker volume ls` command is going to show us that the volumes we have previously created were not deleted:
![[Pasted image 20240130234701.png]]
These volumes are actually storing the Wordpress data and the data from MariaDB.

Now, we can set up new containers that use these two Volumes and we should be able to see the post that we had created in the previous two containers.

Running `docker compose up -d` is going to recreate both the Wordpress Container and the Database Container. Docker will utilize the existing named volumes. 

Once the command finishes running, we can go back to the `http://localhostL:8081/` page, refresh, and we should be able to see the existing post we created previously with no problems.

This is all possible because we used named Volumes, which persist past the lifetime of the existing containers. 

Running `docker compose down` will remove the containers and the networking for the containers.

We will have to remove the Volumes manually. 
Running `docker volume ls` will return the names of the volumes.
![[Pasted image 20240131100127.png]]

Running `docker volume rm [volume_name]` will remove the Volume.

Run `docker ps -a` to make sure there are no running/stopped containers. 

Run `docker volume ls` to make sure the Volumes we created have been deleted. 

---
# Container Registry
Container registries are like GitHub but for Docker images. 

Docker Hub is an example of a registry. 
Private registries are a thing (cloud or on-premises).

Registries are split into repositories just like GitHub: You can `docker pull` from or `docker push` to repositories.
`docker pull` will pull images from the repository to the local Docker host. 
`docker push` will push images from the Docker Host to the registry of our choosing. 

To use Docker Hub, we will need a username, repository name and a tag: e.g. `acantril/containerofcats:latest`

---
https://www.youtube.com/watch?v=SXwC9fSwct8
# Docker Compose
To have different containers that are running different services and applications within them, and need to talk to each other
When we have containers at hand that need to:
- Deployed and run together
- The services need to communicate
A tool to define and run multiple services and application that belong together in one environment.


`docker network create mongo-network`
Creates a docker network

```bash
docker run -d \ 
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=supersecret \
--network mongo-network \
--name mongodb \
mongo # IMAGE
```
Creates docker container,  detaches it from the terminal, maps it out to port 27017 and gives it two environment variables: `MONGO_INITDB_ROOT_USERNAME` and `MONGO_INITDB_ROOT_PASSWORD`.
It also attaches it to the network that we have created, `mongo-network`, gives it `mongodb` name and `mongo` being the image on which the container is based on.

`docker ps` shows us the currently running container(s).


We run another Docker container, mongo-express, which is the UI that communicates with MongoDB.
```bash
docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=supersecret \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--network mongo-network \
--name mongo-express \
mongo-express # IMAGE
```

`docker ps` should once again show us the currently running containers:
![[Pasted image 20240311124548.png]]

In order to check whether Mongo-express has connected properly to our MongoDB database, we log into http://localhost:8081 and log in using the credentials we have entered as environment variables. 

Running `docker logs [containerID]` shows us the container logs. 
![[Pasted image 20240311124743.png]]

In this demo, we demonstrated running two containers that are co-dependent using the normal, plain Docker run command. 

In a microservice application, where the scale of containers that have to communicate is much bigger, it becomes clear pretty quick that using the plain Docker commands to run them all in the same manner that we have just done is not efficient at all. 

Not only that, but if we wanted to stop containers or re-run them, it can get very manual and tedious to do.

Docker compose helps us create containers that are dependent on each other as a single unit.
`docker-compose` is a YAML file that configures and maintains the application's services.
With a single command, we can create and start all the services from our configuration.

![[Pasted image 20240311125329.png]]

What we can do is, copy the script that we used to run the container and paste it into the `docker-compose` file. The `docker-compose` file is *more structured*, abstracts away the low-level commands and provides a higher-level, more human-readable configuration format.

 First two lines are the required attributes of Docker compose file. 
 First line defines the version of Docker compose which is the latest version which should be compatible with the locally installed Docker compose. 
 
```YAML
version: '3.1'
services:
	mongodb: # container-name
		image: mongo
		ports:
			- 27017:27017 # HOST:CONTAINER
		environment:
			- MONGO_INITDB_ROOT_USERNAME=admin
			- MONGO_INITDB_ROOT_PASSWORD=secret
	mongo-express: # container-name
		image: mongo-express
		ports:
			- 8081:8081
		environment:
			- ME_CONFIG_MONGODB_ADMINUSERNAME=admin
			- ME_CONFIG_MONGODB_ADMINPASSWORD=password
			- ME_CONFIG_MONGODB_SERVER=mongodb
```

So basically, Docker Compose is just a structured way to contain normal common commands, and it is easier to edit the file if we wanted to change some variables.
- Helps structure our commands
- Simplifies container management
- Easier to make changes, and see current configuration
- Declarative approach: defining the desired state

