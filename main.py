import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

clear = lambda: os.system('cls')
clear()

# Get the current directory
current_dir = os.getcwd()

count = 0
images = []

# Iterate over all files in the directory
for filename in os.listdir(current_dir + '\\Images'):
    if (filename.endswith('.jpg') or filename.endswith('.png')):
        count += 1
        images.append(filename)
        print(f"Image #{count}: {filename}")

print('\n')
img_num = int(input('enter number of file you want to read: '))


# original image
img = cv2.imread('Images/' + str(images[img_num - 1]))
img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cv2.imshow(str(images[img_num - 1]), img)

# grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cv2.imwrite('Result/gray_' + str(images[img_num - 1]), gray_img)
cv2.imshow('gray_' + str(images[img_num - 1]), gray_img)


#Initialize intensity values with 256 zeroes
intensity_count = [0 for i in range(256)]

height, width = gray_img.shape[:2]
N = height * width                  

#Array for new_image
high_contrast = np.zeros(gray_img.shape) 

for i in range(0, height):
    for j in range(0, width):
        intensity_count[gray_img[i][j]] += 1 # Find pixels count for each intensity

L = 256

intensity_count, total_values_used = np.histogram(gray_img.flatten(), L, [0, L])      
pdf_list = np.ceil(intensity_count * (L - 1) / gray_img.size) # Calculate PDF
cdf_list = pdf_list.cumsum() # Calculate CDF


for y in range(0, height):
    for x in range(0, width): 
	#Apply the new intensities in our new image
        high_contrast[y,x] = cdf_list[gray_img[y, x]]                         


cv2.imwrite('Result/high_contrast_' + str(images[img_num - 1]), high_contrast)  



plt.figure(figsize=(12, 4))
plt.subplot(2, 1, 1)
plt.plot(img_hist, color='black')
plt.title(str(images[img_num - 1]) + ' histogram')
plt.ylabel('Frequency')

plt.subplot(2, 1, 2)
plt.plot(gray_hist, color='black')
plt.title('grayscale image histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.hist(high_contrast.ravel(), 256, [0, 256])	

cv2.waitKey(0)
cv2.destroyAllWindows()
plt.savefig('Result/fig_' + str(images[img_num - 1]))


plt.show()