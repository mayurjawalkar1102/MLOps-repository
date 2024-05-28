import os
import argparse
import itertools
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

from azureml.core import Dataset, Run
run = Run.get_context()


