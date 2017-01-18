from matplotlib import pyplot

class Viewer(object):
    """
    Class used to make updatable heatmap images of 2D numpy arrays. Can be used
    to quickly and easily view 2D numpy arrays while a script is running
    
    Methods
    -------
    view -- displays an heatmap of the array for a specified length of time
    update -- updates the viewers array and then the image
    """
    def __init__(self, array, disp_time=1, colormap="viridis"):
        """
        Instantiates a viewer object with a given array and display time
    
        Arguments
        ---------
        array -- a 2D numpy array to be viewed later
        disp_time -- desired display time for each plot; plot refresh speed
        colormap -- colormap used for heatmap; for list of colormaps see
            http://matplotlib.org/examples/color/colormaps_reference.html
        """
        self.__is2D(array)
        self.array = array
        self.disp_time = disp_time
        self.fig, self.ax, self.im = None, None, None
        if self.array.dtype == 'bool':
            self.colormap = "Greys"  # grey scale for boolean data type
        else:
            self.colormap = colormap

    def view(self, block=False):
        """
        Basic viewing function that creates a single heatmap with the original
        array.

        Arguments
        ---------
        block -- boolean for if script should be blocked by image
        """
        if None in (self.fig, self.ax, self.im):
            self.fig, self.ax = pyplot.subplots()
            self.im = self.ax.imshow(self.array, cmap=self.colormap,
                interpolation='nearest')
            pyplot.colorbar(self.im)
        else:
            self.im.set_array(self.array)
        
        
        self.ax.axis("off")
        pyplot.show(block=block)
        pyplot.pause(self.disp_time)

    def update(self, narray):
        """
        Updates local array and displays new array by calling the view function
    
        Arguments
        ---------
        narray -- new 2D numpy array
        """
        self.__is2D(narray)
        self.array = narray
        self.view()

    @staticmethod
    def __is2D(array):
        """Class method to check array isn't larger than 2D"""
        if len(array.shape) > 2:
            raise ValueError("Array is more than 2 dimensions")
