# Decision Tree Classifier with Streamlit

## Overview

This Streamlit application implements a Decision Tree Classifier using the ID3 algorithm for machine learning tasks. It allows users to upload their own dataset in CSV format, preprocess the data, train a decision tree model, visualize the decision tree, and make predictions.

The application is built using Streamlit, a Python library for building interactive web applications for data science and machine learning.

## Features

- **Dataset Upload**: Users can upload their own dataset in CSV format.
- **Data Preprocessing**: The uploaded dataset is preprocessed using label encoding.
- **Training**: The decision tree model is trained on the preprocessed dataset.
- **Visualization**: Visualize the trained decision tree.
- **Prediction**: Make predictions based on user-input feature values.
- **Evaluation**: Evaluate the model's accuracy on a test dataset.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/decision-tree-classifier.git
   ```
2. Navigate to the project directory:
   ```bash
   cd decision-tree-classifier
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

1. **Run the Streamlit application:**

   ```bash
   streamlit run app.py
   ```
2. **Access the application:**  
   Open the local URL provided by Streamlit in your web browser: [http://localhost:8501](http://localhost:8501).

3. **Upload your dataset:**  
   Use the sidebar file uploader to upload your dataset.

4. **Explore the features and functionalities of the application:**  
   - View the uploaded dataset.
   - Train the decision tree model.
   - Visualize the decision tree.
   - Make predictions based on input feature values.

## Dependencies

The application uses the following Python libraries:

- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`

These dependencies are specified in the `requirements.txt` file.

## Additional Resources

### Sample Video
Watch a demonstration of the application in action in this sample video:
[Sample Video](https://drive.google.com/file/d/15ZqLqHRTX3X6XyEeksnZMu-S_dtXtt04/view?usp=drive_link)

### Blog Post
Read our blog post on Medium to learn more about the development process and features of the application:
[Medium Blog Post](https://medium.com/@prabhuprabhakar647/-2f619c84983f) 
