import cv2
from typing import Any

def save_image(path: str, img: Any) -> None:
    cv2.imwrite(path, img)

def read_image(path: str, mode: int=1) -> None:
    image = cv2.imread(path, mode)
    cv2.imshow('Prueba de lectura', image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    save_image(f'results/copy_{path}', image)

if __name__=="__main__":
    read_image('Banner github.png', 0)