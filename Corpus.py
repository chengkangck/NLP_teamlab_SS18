# coding: utf-8
"""
this file contain some method to deal with different framework to create corpus library
"""
import pickle
# utils
import io
# emotion package
# from emotion.model.Evaluation import Emotion
# const variable
from corpus import TRAIN_LABEL_CSV as TRAIN_LABEL_CSV
from corpus import PREDICATION_LABEL_CSV as PREDICATION_LABEL_CSV
# logger
import config
from logger import logger

logger = logger(config)


class Corpus:

    # """
    # init some variables
    # """
    def __init__(self):
        #self.train_file =
        #self.test_file =
        # marked labels file
        self.label_file = TRAIN_LABEL_CSV
        self.predicted_file = PREDICATION_LABEL_CSV
        # gold_labels is created by training labels text
        self.gold_labels = []
        # no use
        self.predicted_labels = []

    # """
    # read data from marked label file, and create the gold labels
    # """
    def read_label(self):
        file_handle = io.open_file(self.label_file)
        for line in file_handle:
            self.gold_labels.append(line.strip())
        logger.i('read label successfully')

        return self.gold_labels

    def read_prediction(self):
        file_handle = io.open_file(self.predicted_file)
        for line in file_handle:
            self.predicted_labels.append(line.strip())
        logger.i('read label successfully')

        return self.predicted_labels

