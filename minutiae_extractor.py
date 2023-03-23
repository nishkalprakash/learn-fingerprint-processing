from utils import (
    skeletonize,
    binarize,
    enhancer,
    filter_mask,
    minutiae_generator,
    minutiae_angles,
)
import cv2 as cv


def feature_vector(img0):
    img1 = skeletonize(binarize(enhancer(img0)))
    mask = filter_mask(img0)
    minutiae_pts_arr = minutiae_generator(img1)
    filtered_minutiae = list(filter(lambda m: mask[m[1], m[0]] > 20, minutiae_pts_arr))
    minutiae_angle = minutiae_angles(filtered_minutiae, img1)
    return minutiae_angle


def extract_minutiae(ip_path):
    img = cv.imread(ip_path, cv.IMREAD_GRAYSCALE)
    fv = feature_vector(img)
    return fv
    # f = open(op_path, "w")
    # f.write(str(fv))


def extract_minutiae_vector(ip_path):
    # from pymongo import MongoClient as mc

    # if not mc("10.5.18.101")["BI"]["mv"].count_documents({'path':ip_path},limit=1):

        img = cv.imread(str(ip_path), cv.IMREAD_GRAYSCALE)
        fv = feature_vector(img)
        # try:
        #     fv = feature_vector(img)
        # except Exception as e:
        #     print(str(e))
            # fv=[]
        # return {"path": str(ip_path), "mv": fv}