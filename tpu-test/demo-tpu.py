import argparse
from edgetpu.detection.engine import DetectionEngine
import PIL
import socket
import base64
from io import BytesIO
import cv2

import time 
from collections import deque
time_queue = deque([])

UDP_IP = socket.gethostname()
UDP_PORT_IMG = 5005
UDP_PORT_PRED = 5006
sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM) 

width, height = 640,480

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='Path of the detection model.', required=True)
    parser.add_argument('--socket_pred', default = "True", help='Bool: Whether to send prediction over socket.', required=False)
    parser.add_argument('--socket_img', default = "True", help='Bool: Whether to send image over socket.', required=False)
    
    args = parser.parse_args()    

    engine = DetectionEngine(args.model)
    socket_pred = str2bool(args.socket_pred)
    socket_img = str2bool(args.socket_img)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    print("Camera started. Streaming results")    
    
    while(cap.isOpened()):
        print("Running")
        _, frame = cap.read()
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(im)

        # draw = PIL.ImageDraw.Draw(input_buf)

        ans = engine.detect_with_image(img, threshold = 0.35, keep_aspect_ratio = True, relative_coord= False, top_k = 1) 
        
        pred = "nopeople"
 
        if ans:
            for obj in ans:
                if (obj.label_id==0):
                    box = obj.bounding_box.flatten().tolist()
                    #draw.rectangle(box, outline='red')
                    #if socket_img:
                    #    drawBoundingBox(img, draw, box, 4)

                    pos =  ((box[0]+box[2])/width) - 1
                    pred = '{:.3f}'.format(pos)
                    print(pos)
        
        print(pos)
        print(pred)
        #if socket_pred:
            #sendMsgUDP(pred)
        #if socket_img:
        #    sendImgUDP(img)
      
        time_queue.append(time.time()) 
        if len(time_queue) > 5:
            time_queue.popleft()
         
        if len(time_queue) > 1:
           print("FPS: ", len(time_queue)/(time_queue[-1]-time_queue[0]))   
 
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def drawBoundingBox(img, draw, box, thickness):
    for i in range(thickness):
        draw.rectangle(box, outline='red')
        box[0] += 1
        box[1] -= 1
        box[2] += 1
        box[3] -= 1

def sendMsgUDP(msg):
    MESSAGE=msg.encode('utf-8')
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_PRED))

def sendImgUDP(img):
    #if width*height > 64000:
    img = img.resize([160, 120],Image.ANTIALIAS)
    buff = BytesIO()
    img.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    sock.sendto(img_str, (UDP_IP, UDP_PORT_IMG))

if __name__ == '__main__':
    main()
