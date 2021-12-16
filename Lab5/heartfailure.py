import tensorflow as tf
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


def df_to_dataset(dataframe, batch_size=8):
    dataframe = dataframe.copy()
    labels = dataframe.pop('HeartDisease')
    return tf.data.Dataset.from_tensor_slices((dict(dataframe), labels)) \
          .shuffle(buffer_size=len(dataframe)) \
          .batch(batch_size)

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

dataFile = r'C:\Users\Krystian\PycharmProjects\Class1NAI\Lab4\heart.csv'
df = pd.read_csv(dataFile)
df.head()


feature_columns = []
'''
for header in ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR',
               'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']:
    feature_columns.append(tf.feature_column.numeric_column(header))
'''

age = tf.feature_column.numeric_column("Age")
age_buckets = tf.feature_column.bucketized_column(age, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])
print(age_buckets)
feature_columns.append(age_buckets)

df["Sex"] = df["Sex"].apply(str)
sex = tf.feature_column.categorical_column_with_vocabulary_list(
      'Sex', ['0', '1'])
sex_one_hot = tf.feature_column.indicator_column(sex)
print(sex_one_hot)
feature_columns.append(sex_one_hot)

df["ChestPainType"] = df["ChestPainType"].apply(str)
ChestPainType = tf.feature_column.categorical_column_with_vocabulary_list(
      'ChestPainType', ['0', '1', '2', '3'])
ChestPainType_one_hot = tf.feature_column.indicator_column(ChestPainType)
print(ChestPainType_one_hot)
feature_columns.append(ChestPainType_one_hot)

RestingBP = tf.feature_column.numeric_column("RestingBP")
RestingBP_buckets = tf.feature_column.bucketized_column(RestingBP, boundaries=[0, 70, 90, 130, 150, 180])
print(RestingBP_buckets)
feature_columns.append(RestingBP_buckets)

Cholesterol = tf.feature_column.numeric_column("Cholesterol")
Cholesterol_buckets = tf.feature_column.bucketized_column(Cholesterol, boundaries=[0, 60, 130, 180, 200, 250, 320])
print(Cholesterol_buckets)
feature_columns.append(Cholesterol_buckets)

FastingBS = tf.feature_column.numeric_column("FastingBS")
print(FastingBS)
feature_columns.append(FastingBS)

df["RestingECG"] = df["RestingECG"].apply(str)
RestingECG = tf.feature_column.categorical_column_with_vocabulary_list(
      'RestingECG', ['0', '1', '2'])
RestingECG_one_hot = tf.feature_column.indicator_column(RestingECG)
print(RestingECG_one_hot)
feature_columns.append(RestingECG_one_hot)

MaxHR = tf.feature_column.numeric_column("MaxHR")
MaxHR_buckets = tf.feature_column.bucketized_column(MaxHR, boundaries=[0, 40, 60, 100, 130, 200, 250])
print(MaxHR_buckets)
feature_columns.append(MaxHR_buckets)

df["ExerciseAngina"] = df["ExerciseAngina"].apply(str)
sex = tf.feature_column.categorical_column_with_vocabulary_list(
      'ExerciseAngina', ['0', '1'])
sex_one_hot = tf.feature_column.indicator_column(sex)
print(sex_one_hot)
feature_columns.append(sex_one_hot)

Oldpeak = tf.feature_column.numeric_column("Oldpeak")
Oldpeak_buckets = tf.feature_column.bucketized_column(Oldpeak, boundaries=[-1, -0.8, 0, 0.5, 1.8, 2.6, 3.56, 4.5])
print(Oldpeak_buckets)
feature_columns.append(Oldpeak_buckets)

df["ST_Slope"] = df["ST_Slope"].apply(str)
slope = tf.feature_column.categorical_column_with_vocabulary_list(
      'ST_Slope', ['0', '1', '2'])
slope_one_hot = tf.feature_column.indicator_column(slope)
print(slope_one_hot)
feature_columns.append(slope_one_hot)

train, test = train_test_split(df, test_size=0.2, random_state=64)
train_ds = df_to_dataset(train)
test_ds = df_to_dataset(test)

print(test_ds)
print(train_ds)

model = tf.keras.models.Sequential([
  tf.keras.layers.DenseFeatures(feature_columns=feature_columns),
  tf.keras.layers.Dense(units=128, activation="relu"),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(units=64, activation="relu"),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(units=8, activation="relu"),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(units=1, activation="sigmoid"),
])

model.compile(optimizer=tf.keras.optimizers.Adam(0.0001), loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_ds, validation_data=test_ds, epochs=100, use_multiprocessing=True)

model.evaluate(test_ds)

plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.ylim((0, 1))
plt.legend(['Train', 'Test'], loc='upper left')

plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
