# This is the function you should implement. The input parameters are:
# workspace is the location of the directory where the input data files are. This means you need to have everything
# in one directory, and that the result will also be written to this directory. This parameter is a string.
#
# soil, trees, and elevation are the names of the input data layers, as Strings.
#
# soil_text, trees_text, and slope_text are the names of the text files containing the reclass data
#
# cost_surface_name is the name of the cost surface layer to be developed, again as text

def cost_surface(workspace, soil, trees, elevation, soil_text, trees_text, slope_text, cost_surface_name):

    #dummy return to make the skeleton runnable
    return -1

# This is a function that shows you how you should be able to run the cost_surface function. When you have
# developed a cost_surface function that, when this function is run, creates four cost surface layers for you,
# you are at least close to solving the exercise.
#
def test_function():
    # put the name of your workspace directory here!
    # also put all your input data to the workspace directory!
    ws = r'\\your.home\your\data\directory\'

    # the names of the text files, for convenience
    slope='slope_reclass.txt'
    soil='soil_reclass.txt'
    trees='trees_reclass.txt'

    # here your function is called for all the four input data sets provided with the exercise.
    cost_surface(ws, 'A_soil.tif','A_trees.tif','A_elevation.tif',soil,trees,slope,'A_surface.tif')
    cost_surface(ws, 'B_soil.tif','B_trees.tif','B_elevation.tif',soil,trees,slope,'B_surface.tif')
    cost_surface(ws, 'C_soil.tif','C_trees.tif','C_elevation.tif',soil,trees,slope,'C_surface.tif')
    cost_surface(ws, 'D_soil.tif','D_trees.tif','D_elevation.tif',soil,trees,slope,'D_surface.tif')


# this is the main function
def main():
    print 'starting test'
    test_function()
    print 'test ended'

# This is the part that calls the rest of the code
if __name__ == "__main__":
    main()
