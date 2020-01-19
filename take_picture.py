import cv2
import time 

cam = cv2.VideoCapture(1)

cv2.namedWindow("test")

img_counter = 300
step = 0
while True:
    ret, frame = cam.read()
    name = "picture" + str(step)
    cv2.imshow("smile", frame)
    k = cv2.waitKey(1000)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    img_name = "red_bull_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1
    time.sleep(0.5)
    print("ok!")
cam.release()

cv2.destroyAllWindows()