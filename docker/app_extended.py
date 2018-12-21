#!/usr/bin/env python3
# coding=utf-8

import pickle
import logging

log = logging.Logger("log")

model = pickle.load(open('model.pkl', 'rb'))


def predict_professional(features_raw):
    """Return prediction made from input and loaded model"""

    log.info(features_raw)

    if not is_valid_input(features_raw):
        return "Error"

    # feature_preprocessing
    features_processed = feature_processing(features_raw)

    try:
        prediction = model.predict(features_processed)
        output = list(prediction)
    except Exception as e:
        return "Error:" + str(e)

    if not is_valid_output(output):
        return

    return output


def is_valid_input(features_raw):
    # do some checks
    return True


def feature_processing(features):
    # add some meta features
    return features


def is_valid_output(output):
    # do some checks
    return True
