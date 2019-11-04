import cv2
import numpy as np# Reading in and displaying our image


high_res=cv2.imread('HR.png')
high_res_inv = cv2.bitwise_not(high_res)

cv2.imshow('Original', high_res_inv)



image = cv2.imread('output.png')
#image2 = cv2.bitwise_not(image)



#Create our shapening kernel, it must equal to one eventually

kernel_sharpening = np.array([[0,-1,0], 
                              [-1, 5,-1],
                              [0,-1,0]])# applying the sharpening kernel to the input image & displaying it.

sharpened = cv2.filter2D(image, -1, kernel_sharpening)
#imagem = cv2.bitwise_not(sharpened)

lanczos4=cv2.resize(image, (384, 384), interpolation = cv2.INTER_LANCZOS4)

cv2.imshow('Image Sharpening', lanczos4)
#cv2.imwrite('result.png', lanczos4)
cv2.waitKey(0)
cv2.destroyAllWindows()