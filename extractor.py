import cv2
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="a python script that extract images from video"
    )
    parser.add_argument("video", help="the video that you want to extract")
    parser.add_argument("-p", "--path", help="the directory you want to store your extracted images", required=True)
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_args()

    vid_file = args.video
    vid = cv2.VideoCapture(vid_file)

    vid_path = args.path

    try:
        if not os.path.exists(vid_path):
            os.mkdir(vid_path)

    except OSError:
        print('Error: while creating directory of output')

    currentFrame = 0

    while True:
        ret, frame = vid.read()

        if ret:
            name = f'./{vid_path}/frame_{str(currentFrame)}.jpg'
            print('creating..', name)
            cv2.imwrite(name, frame)

            currentFrame += 1
        else:
            break

    vid.release()
    cv2.destroyAllWindows()
