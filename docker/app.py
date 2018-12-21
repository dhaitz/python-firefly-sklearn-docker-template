#!/usr/bin/env python3
# coding=utf-8

import pickle

model = pickle.load(open('model.pkl', 'rb'))


def predict(features):
    return list(model.predict(features))


def predict_extended(features):
    """Return prediction made from input and loaded model"""
    try:
        prediction = model.predict(features)
        return list(prediction)
    except Exception as e:
        return "Error:" + str(e)
