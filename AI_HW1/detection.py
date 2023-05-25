import os
import cv2
import matplotlib.pyplot as plt

def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """

    """
Firstly, I read the file "detectData.txt" and store its data in a list called "text" using the "readlines" method.
Then, I use a while loop to iterate through the lines in the list. There are two parts to the loop:

1. Reading the information about the picture:
I use the "split" function to separate the picture name and the number of faces to detect.
I then use the "imread" function to read the picture and load it into a variable called "pic".

2.Detecting the faces in the picture:
I use a for loop to iterate through all the marked faces.
Using the "map(int, ListName)" method, I convert the list of elements from strings to integers.
I then extract the subimage and store it in a variable called "newImage".
Since the subimage is not 19x19, I use the "cv2.resize" function to resize it to 19x19 and change its color to grayscale using 
the "cv2.cvtColor(cv2.COLOR_BGR2GRAY)" function.  Thus, "newImage" becomes a 19x19 grayscale image.
Finally, I use the "classify()" function to detect the picture. If the output is 1, I draw a green rectangle on the image,
otherwise I draw a red rectangle on it.
At every step, I increment the variable "cur" by 1 to get the information on the next line.
In the end , I use the "imshow()" function to display the resulting image and the "waitKey()" function to wait for a key press 
before closing the window.
    """
    # Begin your code (Part 4)
    cur = 0
    f = open(dataPath, 'r')
    text = f.readlines()

    while cur < len(text):
        slide = text[cur]

        cur += 1
        temp = slide.split(' ')
        pic = temp[0]
        img = cv2.imread("data/detect/" + pic)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.bilateralFilter(gray, 9, 75, 75)
        edges = cv2.Canny(blurred, 100, 200)

        for j in range(int(temp[1])):
            cor = list(map(int, text[cur].split(' ')))
            cur = cur + 1
            newImage = img[cor[1]: cor[1] + cor[3], cor[0]:cor[0] + cor[2]]
            newImage = cv2.resize(newImage, (19, 19))
            newImage = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
            if clf.classify(newImage) == 1:
                img = cv2.rectangle(img, (cor[0],cor[1]), (cor[0] + cor[2], cor[1] + cor[3]), (0,255,0), 2)
            else:
                img = cv2.rectangle(img, (cor[0],cor[1]), (cor[0] + cor[2], cor[1] + cor[3]), (0,0,255), 2)
        
        cv2.imshow('photo', img)
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

        cv2.waitKey(0)
    # End your code (Part 4)
