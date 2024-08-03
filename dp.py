import numpy as np 
import pandas as pd 
import tensorflow as tf 
import cv2 
from skimage import measure 
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_arrayfrom tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
# Load your dataset 
# Replace 'data' and 'labels' with your dataset 
# Make sure your images are properly organized in subdirectories for each class data = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2) 
train_data = data.flow_from_directory( r'C:\\Users\\VKRAMYA.ai\\Desktop\\dataset\\blood  cells\\dataset2-master\\dataset2-master\\images\\TRAIN', target_size=(128, 128), 
 batch_size=32, class_mode='categorical', subset='training') 
val_data = data.flow_from_directory(r'C:\\Users\\VKRAMYA.ai\\Desktop\\dataset\\blood  cells\\dataset2-master\\dataset2-master\\images\\TEST', target_size=(128, 128), 
 batch_size=32, class_mode='categorical', subset='validation') 
# Create a CNN model 
model = Sequential() 
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3))) model.add(MaxPooling2D((2, 2))) 
model.add(Conv2D(64, (3, 3), activation='relu')) 
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu')) 
model.add(MaxPooling2D((2, 2))) 
model.add(Flatten()) 
model.add(Dense(128, activation='relu')) 
model.add(Dropout(0.5)) 
model.add(Dense(4, activation='softmax')) # Assuming 4 blood cell types 
# Compile the model 
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) 
# Train the model (you can adjust the number of epochs) 
history = model.fit(train_data, epochs=10, validation_data=val_data) 
# Load and preprocess a single image 
image_path = r'C:\\Users\\VKRAMYA.ai\\Desktop\\a.jpeg' # Replace with the path to your single  image 
image = load_img(image_path, target_size=(128, 128)) 
image_array = img_to_array(image) / 255.0 # Preprocess the image image_array = np.expand_dims(image_array, axis=0) # Add a batch dimension 
# Predict the blood cell type 
predicted_probs = model.predict(image_array)[0] 
predicted_class_index = np.argmax(predicted_probs) 
# Define class names (modify based on your classes) 
class_names = ['lymphocyte', 'monocyte', 'neutrophil', 'eosinophil'] 
# Display the image and predicted blood cell type 
plt.imshow(image) 
plt.title(f'Predicted: {class_names[predicted_class_index]}') 
plt.axis('off')
plt.show() 
# Load the blood cell image 
image_path = r'C:\\Users\\VKRAMYA.ai\\Desktop\\a.jpeg'  
image = cv2.imread(image_path) 
# Preprocess the image 
# Apply any necessary preprocessing steps such as resizing, noise reduction, and contrast  enhancement. 
# Convert the image to grayscale 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# Threshold the image to create a binary mask 
_, binary_mask = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) 
# Find contours in the binary mask 
contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
# Calculate the area of each contour to estimate cell count 
cell_count = len(contours) 
# Display the result 
print(f"Estimated blood cell count: {cell_count}") 
# Optionally, visualize the result 
result_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2) cv2.imshow('Blood Cell Count Prediction', result_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
# ... (previous code) 
# Calculate the area of each contour to estimate cell count cell_count = len(contours) 
# Define a threshold to determine low and normal cell counts (modify as needed) low_count_threshold = 5 # Example threshold, you should adjust this 
# Determine health status based on cell count 
if:
    cell_count < low_count_threshold: 
    health_status = "Potential Health Issue" 
else: 
     health_status = "Normal Health" 
# Display the result 
print(f"Estimated blood cell count: {cell_count}") 
print(f"Predicted Health Status: {health_status}") 
# Optionally, visualize the result 
result_image = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2) 
cv2.putText(result_image, f"Predicted Health: {health_status}", (10, 30),  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) 
cv2.imshow('Blood Cell Count and Health Status Prediction', result_image) cv2.waitKey(0) 
cv2.destroyAllWindows()
