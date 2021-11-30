import numpy as np
import matplotlib.pyplot as plt
from data_preprocessor import import_data
from sklearn import svm,datasets

def predict_total_amount():
    data = import_data()
    claims = []
    total_amounts = []
    for claim, total_amount in data:
        claims.append(claim)
        total_amounts.append(total_amount)
    print(claims)
    print(total_amounts)

    #creating SVM for claim, total_payment
    svc = svm.SVC(kernel='rbf', C=1, gamma=100).fit(claims, total_amounts)

predict_total_amount()