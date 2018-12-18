# python-firefly-docker-sklearn-template
A simple example of python api for real time machine learning.
Offline, a simple linear regression model is created and saved on disk.
In the running container, on request via the prediction API, the simple model is loaded and returns a prediction.
For more information read [this post](https://blog.solutotlv.com/deployed-scikit-learn-model-flask-docker/?utm_source=Github&utm_medium=python-flask-sklearn-docker-template)


Requirements: docker installed


## Train model and copy model file to docker folder

    cd model-training/
    ./train_model.py
    mv some_model.pkl ../docker/
    cd ..
    

## Build image

    cd docker/
    docker build . -t test_project

## Start container  

Detached mode:

     docker run -p 3000:5000 -d test_project

Interactive mode (for debug):

    docker run -p 3000:5000 -it test_project


## Obtain prediction via API  
Create a test file:

    echo '{"features": [[1, 2, 3]]}' > dummy-input.json
    
Send data to the running container and obtain result:
    
    curl -v -d '{"features": [[1,2,3]]}' http://127.0.0.1:3000/predict
    
Result:

    [0.4999999999999999]
