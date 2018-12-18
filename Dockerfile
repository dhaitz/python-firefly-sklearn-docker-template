# Options for building image
FROM python:3.6
RUN pip install --no-cache-dir pandas==0.20.2  scikit-learn==0.20.0  firefly-python==0.1.15  # or with -r requirements.txt
COPY app.py model.pkl ./

# Options for starting container
ENTRYPOINT firefly app.predict --bind 0.0.0.0:5000
EXPOSE 3000
