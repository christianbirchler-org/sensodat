# SensoDat: Simulation-based Sensor Dataset of Self-driving Cars
Developing tools in the context of autonomous systems, such as self-driving cars (SDCs), is time-consuming and costly since researchers and practitioners rely on expensive computing hardware and simulation software.
We propose SensoDat, a dataset of 32,580 executed simulation-based SDC test cases generated with state-of-the-art test generators for SDCs.
The dataset consists of trajectory logs and a variety of sensor data from the SDCs (e.g., rpm, wheel speed, brake thermals, transmission, etc.) represented as a time series.
In total, SensoDat provides data from 81 different simulated sensors.
Future research in the domain of SDCs does not necessarily depend on executing expensive test cases when using SensoDat.
Furthermore, with the high amount and variety of sensor data, we think SensoDat can contribute to research, particularly for AI development, regression testing techniques for simulation-based SDC testing, flakiness in simulation, etc.

- Link to original paper: https://doi.org/10.1145/3643991.3644891

## Quick Start (Recommended)
1. Set up a MongoDB instance (see [MongoDB Community Edition](https://www.mongodb.com/products/self-managed/community-edition))
2. Import the SensoDat `mongorestore -d sensodat mongodump/sensodat`

## Documentation
Please refer to the paper publication for the general overview of the dataset.
A condensed version of it you find here: [DOCUMENTATION.md](./DOCUMENTATION.md)

## Examples
Please look at some examples in the `examples/` directory.
There you can get some inspiration how to connect to the MongoDB and doing some simple queries on SensoDat.

## Links
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

