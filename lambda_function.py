#import boto3
import pickle
import json
import numpy as np
from sklearn.linear_model import LogisticRegression 




with open('tumor_model.pkl', 'rb') as f:
        model = pickle.load(f)
    #return model


def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return {
            'statusCode': 200,
            'body': json.dumps({'prediction': int(prediction[0])})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
