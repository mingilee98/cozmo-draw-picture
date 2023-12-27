import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Sequential

labels_df = pd.read_csv("training_data.csv")
train_df, val_df = train_test_split(labels_df, test_size=0.2, random_state=42)
image_folder = "training_data"

# create generators for training and validation data
train_datagen = ImageDataGenerator(rescale=1.0 / 255)
val_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_dataframe(
    dataframe=train_df,
    directory=image_folder,
    x_col="filename",
    y_col="label",
    target_size=(256, 256),
    batch_size=32,
    class_mode="categorical",
)

val_generator = val_datagen.flow_from_dataframe(
    dataframe=val_df,
    directory=image_folder,
    x_col="filename",
    y_col="label",
    target_size=(256, 256),
    batch_size=32,
    class_mode="categorical",
)

# create ML model using cnn
model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(256, 256, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(3, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# train the ML model
epochs = 10
model.fit(train_generator, epochs=epochs, validation_data=val_generator)

evaluation = model.evaluate(val_generator)
print(f"Accuracy: {evaluation[1]*100:.2f}%")

model.save("shape_detection_model.keras")
