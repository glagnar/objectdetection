# Python Camera and TPU via. Docker on macOS, Ubuntu and Raspbian

## Build
```bash
docker build -t tpu-test .
```

## Run
```bash
docker run --rm -it --privileged -v /dev/bus/usb:/dev/bus/usb tpu-test
```

### Contents
* `main.pu` - analyse camara feed, and output if and where a person is located in the image 