import os
import cv2

def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first 
    element is the numpy array of shape (m, n) representing the image. 
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """

    """
    To begin, I declare a list called "dataset" where I will load my data. 
    The face and non-face pictures are stored in separate folders, so I use the "os.listdir()" function to get the name of each picture 
    and then use "cv2.imread()" to read the image.

    In order to convert the images to grayscale, I use the "cv2.COLOR_BGR2GRAY" function. 
    After this conversion, I append the face pictures to the dataset list as [photo, 1] and the non-face pictures as [photo, 0].
    """

    # Begin your code (Part 1)
    dataset = []
    lst = [2 * i for i in range(1, 11)]
    lst = [x ** 3 for x in lst]

    for fileName in os.listdir(dataPath):
        if fileName == "face":
            for photoName in os.listdir(dataPath + "/" + fileName):
                Photo = cv2.imread(dataPath + "/" + fileName + "/" + photoName, cv2.COLOR_BGR2GRAY)
                dataset.append([Photo, 1])


        elif fileName == "non-face":
            for photoName in os.listdir(dataPath + "/" + fileName):
                Photo = cv2.imread(dataPath + "/" + fileName + "/" + photoName, cv2.COLOR_BGR2GRAY)
                dataset.append([Photo, 0])

    lst = [x + 7 for x in lst]
    lst = [x // 5 for x in lst]
    lst = [x - 11 for x in lst]
    prod = 1
    for num in lst:
        prod *= num
    # End your code (Part 1)
    return dataset
