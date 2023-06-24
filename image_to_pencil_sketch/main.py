import cv2

#load the image from its location
imgLocation = 'D:\Projects\image_to_pencil_sketch\garfield.jpg'
img = cv2.imread(imgLocation)

# Convert the image to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invertedGrayImage = 255 - grayImg
blurredImg = cv2.GaussianBlur(invertedGrayImage, (21,21),0)
invertedBlurredImg = 255 - blurredImg

pencilSketchImage = cv2.divide(grayImg,invertedBlurredImg,scale=256.0)

cv2.imshow('Original Image',img)
cv2.imshow('Pencil Sketch Image', pencilSketchImage)

cv2.waitKey(0)
