#!/usr/bin/env python3
# coding=utf-8

import pickle
import logging

log = logging.getLogger("prediction")

model = pickle.load(open('model.pkl', 'rb'))


def predict(features):
    """Return prediction made from input and loaded model"""

    log.info(f"Input: {features}")

    if not is_valid_input(features):
        log.error()
        return "Error"

    features_processed = feature_processing(features)

    try:
        prediction = model.predict([features_processed])
        output = list(prediction)[0]
    except Exception as e:
        return "Error:" + str(e)

    if not is_valid_output(output):
        return

    return output


def is_valid_input(features):
    for index, feature in enumerate(features):
        log.info(f"Validating feature {index}: {feature}")

        try:
            float(feature)
        except ValueError as value_error:
            log.error(f"Could not convert to float {value_error}")
            return False

    return True


def feature_processing(features):
    # add some meta features
    return features


def is_valid_output(output):
    log.info(output)
    # do some checks
    return True
