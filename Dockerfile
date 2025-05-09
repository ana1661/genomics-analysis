FROM public.ecr.aws/lambda/python:3.10

# Install your Python packages
RUN pip install --upgrade pip && \
    pip install scikit-learn numpy

# Copy your function and model into the container
COPY lambda_function.py tumor_model.pkl ./

# Set the handler (entry point for Lambda)
CMD ["lambda_function.lambda_handler"]