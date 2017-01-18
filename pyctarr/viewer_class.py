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
    def __init__(self, array, disp_time=1):
        """
        Instantiates a viewer object with a given array and display time
    
        Arguments
        ---------
        array -- a 2D numpy array to be viewed later
        disp_time -- desired display time for each plot; plot refresh speed
        """
        self.array = array
        self.disp_time = disp_time
        self.fig, self.ax, self.im = None, None, None

    def view(self):
        """
        Basic viewing function that creates a single heatmap with the original
        array.
        """
        if None in (self.fig, self.ax, self.im):
            self.fig, self.ax = pyplot.subplots()
            self.im = self.ax.imshow(self.array, interpolation='nearest')        
        else:
            self.im.set_array(self.array)

        pyplot.draw()
        pyplot.pause(self.disp_time)

    def update(self, narray):
        """
        Updates local array and displays new array by calling the view function
    
        Arguments
        ---------
        narray -- new 2D numpy array
        """
        self.array = narray
        self.view()
