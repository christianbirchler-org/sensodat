# SensoDat: Simulation-based Sensor Dataset of Self-driving Cars
SensoDat is a dataset of self-driving car simulation data. Concretely, it contains:
- Simulation description
- Sensor data as time series

## Associated Paper Preprint
```{bibtex}
@article{sensodat-preprint,
  author       = {Christian Birchler and
                  Cyrill Rohrbach and
                  Timo Kehrer and
                  Sebastiano Panichella},
  title        = {SensoDat: Simulation-based Sensor Dataset of Self-driving Cars},
  journal      = {CoRR},
  volume       = {abs/2401.09808},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2401.09808},
  doi          = {10.48550/ARXIV.2401.09808},
  eprinttype    = {arXiv},
  eprint       = {2401.09808},
}
```

## Requirements
You need to have [Docker](https://docker.com) installed and running.

NOTE: The following instructions were tested with Windows and Linux with 32GB RAM.

## Automatic setup
To set up a MongoDB with the SDC simulation data, ensure `Docker` is up and running.
Then simply execute the `setup.sh` (Linux/MacOS) or `setup.bat` (Windows) script.

## Automatic clean up
To tear down the database simply execute the `cleanup.sh` (Linux/MacOS) or `cleanup.bat` (Windows) script.

## Manual setup
Run the following commands in the exact order to setup the database:

Start an `uploader` and a `mongo` container:
````
docker compose -f ./environment/docker-compose.yml up -d --build
````

Verify the containers are up and running:
````
docker ps
````

Copy the data to the `uploader` container:
````
docker cp ./data uploader:/app/data
````

Unzip the data in the `uploader` container:
````
docker exec uploader unzip ./data/data.zip -d ./data
````

Copy the code to upload the data to the `mongo` container:
````
docker cp ./code uploader:/app/code
````

Upload the data to the `mongo` container:
````
docker exec -it uploader python ./code/fill_mongodb.py
````

To tear down the database when you don't need it anymore:
````
docker compose -f ./environment/docker-compose.yml up down
````

