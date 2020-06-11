import cv2
import numpy

def main():
    print('Program Starting - please ignore errors as we are just testing all possible ports')
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    print('Cameras were found at slots:')
    print(arr)

if __name__ == '__main__':
    main()
