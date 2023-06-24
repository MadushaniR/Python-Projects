import cv2

#load the image from its location
imgLocation = 'D:\Projects\image_to_pencil_sketch\garfield.jpg'
img = cv2.imread(imgLocation)

# Convert the image to grayscale
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invertedGrayImage = 255 - grayImg

# Apply Gaussian blur to the inverted grayscale image
blurredImg = cv2.GaussianBlur(invertedGrayImage, (21,21), 0)

# Invert the blurred image
invertedBlurredImg = 255 - blurredImg

# Create the pencil sketch image by dividing the grayscale image by the inverted blurred image
pencilSketchImage = cv2.divide(grayImg, invertedBlurredImg, scale=256.0)

# Display the original image and the pencil sketch image
cv2.imshow('Original Image', img)
cv2.imshow('Pencil Sketch Image', pencilSketchImage)

# Wait for a key press to exit the program
cv2.waitKey(0)
