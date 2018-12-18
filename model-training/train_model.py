#!/usr/bin/env python3
# coding=utf-8

"""Train simple model and save to disk"""

import pickle
from sklearn import linear_model


def train_and_save_model(savepath):
    reg_model = linear_model.LinearRegression()
    reg_model.fit([[1.,1.,5.], [2.,2.,5.], [3.,3.,1.]], [0.,0.,1.])

    print("Saving model to", savepath)
    pickle.dump(reg_model, open(savepath, 'wb'))


if __name__ == "__main__":
    train_and_save_model('model.pkl')
