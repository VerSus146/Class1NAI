import numpy as np
import matplotlib.pyplot as plt
from data_preprocessor import import_data
from sklearn import svm, datasets
from matplotlib import style

style.use("ggplot")

def predict_total_amount():
    data = import_data()

    #features are input data, claims
    features = []

    #samples are the expected result after inputting the feature
    samples = []

    #arrays will be scattered for graph purposes
    claims = []
    total_payments = []

    for claim, total_payment in data:
        #graph generation purpose
        claims.append(claim)
        total_payments.append(total_payment)


        features.append([claim])
        samples.append(total_payment)

    # creating SVR for claim, total_payment, linear regression
    svr = svm.SVR(kernel='linear', C=1.0).fit(features, samples)

    # Taking coefficiency

    w = svr.coef_[0]
    a = w

    # Setting the lin
    xx = np.linspace(0,180)
    yy = a* xx - svr.intercept_[0] / w[0]

    # Generating plot
    plt.plot(xx,yy, 'k-',)

    # Scattering data for x,y graph
    plt.scatter(claims, total_payments)
    plt.show()
    # Test data
    print("Prediction of payout for 40 claims: " + str(svr.predict([[40]])[0]) + " thousand swedish crowns")
    print("Prediction of payout for 100 claims: " + str(svr.predict([[100]])[0]) + " thousand swedish crowns")
    print("Prediction of payout for 25 claims: " + str(svr.predict([[25]])[0]) + " thousand swedish crowns")


predict_total_amount()
