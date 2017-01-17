from matplotlib import pyplot

def view(array):
    """
    Gives a simple heatmap representation of a 2D numpy array
    
    Argument
    --------
    array -- a 2D numpyarray
    """
    pyplot.imshow(array, interpolation='nearest')
    pyplot.colorbar()
    pyplot.axis('off')
    pyplot.show()
