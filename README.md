# TD7A4
TD Goal: 

Practice volumes. The DB mongo is linked to a volume which allows me to not do manual manipulations each 
time I recreate the container.

Steps to follow :

First you have to create the image of the flask application from the docker file with the following command: 

```
docker build -t flask .
```
(note: do not change the name of the image (flask) because it is used in the docker compose)

Then create your containers with the docker compose : 
```
docker-compose up
```
(note: they are in the default network)


Currently the db and collections used by flask do not exist. You have to  create it and add an information to display
(note: this code is rudimentary and is not intended to be to be pretty. The goal is just to test the volumes so there
is no template and the display is rustic).
```
docker exec -it mongo-container bash mongosh 
```


```
use flask_db
```
 

```
db.collection.insertOne({message: " Your message"})
```

Now if you destroy your container and recreate it with the same volume you won't have to add your message manually.