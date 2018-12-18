#!/usr/bin/env python3
# coding=utf-8

import pickle

loaded_model = pickle.load(open('model.pkl', 'rb'))


def predict(features):
    """Return prediction made from input and loaded model"""
    try:
        prediction = loaded_model.predict(features)
        return list(prediction)
    except Exception as e:
        return "Error:" + str(e)
