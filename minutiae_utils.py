"""File containing the various minutiae extraction methods"""
from setup_logger import get_logger
logger = get_logger(__name__)

def crossing_number(image):
    """Extracts the minutiae from the image using the crossing number method
    
    Args:
        image (np.ndarray): The image from which the minutiae are to be extracted


    Returns:
        list: The minutiae extracted from the image, each minutiae is dict(x,y,angle,type)
    """
    logger.info("Extracting minutiae using crossing number method")
    minutiae = []
    """TODO: Implement crossing number method for minutiae extraction"""
    return minutiae
    
def minutiae_net(image):
    """Extracts the minutiae from the image using the minutiae net method
    
    Args:
        image (np.ndarray): The image from which the minutiae are to be extracted
    
    Returns:
        list: The minutiae extracted from the image, each minutiae is dict(x,y,angle,type)
    """
    logger.info("Extracting minutiae using minutiae net method")
    minutiae = []
    """TODO: Implement minutiae net method for minutiae extraction"""
    return minutiae



