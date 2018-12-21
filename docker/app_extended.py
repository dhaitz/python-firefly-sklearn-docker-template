#!/usr/bin/env python3
# coding=utf-8

import pickle
import logging

log = logging.getLogger(f"[{__name__}]")

model = pickle.load(open('model.pkl', 'rb'))


def predict(features):
    """Return prediction made from input and loaded model"""

    log.info(f"Input: {features}")

    if not is_valid_input(features):
        log.error()
        return "Error"

    features_processed = feature_processing(features)

    # apply model
    try:
        prediction = model.predict([features_processed])
        output = list(prediction)[0]
    except Exception as e:
        return "Error:" + str(e)

    if not is_valid_output(output):
        return

    return output


def is_valid_input(features) -> bool:
    """Check if features can be casted to float"""
    for index, feature in enumerate(features):
        log.info(f"Validating feature {index}: {feature}")

        try:
            float(feature)
        except ValueError as value_error:
            log.error(value_error)
            return False

    log.info("Input successfully validated")
    return True


def feature_processing(features):
    # ToDo: add meta feature generation if needed
    return features


def is_valid_output(output) -> bool:
    """Check if output can be casted to float"""
    log.info(f"Output validation: {output}")

    try:
        float(output)
    except ValueError as value_error:
        log.error(value_error)
        return False

    log.info("Output successfully validated")
    return True
