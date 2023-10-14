import skimage
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io
from skimage.feature import hog
from skimage import exposure

car = io.imread('datasets/cat.png')