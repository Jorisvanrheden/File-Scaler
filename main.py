import cv2
import os
import math
import numpy as np

maxFileSize = 2000000

scale = 0.5

inputDirectory = r"D:\repos\File Scaler\Input\\"
outputDirectory = r"D:\repos\File Scaler\Output\\"

files = os.listdir(inputDirectory)
for file in files:
    fullFilePath = inputDirectory + file

    fileSize = os.path.getsize(fullFilePath)

    if fileSize > maxFileSize:
        print("Exceeded!")

        scaler = fileSize / maxFileSize
        dimensionScaler = math.sqrt(scaler)

        image = cv2.imread(file)

        scaledWidth = int(image.shape[0] / dimensionScaler)
        scaledHeight = int(image.shape[1] / dimensionScaler)
        scaleDimensions = (scaledHeight, scaledWidth)
        resizeImage = cv2.resize(image, scaleDimensions)

        cv2.imwrite(outputDirectory + file, resizeImage)

print("Hello world")


