import cv2
import os

for file in os.listdir("frames"):
    img = cv2.imread("frames/" + file)
    res = cv2.resize(img, dsize=(32, 24), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("mini/" + file, res) 

print("Done")