import numpy as np
import cv2 as cv

path = "c:\Users\oheimlic\Desktop\smiley.png"
path_file = "c:\Users\oheimlic\Desktop\similey_values.csv"
img = cv.imread(path, cv.CV_LOAD_IMAGE_GRAYSCALE)
file = open(path_file,"w")

width = img.shape[1]
height = img.shape[0]
img = cv.resize(img,(25, 25))
print img.shape[1]
print img.shape[0]
cv.imshow("img", img)
cv.waitKey(3000)
path_out = "c:\Users\oheimlic\Desktop\smiley_{}x{}.JPG".format(img.shape[1],img.shape[0])
cv.imwrite(path_out,img)
for height in img:
    for px in height:
        file.write(px.__str__() + ", ")
    file.write("\n")

