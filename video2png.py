import cv2
vidcap = cv2.VideoCapture('<--- Here is path to movie --->')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames/%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  count += 1
print("Done")