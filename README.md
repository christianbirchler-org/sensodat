# SensoDat: Simulation-based Sensor Dataset of Self-driving Cars
Latest Release on Zendodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12600225.svg)](https://doi.org/10.5281/zenodo.12600225)

Original Paper Artifact: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10307479.svg)](https://doi.org/10.5281/zenodo.10307479)

SensoDat is a dataset of self-driving car simulation data (**30K executed simulations**). Concretely, it contains:
- Simulation description data in [ASAM OpenDRIVE](https://www.asam.net/standards/detail/opendrive/) format
- Sensor data as time series of 81 sensors/properties

## Associated Paper
```{bibtex}
@inproceedings{sensodat,
  author       = {Christian Birchler and
                  Cyrill Rohrbach and
                  Timo Kehrer and
                  Sebastiano Panichella},
  title        = {SensoDat: Simulation-based Sensor Dataset of Self-driving Cars},
  booktitle    = {21th {IEEE/ACM} International Conference on Mining Software Repositories,
                  {MSR} 2024, Lisbon, Portugal, April 15-16, 2024},
  year         = {2024},
  doi          = {to appear},
}

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

## License
```{text}
    SensoDat: Simulation-based Sensor Dataset of Self-driving Cars
    Copyright (C) 2024  Christian Birchler

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
