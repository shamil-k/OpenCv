from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2

# construct the argument parse and parse the arguments
# --images : The path to your directory containing the images you want to build a montage out of.
# --samples : An optional command line argument that specifies the number
# of images to sample (we default this value to 21  total images).
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to input directory of images")
ap.add_argument("-s", "--sample", type=int, default=21,
                help="# of images to sample")
args = vars(ap.parse_args())

# grab the paths to the images, then randomly select a sample of
# them
imagePaths = list(paths.list_images(args["images"]))
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]

