# import the necessary packages
from os import path

# define the type of dataset we are training (i.e., either "age" or # "gender")
DATASET_TYPE = "gender"

# define the base paths to the faces dataset and output path
BASE_PATH = "/raid/datasets/adience"
OUTPUT_BASE = "output"
MX_OUTPUT = BASE_PATH

# based on the base path, derive the images path and folds path
IMAGES_PATH = path.sep.join([BASE_PATH, "aligned"])
LABELS_PATH = path.sep.join([BASE_PATH, "folds"])
