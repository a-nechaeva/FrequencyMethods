import cv2 as cv2
import numpy as np


img = cv2.imread('14.png')

img_array = np.array(img) / 255.0

f_image = np.fft.fftshift(np.fft.fft2(img_array, axes=(0, 1)))

abs_arr = abs(f_image)

angle_arr = np.angle(f_image)

for i in range(len(abs_arr)):
    for j in range(len(abs_arr[i])):
        abs_arr[i][j] = np.log(abs_arr[i][j] + 1)

norm_abs_arr = ((abs_arr - abs_arr.min()) / (abs_arr.max() - abs_arr.min()))


cv2.imwrite("res1.png", norm_abs_arr)

print(norm_abs_arr)
