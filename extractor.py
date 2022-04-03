import cv2
import os

vid = cv2.VideoCapture('./test.mp4')

try:
    if not os.path.exists('output'):
        os.makedirs('output')

except OSError:
    print('Error: while creating directory of output')

currentFrame = 0

while True:
    ret, frame = vid.read()

    if ret:
        name = './output/frame' + str(currentFrame) + '.jpg'
        print('creating..', name)
        cv2.imwrite(name, frame)

        currentFrame += 1
    else:
        break

vid.release()
cv2.destroyAllWindows()
