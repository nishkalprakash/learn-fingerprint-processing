from matplotlib import pyplot as plt
import cv2 as cv
from pathlib import Path
import numpy as np

class Image:
    """Returns an object of an Image 
        if width is integer and height not provided:
            height=width
        if iterable:
            raw_data = iterable
        if str or path
            path = path of image
            raw_data = load from path
        height
        width
        raw_data of image # init as zeros
    """
    def __init__(self, width=-1, height=-1):
        """Constructor to store image

        Args:
            width (int|str|path|iterable): width of the image
            height (int): height of the image
        """
        

        # if width is a string or Path then load the image from the given path
        if isinstance(width,str) or isinstance(width,Path):
            self.load(width)
            return
        # if width is an iterable then load the image from the given iterable
        if hasattr(width,"__iter__"):
            self.image = np.array(width)
            self.height,self.width = self.image.shape[:2]
            return
        # if width is not given, then skip the initialization
        if width == -1:
            self.image=None
            return
        # if height is not given, then height is equal to width
        self.width = width
        self.height = width if height == -1 else height
        # image stores the image as a numpy array with 0 as default values
        self.image = np.array([[0]*self.width]*self.height)
        
    def plot(self,title="",**kwargs):
        """Plots the image using matplotlib"""
        plt.axis('off')
        plt.title(title)
        plt.imshow(self.image,**kwargs)
        # plt.show()
    
    def show(self,title=""):
        """Shows the image using opencv"""
        cv.imshow(title,self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
    def load(self,path):
        """Loads the image from the given path"""
        self.image = cv.imread(str(path))
        self.height,self.width = self.image.shape[:2]
        self.path=Path(path)

    def save(self,path):
        """Saves the image to the given path"""
        cv.imwrite(path,self.image)
        # plt.savefig(f"{path}.png", bbox_inches='tight')
