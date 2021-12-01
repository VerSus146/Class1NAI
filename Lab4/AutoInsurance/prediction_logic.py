import numpy as np
import matplotlib.pyplot as plt
from data_preprocessor import import_data
from sklearn import svm, datasets


def predict_total_amount():
    data = import_data()

    features = []
    samples = []
    for claim, total_payment in data:
        features.append([claim])
        samples.append(total_payment)

    print(features)
    print(samples)
    # creating SVM for claim, total_payment
    svc = svm.SVR(kernel='linear', C=1.0).fit(features, samples)
    print(svc.predict([[40]]))

predict_total_amount()
