import cv2

print("Package imported")

#SHOW IMAGE

# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)



#SHOW VIDEO
# capVideo = cv2.VideoCapture("Resources/test_video.mp4")
#
#
# while True:
#     success, img = capVideo.read()
#     cv2.imshow("Video", img)
#
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

#SHOW VIDEOCAM
cam = cv2.VideoCapture(0)
cam.set(3, 640)#Width
cam.set(4, 480)#Height
cam.set(10, 100)#Brigthness

while True:
    success, img = cam.read()

    if success:
        cv2.imshow("Video", img)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        print("Camera doesn't work")
        break

