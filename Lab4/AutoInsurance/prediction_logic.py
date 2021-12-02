import numpy as np
import matplotlib.pyplot as plt
from data_preprocessor import import_data
from sklearn import svm, datasets
from matplotlib import style

style.use("ggplot")

def predict_total_amount():
    data = import_data()

    features = []
    samples = []
    claims = []
    total_payments = []
    for claim, total_payment in data:
        #graph generation purpose
        claims.append(claim)
        total_payments.append(total_payment)

        features.append([claim])
        samples.append(total_payment)

    print(features)
    print(samples)
    # creating SVM for claim, total_payment

    # plt.scatter(claims,total_payments)
    # plt.show()

    svc = svm.SVR(kernel='linear', C=1.0).fit(features, samples)
    w = svc.coef_[0]
    a = w
    xx = np.linspace(-5,180)
    yy = a* xx - svc.intercept_[0] / w[0]
    h0 = plt.plot(xx,yy, 'k-', label="non weighted div")
    plt.scatter(claims, total_payments, c = y)
    plt.show()
    print(w)
    print(svc.predict([[40]]))


predict_total_amount()
