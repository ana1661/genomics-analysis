# Gene Expression Cancer Classifier

This project leverages machine learning to classify tumor vs. non-tumor samples based on high-dimensional gene expression data. It features a real-time deployment pipeline using AWS Lambda and a user-friendly Streamlit frontend.

## Live App
🔗 [Try the Live Classifier](https://genomics-analysis-6mpu8ckcclvgnn3euxb8xe.streamlit.app/)

## Features
- Binary classification model trained on gene expression microarray data (22,269 features)
- Real-time predictions using a scikit-learn model deployed via AWS Lambda (containerized)
- User-facing web interface built with Streamlit and hosted via Streamlit Cloud
- GitHub-backed version control and reproducibility

## Technologies Used
- `scikit-learn` for machine learning
- `pandas`, `numpy` for data processing
- `Docker` for containerizing the Lambda function
- `AWS Lambda`, `API Gateway` for scalable cloud inference
- `Streamlit` for frontend deployment
- `GitHub` for version control and Streamlit Cloud integration

## How It Works

1. **Data Preparation**: Gene expression data was cleaned, transposed, and labeled as tumor (1) or non-tumor (0).
2. **Model Training**: A logistic regression model was trained using scikit-learn with thousands of gene features.
3. **Model Deployment**:
   - Model serialized with `pickle`
   - Dockerized and uploaded to AWS Lambda (container image)
   - API Gateway configured to route prediction requests
4. **Frontend Deployment**:
   - Streamlit app connects to the Lambda API
   - Hosted using Streamlit Community Cloud
   - Users can paste in gene data to get real-time predictions

## Project Structure

```bash
├── app.py                  # Streamlit frontend
├── lambda_function.py      # AWS Lambda code for inference
├── Dockerfile              # Lambda container image definition
├── tumor_model.pkl         # Trained machine learning model
├── requirements.txt        # Python dependencies
└── README.md               # Project overview (this file)
