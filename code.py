import tifffile
import numpy as np
import re

#def cost_surface(soil, trees, elevation, soil_text, trees_text, slope_text, cost_surface_name):

    #dummy return to make the skeleton runnable
    #return -1

def DEMtoDegrees(dem):

    px, py = np.gradient(dem, 1)
    slope = np.sqrt(px**2 + py **2)
    slope_deg = np.degrees(np.arctan(slope))

    return slope_deg

def reClassTif(tif, reclass):
    origReclass = reclass
    classifier = []

    for row in origReclass:
        reclasser = re.split('[" " :]', row)
        break

    if reclasser[1] == "":
        for row in reclass:
            parts = row.split()
            classifier.append([int(parts[0]), int(parts[2])])

        for row in range(len(tif)):
            for column in range(len(tif[0])):
                pixelValue = tif[row][column]
                if pixelValue == 32767:
                    tif[row][column] = 0
                for key, value in classifier:
                    if pixelValue == key:
                        tif[row][column] = value
                        break

    else:
        for row in reclass:
            parts = row.split()
            classifier.append([int(parts[0]), int(parts[1].replace(":", "")), int(parts[2])])
        
        for row in range(len(tif)):
            for column in range(len(tif[0])):
                pixelValue = tif[row][column]
                if pixelValue == 32767:
                    tif[row][column] = 0
                for low, high, value in classifier:
                    if pixelValue > low and pixelValue <= high:
                        tif[row][column] = value
                        break
            
    return tif

def testCostSurface():
    slope = open('input_data/slope_reclass.txt')
    trees = open('input_data/trees_reclass.txt')
    soilReclass = open('input_data/soil_reclass.txt')

    letters = ["A", "B", "C", "D"]

    for letter in letters:
        
        slopeTif = reClassTif(DEMtoDegrees(tifffile.imread("input_data/{}_elevation.tif".format(letter))),slope)
        outputFileName = "{}_slope.tif".format(letter)
        tifffile.imwrite(outputFileName, slopeTif)

        soilTif = reClassTif(tifffile.imread("input_data/{}_soil.tif".format(letter)), soilReclass)
        outputFileName = "{}_soil.tif".format(letter)
        tifffile.imwrite(outputFileName, soilTif)

        treesTif = reClassTif(tifffile.imread("input_data/{}_trees.tif".format(letter)), trees)
        outputFileName = "{}_trees.tif".format(letter)
        tifffile.imwrite(outputFileName, treesTif)

        #elevationTif = tifffile.imread("input_data/{}_elevation.tif".format(letter))
        
        break

        res1 = slopeTif * soilTif
        res2 = res1 * treesTif

        outputFileName = "{}_output.tif".format(letter)
        tifffile.imwrite(outputFileName, res2)
        break
        #print(elevationTif[0][0])


    #soilTif = tifffile.imread("input_data/A_soil.tif")
    #treesTif = tifffile.imread("input_data/A_trees.tif")


    #tif = tifffile.imwrite("output.tif", tif)


#this is the main function
def main():
    testCostSurface()

# This is the part that calls the rest of the code
if __name__ == "__main__":
    main()