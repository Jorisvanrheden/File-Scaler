import cv2
import os
import math
import numpy as np

maxFileSize = 2000000

inputDirectory = r"D:\repos\File Scaler\Input\\"
outputDirectory = r"D:\repos\File Scaler\Output\\"

files = os.listdir(inputDirectory)
for file in files:

    fullFilePath = inputDirectory + file
    fileSize = os.path.getsize(fullFilePath)

    image = cv2.imread(fullFilePath)

    if fileSize > maxFileSize:
        scaler = fileSize / maxFileSize
        dimensionScaler = math.sqrt(scaler)

        scaledWidth = int(image.shape[0] / dimensionScaler)
        scaledHeight = int(image.shape[1] / dimensionScaler)
        scaleDimensions = (scaledHeight, scaledWidth)

        print(scaleDimensions)

        resizeImage = cv2.resize(image, scaleDimensions)
        cv2.imwrite(outputDirectory + file, resizeImage)
    else:
        image = cv2.imread(fullFilePath)
        cv2.imwrite(outputDirectory + file, image)