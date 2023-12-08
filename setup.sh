#!/bin/bash
docker compose -f ./environment/docker-compose.yml up -d --build
docker cp ./data uploader:/app/data
docker exec uploader unzip ./data/data.zip -d ./data
docker cp ./code uploader:/app/code
docker exec -it uploader python ./code/fill_mongodb.py
