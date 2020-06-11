# Python Camera via. Docker on macOS, Ubuntu and Raspbian

[![Twitter: @thomasbjgilbert](https://img.shields.io/badge/contact-@thomasbjgilbert-blue.svg?style=flat)](https://twitter.com/thomasbjgilbert)
[![Language: Python](https://img.shields.io/badge/lang-Python-yellow.svg?style=flat)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat)](http://opensource.org/licenses/MIT)

This project will demonstrate how to use Python to access the videofeed from your camera, while still supporting Docker.

## Build
```bash
docker build -t python-test .
```

## Run
```bash
docker run --rm -it --device=/dev/video0 python-test
```

### Contents
* `main.pu` - will iterate over all your camera devices until there are none left. 
* `demo-ui.py` - will open a window on your local computer showing you some video feed. Note this cannot run in Docker
* `demo-tpu.py`- will try to load the tensorflow libraries in python, and exit when done.