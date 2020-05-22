# Python Camera via. Docker on macOS, Ubuntu and Raspbian

## Build
```bash
docker build -t python-test .
```

## Run
```bash
docker run --rm -it --device=/dev/video0 python-test
```
