import cv2
from typing import Any

def get_video(path: str='results/video_test.avi') -> None:
    video_capture = cv2.VideoCapture(path)
    while video_capture.isOpened():
        ret, image = video_capture.read()
        if ret:
            cv2.imshow('video', image)
            # if OS is based in 64 bits is necesary add 0xff
            if cv2.waitKey(30) & 0xFF == ord('s'):
                break
        else: break
    video_capture.release()
    cv2.destroyAllWindows()

def read_video_camera() -> None:
    try:
        video_capture = cv2.VideoCapture(2)
        video_output = cv2.VideoWriter('results/video_test.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
        while video_capture.isOpened():
            ret, image = video_capture.read()
            if ret:
                cv2.imshow('video', image)
                video_output.write(image)
                # if OS is based in 64 bits is necesary add 0xff
                if cv2.waitKey(2) & 0xFF == ord('s'):
                    break
        video_capture.release()
        video_output.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)


if __name__=="__main__":
    read_video_camera()