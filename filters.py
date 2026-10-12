import numpy as np

def toGrayScale(img: np.ndarray):
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]

    out = r*0.299 + g*0.587 + 0.114*b
    return out.astype(np.uint8)

def adjustBrightness(img: np.ndarray, val: int):

    floatimg = img.astype(np.float32)
    newimg = floatimg + val

    return np.clip(newimg, 0 , 255).astype(np.uint8)