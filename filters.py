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

def adjustContrast(img:np.ndarray, val:int):
    floatimg = img.astype(np.float32)
    newimg = floatimg*val

    return np.clip(newimg,0,255).astype(np.uint8)

def flipImage(img:np.ndarray,mode = "Horizondal"):
    if mode == "Horizondal":
        return img[:,::-1,:]
    elif mode == "Vertical":
        return img[::-1,:,:]
    elif mode == "180":
        return img[::-1,::-1,:]
    else:
        raise ValueError("Mode must be 'horizontal', 'vertical', or '180'")