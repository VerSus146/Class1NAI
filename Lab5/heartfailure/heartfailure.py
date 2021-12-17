import tensorflow as tf
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

# change DataFrame to dataset of tensors and change them into batches
def df_to_dataset(dataframe, batch_size=64):
    dataframe = dataframe.copy()
    labels = dataframe.pop('HeartDisease')
    return tf.data.Dataset.from_tensor_slices((dict(dataframe), labels)).shuffle(buffer_size=len(dataframe))\
        .batch(batch_size)


dataFile = r'../../Lab4/heart.csv'
df = pd.read_csv(dataFile)
df.head()

# Create empty list
feature_columns = []

# Create a bucketized feature column for age
# Create an numeric column for age
age = tf.feature_column.numeric_column("Age")
# Create bucketized age column
age_buckets = tf.feature_column.bucketized_column(age, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])
# Add to feature columns list
feature_columns.append(age_buckets)

RestingBP = tf.feature_column.numeric_column("RestingBP")
RestingBP_buckets = tf.feature_column.bucketized_column(RestingBP, boundaries=[0, 70, 90, 130, 150, 180])
feature_columns.append(RestingBP_buckets)

Cholesterol = tf.feature_column.numeric_column("Cholesterol")
Cholesterol_buckets = tf.feature_column.bucketized_column(Cholesterol, boundaries=[0, 60, 130, 180, 200, 250, 320])
feature_columns.append(Cholesterol_buckets)

Oldpeak = tf.feature_column.numeric_column("Oldpeak")
Oldpeak_buckets = tf.feature_column.bucketized_column(Oldpeak, boundaries=[-1, -0.8, 0, 0.5, 1.8, 2.6, 3.56, 4.5])
feature_columns.append(Oldpeak_buckets)

MaxHR = tf.feature_column.numeric_column("MaxHR")
MaxHR_buckets = tf.feature_column.bucketized_column(MaxHR, boundaries=[0, 40, 60, 100, 130, 200, 250])
feature_columns.append(MaxHR_buckets)

# Create an numeric feature column for FastingBS
# Create an numeric column for FastingBS
FastingBS = tf.feature_column.numeric_column("FastingBS")
# Add to feature columns list
feature_columns.append(FastingBS)

# Create indicator column for sex by first changing it's string data into numbers
# Change data into string type
df["Sex"] = df["Sex"].apply(str)
# Create categorical column by changing string into numbers
sex = tf.feature_column.categorical_column_with_vocabulary_list(
      'Sex', ['0', '1'])
# Create indicator column from categorical column
sex_one_hot = tf.feature_column.indicator_column(sex)
# Add to feature columns list
feature_columns.append(sex_one_hot)

df["ChestPainType"] = df["ChestPainType"].apply(str)
ChestPainType = tf.feature_column.categorical_column_with_vocabulary_list(
      'ChestPainType', ['0', '1', '2', '3'])
ChestPainType_one_hot = tf.feature_column.indicator_column(ChestPainType)
feature_columns.append(ChestPainType_one_hot)

df["RestingECG"] = df["RestingECG"].apply(str)
RestingECG = tf.feature_column.categorical_column_with_vocabulary_list(
      'RestingECG', ['0', '1', '2'])
RestingECG_one_hot = tf.feature_column.indicator_column(RestingECG)
feature_columns.append(RestingECG_one_hot)

df["ExerciseAngina"] = df["ExerciseAngina"].apply(str)
sex = tf.feature_column.categorical_column_with_vocabulary_list(
      'ExerciseAngina', ['0', '1'])
sex_one_hot = tf.feature_column.indicator_column(sex)
feature_columns.append(sex_one_hot)

df["ST_Slope"] = df["ST_Slope"].apply(str)
slope = tf.feature_column.categorical_column_with_vocabulary_list(
      'ST_Slope', ['0', '1', '2'])
slope_one_hot = tf.feature_column.indicator_column(slope)
feature_columns.append(slope_one_hot)

# Split data into train and test sets
train, test = train_test_split(df, test_size=0.2, random_state=64)
train_ds = df_to_dataset(train)
test_ds = df_to_dataset(test)

# Create Neural Network Model
# ToDO: Learn more about Neural Network Layers
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

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(0.0001), loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(train_ds, validation_data=test_ds, epochs=100, use_multiprocessing=True)

# Evaluate the model on test data
model.evaluate(test_ds)

# Plot the accuracy and val_accuracy
plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.ylim((0, 1))
plt.legend(['Train', 'Test'], loc='upper left')

# Plot the loss and val_loss
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
