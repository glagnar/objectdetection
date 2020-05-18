# Testing USB Camera from Docker

## Docker build
```bash
docker build -t usbcam-test .
```

## Docker run
```bash
docker run --rm -it --privileged -v $PWD/motion.conf:/etc/motion/motion.conf  -v /dev/video0:/dev/video0 -v $PWD/output:/var/lib/motion -p 8080:8080 -p 8081:8081 usbcam-test motion -n
```
