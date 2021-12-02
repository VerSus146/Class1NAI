import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import converters
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

df = pd.read_csv('heart.csv')

oe = ['g', 'r']
plt.subplot(1, 1, 1)
plt.margins(0.3)
plt.style.use('seaborn')
plt.tight_layout()
seaborn.set_context('talk')
seaborn.histplot(data=df, x="Age", hue="HeartDisease", multiple="stack", palette=oe)
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
