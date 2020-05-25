# Python Camera via. Docker on macOS, Ubuntu and Raspbian
In this folder you will find example code of using Python to access your camera.

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
* `demo-ui.py` - will open a window on your local computer showing you some video feed.