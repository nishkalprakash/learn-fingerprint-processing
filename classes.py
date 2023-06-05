#%% Imports
from matplotlib import pyplot as plt
import cv2 as cv
from pathlib import Path
import numpy as np
from pprint import pprint as pp
from minutiae_utils import crossing_number, minutiae_net

#%% Logging
from setup_logger import get_logger

logger = get_logger(__name__)

#%% Image Class  
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

        if isinstance(width,str|Path):
            """if width is a string or path then load the image from the given path"""
            logger.info(f"Loading image from path: {width}")
            self.init_from_path(width)
            return

        if hasattr(width,"__iter__"):
            """if width is an iterable then load the image from the given iterable"""
            logger.info(f"Loading image from iterable")
            self.init_from_list(width)
            return

        if isinstance(width,list|tuple|np.ndarray):
            """if width is an list|tuple|nd.ndarray then load the image from the given iterable"""
            logger.info(f"Loading image from {type(width)}")
            self.init_from_list(width)
            return

        
        if width == -1:
            """if width is not given, then skip the initialization"""
            logger.info(f"Skipping initialization of image")
            self.image=None
            return
        
        self.width = width
        
        # if height is not given, then height is equal to width
        self.height = width if height == -1 else height
        # image stores the image as a numpy array with 0 as default values
        logger.info(f"Initializing empty 1 channel image with 0 of size {self.width}x{self.height}")
        self.image = np.array([[0]*self.width]*self.height)
        

    
    ## START INIT METHODS for image ##
    def __getitem__(self,key):
        """Returns the value of the image at the given key"""
        d = self.__dict__
        if key in d.keys():
            return d[key]
        logger.warning(f"Unknown key: {key}")
        # return self.__dict__[key]
    
    def init_from_dict(self, doc):
        """Initializes the image from the given mongo document"""
        ## copy all the fields from the document to __dict__
        logger.info(f"Initializing image from mongo document")
        for key in doc.keys():
            self.__dict__[key] = doc[key]
            
        # for key in doc.keys():
            # match key:
            #     case "image":
            #         self.image = np.array(doc["image"])
            #     case "path":
            #         self.path = Path(doc["path"])
            #     case "mv":
            #         self.mv = doc["mv"]
            #     case "height":
            #         self.height = doc["height"]
            #     case "width":
            #         self.width = doc["width"]
            #     case "core":
            #         self.core = doc["core"]
            #     case "db":
            #     case _:
            #         logger.warning(f"Unknown key: {key}")
        # else:
        #     self.image = np.array()
        #     self.path = Path(doc["path"])
        #     self.init_height_width()
    
    def init_one_from_mongo_coll(self,coll,query={}):
        """Initializes the image from the given mongo collection"""
        ## Count the number of images that match the query and only init if count is 1
        if coll.count_documents(query) == 0:
            logger.error(f"There are no images that match the query: {query}")
            raise Exception("There are no images that match the query")
        elif coll.count_documents(query) > 1:
            logger.error(f"There are more than one images that match the query: {query}")
            raise Exception("There are more than one images that match the query")
        else:
            # populate all fields from the collection
            logger.info(f"Initializing image from mongo collection with query: {query}")
            self.init_from_dict(coll.find_one(query))

            # pass


        # self.image = np.array(coll.find_one())
        # self.init_height_width()


    def init_from_list(self,raw_data):
        """Initializes the image from the given list"""
        self.image = np.array(raw_data)
        self.init_height_width()

    def init_from_path(self,path):
        """Loads the image from the given path"""
        self.image = cv.imread(str(path))
        self.init_height_width()
        self.path=Path(path)

    def init_height_width(self):
        """Initializes the height and width of the image"""
        self.height,self.width = self.image.shape[:2]
    ## END INIT METHODS for image ##


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
        
    
    def save(self,path):
        """Saves the image to the given path"""
        cv.imwrite(path,self.image)
        # plt.savefig(f"{path}.png", bbox_inches='tight')

    def get_minutiae(self, method=None):
        """Returns the extract the minutiae from the fingerprint image extracted using the given method"""
        self.minutiae_methods({
            "crossing_number":crossing_number,
            "minutiae_net":minutiae_net,
        })
        logger.info(f"Available minutiae extraction methods:\n{pp(self.minutiae_methods)}")
        self.default_minutiae_method = "crossing_number"
        if method is None:
            logger.info(f"returning minutiae extrated using default method [{self.default_minutiae_method}]")
            return self.extract_minutiae(self.default_minutiae_method)
        elif method in self.minutiae_methods:
            logger.info(f"returning minutiae extrated using method [{method}]")
            self.mv=self.mvs.get(method,self.extract_minutiae(method))
        return self.minutiae

    def extract_minutiae(self, method):
        """Extract the minutiae from the fingerprint image using the given method, should only be called from self.get_minutiae()"""
        logger.info(f"Extracting minutiae using method: {method}")
        if method in self.mintiae_methods:
            return self.minutiae_methods[method](self.image)
            # case "minutiae_net":
                # return self.minutiae_net()
        else:
            logger.error(f"Unknown method: {method}")
            raise Exception(f"Unknown method: {method}")
    
        # return self.minutiae_methods[method](self.image)
