import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import converters
from sklearn import svm, datasets

'''
Converters:
    Sex:
        M - 0
        F - 1
    ChestPainType:
        ASY - 0
        NAP - 1
        ATA - 2
        TA - 3
    RestingECG:
        Normal - 0
        LVH - 1
        ST - 2
    ExerciseAngina:
        N - 0
        Y - 1
    ST_Slope:
        Up - 0
        Flat - 1
        Down - 2
'''

sex_conv = lambda s: converters.sex_converter(s)
cpt_conv = lambda cpt: converters.chestpaintype_converter(cpt)
recg_conv = lambda recg: converters.restingecg_converter(recg)
ea_conv = lambda ea: converters.exerciseangina_converter(ea)
sts_conv = lambda sts: converters.st_slope_converter(sts)

heart = pd.read_csv('heart.csv',
                    usecols=["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG",
                             "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"],
                    converters={"Sex": sex_conv, "ChestPainType": cpt_conv,
                                "RestingECG": recg_conv, "ExerciseAngina": ea_conv, "ST_Slope": sts_conv})
print(heart)

target = pd.read_csv('heart.csv', usecols=["HeartDisease"])
print(target)

svc = svm.SVC(kernel='rbf', C=1, gamma=100).fit(heart, target)

# 38,M,NAP,138,175,0,Normal,173,N,0,Up - result 0
# 38,0,1,138,175,0,0,173,0,0,0

test = np.array([45, 0, 3, 145, 240, 0, 2, 90, 0, 0, 0])
test = test.reshape(1, -1)

print(svc.predict(test))


'''
# import some data to play with
iris = datasets.load_iris()
print(iris)
X = iris.data[:, :2] # we only take the first two features. We could
 # avoid this ugly slicing by using a two-dim dataset
y = iris.target

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
svc = svm.SVC(kernel='rbf', C=1, gamma=100).fit(X, y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
 np.arange(y_min, y_max, h))

plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
'''
