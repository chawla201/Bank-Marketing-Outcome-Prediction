# Bank-Marketing-Outcome-Prediction

## Overview

This repository contains a machine learning project aimed at predicting the outcomes of bank marketing campaigns. The dataset used for this project is derived from real-world marketing campaigns conducted by a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).

## Features

- **Data Preprocessing**: Includes handling missing values, encoding categorical variables, and feature scaling.
- **Exploratory Data Analysis (EDA)**: Visualizations and statistical analysis to understand the dataset.
- **Model Training**: Implementation and fine tuning of Logistic Regression machine learning algorithm.
- **Model Evaluation**: Metrics like accuracy, precision, recall, F1-score, and ROC-AUC are used to evaluate model performance.
- **Deployment**: Includes steps for deploying the trained model using MLOps practices.

## Model Performance:
Logistic Regression algorithm is used for the binary classification task. \
```
LogisticRegression(max_iter = 1000, solver = 'sag')
```
**Performance Outcome:**
```
ROC AUC: 0.9559803921568626
              precision    recall  f1-score   support

           0       0.89      0.95      0.92       150
           1       0.88      0.75      0.81        68

    accuracy                           0.89       218
   macro avg       0.89      0.85      0.87       218
weighted avg       0.89      0.89      0.89       218
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Bank-Marketing-Outcome-Prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Bank-Marketing-Outcome-Prediction
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
### Localhost API
1. Open a terminal/comand prompt window and navigate to the project directory:
    ```bash
    cd Bank-Marketing-Outcome-Prediction
    ```
2. Run the FastAPI server:
    ```bash
    fastapi dev app.py
    ```
3. Go to the "Local Deployment" section under the "API Testing" section in the bank_additional.ipynb notebook
4. Validate that the urls mentioned in the cells is correct and run the first 2 cells to check if the API is working fine
5. Load the test data in the python notebook and pass it as a parameter in the get request to the API
6. Print the response from the API and evaluate the predictions accordingly

### Docker Deployment
1. Open Docker Desktop on your personal computer
2. Open a terminal/comand prompt window and navigate to the project directory:
    ```bash
    cd Bank-Marketing-Outcome-Prediction
    ```
3. Build a docker image:
    ```bash
    docker build -t bank-additional-image .
    ```
4. Build a docker container:
    ```bash
    docker run -d --name bank-additional-container -p 80:80 bank-additional-image
    ```
5. Open docker hub to validate that the container is built successfully and the API is running in the container
6. Go to the "Docker Deployment on Local" section under the "API Testing" section in the bank_additional.ipynb notebook
7. Validate that the urls mentioned in the cells is correct and run the first 2 cells to check if the API is working fine
8. Load the test data in the python notebook and pass it as a parameter in the get request to the API
9. Print the response from the API and evaluate the predictions accordingly

### AWS Deployment
1. Create an image repository on Docker Hub
2. Create an image repository on the local Docker Desktop with the same name and tag the docker image to the repository
    ```bash
    docker tag bank-additional-image chawla201/bank-additional-assignment
    ```
3. Push the local repository on to the Docker Hub
    ```bash
    docker push chawla201/bank-additional-assignment
    ```
4. Open AWS console and log in with your account
5. Go to Elastic Container Service (ECS)
6. Go to task definitions section from the left panel
7. Create new task definition
    * use AWS fargate as launch type
    * change the OS to "Linux/ARM64"
    * select task role as "ecsTaskExecutionRole"
    * add container details and show that the docker image is being taken from the docker hub repository
    * leave rest to default settings
8. Go to cluster section from the left pannel
9. Create a new cluster
    * give an appropriate cluster name
    * select aws fargate in the infrastructure section
    * leave rest to default settings
10. Open the newly created cluster and scroll down to the services section 
11. Create a new section
    * select the task definition family in service details section
    * select "Launch type" compute option in the compute configuration section
    * leave rest to default
12. Once the service has been successfully deployed, open the newly created service
13. Go to the configuration and networking tab and scroll down to network configuration
14. Click on the link under security groups
    * VPS dashboard will open in a new tab
    * click on edit inbound rules and modify the second rule's source to "My IP" to allow traffic from my IP to the deployed API on the public IP
15. On the service page, go to the "Tasks" tab 
    * click on the running task
    * scroll down to the configuration section
    * copy the public IP  
16. Go to the "AWS Deployment" section under the "API Testing" section in the bank_additional.ipynb notebook
17. Paste the public IP in the appropriate cells and run the first 2 cells to check if the API is working fine
18. Load the test data in the python notebook and pass it as a parameter in the get request to the API
19. Print the response from the API and evaluate the predictions accordingly


## Dataset

The dataset used in this project is publicly available and can be downloaded from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing).
### Citation:
S. Moro, P. Rita, and P. Cortez. "Bank Marketing," UCI Machine Learning Repository, 2014. [Online]. Available: https://doi.org/10.24432/C5K306.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
