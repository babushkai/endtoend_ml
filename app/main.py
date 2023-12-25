from fastapi.logger import logger
from fastapi import FastAPI, Request
import tensorflow as tf

import numpy as np
import argparse
import os

import logging

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers

if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)

app = FastAPI()

logger.info("Loading model")
model = tf.saved_model.load('/model')

@app.get("/health", status_code=200)
def health():
    """ health check to ensure HTTP server is ready to handle 
        prediction requests
    """
    return {"status": "healthy"}


@app.post("/predict")
async def predict(request: Request):
    body = await request.json()
    instances = body["instances"]
    inputs = []
    for instance in instances:
        inputs.append(instance['bytes_inputs']['b64'])
       
    # unfinished, returns Internal Server error
    #outputs = model.predict(inputs)
    #logger.info(f"Outputs {outputs}")
    #return {"predictions": [class_num for class_num in np.argmax(outputs, axis=1)]}
    return {'test': 'to-be-finished'}