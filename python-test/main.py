import tensorflow as tf
import cv2
import numpy

def main():
    print('Program Starting')
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_V4L)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    print(arr)

if __name__ == '__main__':
    main()