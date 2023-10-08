# from PIL import Image                                                                                
# img1 = Image.open('C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/wallpapers/orange.jpg')
# img2 = Image.open('C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/wallpapers/orange.jpg')

# img1.show()

# import cv2
# import numpy as np
# a = cv2.imread("C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/wallpapers/pic1.jpg")
# b = cv2.imread("C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/wallpapers/pic2.jpg")
# difference = cv2.subtract(a, b)    
# # cv2.imshow('Subtracted Image', difference)

# print(difference)
# result = not np.any(difference)
# if result is True:
#     print("Pictures are the same")
# else:
#     print("Pictures are different")

from skimage.metrics import structural_similarity as compare_ssim
import argparse
# import imutils
import cv2

a = cv2.imread("C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/wallpapers/img1.jpg")
b = cv2.imread("C:/Users/sushr/Dropbox/My PC (LAPTOP-AC0PDSKE)/Desktop/Sushree/wallpapers/img2.jpg")

# A = cv2.resize(a, (W, H))
(H, W) = a.shape[:-1]
b = cv2.resize(b, (W, H))

grayA = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

if(score == 1):
    print("Images are Same")
else:
    print("Images are Different")