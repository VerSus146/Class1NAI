import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.dummy import DummyClassifier

import Lab4.HeartFailure.converters as converters
import seaborn
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
        Down - 0
        Flat - 1
        Up - 2
    FastingBS:
        0 - N
        1 - Y
'''

fbs_conv = lambda fbs: converters.fastingbs_converter(fbs)
sex_conv = lambda s: converters.sex_converter(s)
cpt_conv = lambda cpt: converters.chestpaintype_converter(cpt)
recg_conv = lambda recg: converters.restingecg_converter(recg)
ea_conv = lambda ea: converters.exerciseangina_converter(ea)
sts_conv = lambda sts: converters.st_slope_converter(sts)


# Read feature data from CSV. Converters change string data to numeric data needed for svm.SVC fit
heart = pd.read_csv('../heart.csv',
                    usecols=["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG",
                             "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"],
                    converters={"Sex": sex_conv, "ChestPainType": cpt_conv,
                                "RestingECG": recg_conv, "ExerciseAngina": ea_conv, "ST_Slope": sts_conv})

# Read Heart failure data from CSV.
target = pd.read_csv('../heart.csv', usecols=["HeartDisease"])

# Train
svc = svm.SVC(kernel='rbf', C=1, gamma=100).fit(heart, target)

# Patient to be tested against our trained model - Data from Krystian's GF > Medical student
test = np.array([45, 0, 3, 145, 240, 0, 2, 90, 0, 0, 0])
test = test.reshape(1, -1)

# Nicely displayer data
print("Subject of test:")
print(f"Age: {test[0, 0]}")
print(f"Sex: {test[0, 1]}")
print(f"Chect Pain Type: {test[0, 2]}")
print(f"Resting BP: {test[0, 3]}")
print(f"Cholesterol: {test[0, 4]}")
print(f"FastingBS: {test[0, 5]}")
print(f"Resting ECG: {test[0, 6]}")
print(f"Max HR: {test[0, 7]}")
print(f"Exercise Angina: {test[0, 8]}")
print(f"Oldpeak: {test[0, 9]}")
print(f"ST Slope: {test[0, 10]}")

print(f"Heart Failure (Prediction): {svc.predict(test)[0]}")
# Correct answer according to Medical Student

df = pd.read_csv('../heart.csv', converters={"FastingBS": fbs_conv})
# Creating Data Frame for diagram display

dummy_clf = DummyClassifier(strategy="stratified")
dummy_clf.fit(heart, target)
DummyClassifier(strategy='stratified')
dummy_clf.predict(test)
print('Accuracy ' + str(dummy_clf.score(heart, target)))

# Colors for diagram
oe = ['g', 'r']

plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
# Layout for PLT
plt.tight_layout()
# Default style type
seaborn.set_context('talk')
# Create histogram with provided data, also histogram smoothing and colors.
seaborn.histplot(data=df, x="Age", hue="HeartDisease", multiple="stack", palette=oe)
# Show diagram
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="Sex", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="ChestPainType", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="RestingBP", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="Cholesterol", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="FastingBS", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="RestingECG", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="MaxHR", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="ExerciseAngina", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="Oldpeak", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="ST_Slope", hue="HeartDisease", multiple="stack", palette=oe)
plt.show()
