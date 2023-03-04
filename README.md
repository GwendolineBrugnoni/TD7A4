# TD7A4
Steps to follow :

docker build -t flask .

docker-compose up

docker exec -it mongo-container bash mongosh 

use flask_db 

db.collection.insertOne({message: "coucou :p "})
