import cv2

imgLocation = 'D:\Projects\image_to_pencil_sketch\garfield.jpg'
img = cv2.imread(imgLocation)

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invertedGrayImage = 255 - grayImg
blurredImg = cv2.GaussianBlur(invertedGrayImage, (21,21),0)
invertedBlurredImg = 255 - blurredImg

pencilSketchImage = cv2.divide(grayImg,invertedBlurredImg,scale=256.0)

cv2.imshow('Original Image',img)
cv2.imshow('Pencil Sketch Image', pencilSketchImage)

cv2.waitKey(0)
