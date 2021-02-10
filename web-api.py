#
# web_api_v2.py
#
# Written by Mark Streffprd
# (c) 2020 Delirium Digital Limited
#
# Based on code from https://towardsdatascience.com/detectron2-the-basic-end-to-end-tutorial-5ac90e2f90e3
#

import flask
from flask import request, jsonify
from flask_cors import CORS
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2 import model_zoo

import base64
from PIL import Image
from io import BytesIO
import requests
import numpy as np
import blosc


def score_image(predictor, image_base64):
    """
    Decode a base64 encoded image and run predictor
    """
    image_raw = Image.open(BytesIO(base64.b64decode(image_base64)))
    image = np.array(image_raw)
    return predictor(image)


def prepare_predictor():
    """
    Create predictor for instance segmentation. Use pre-trained mask-rcnn model
    """
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model (default value)
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
    _predictor = DefaultPredictor(cfg)

    _classes = MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes
    _predictor = DefaultPredictor(cfg)
    print("Predictor has been initialized.")
    return _predictor, _classes


# Setup flask
app = flask.Flask(__name__)
CORS(app)
predictor, classes = prepare_predictor()


@app.route("/api/score-image", methods=["POST"])
def process_score_image_request():
    """
    Call predictor with request data and return classes, scores, boxes and prediction masks
    """
    scoring_result = score_image(predictor, request.get_data())

    instances = scoring_result['instances']
    scores = instances.get_fields()['scores'].tolist()
    pred_classes = instances.get_fields()['pred_classes'].tolist()
    pred_boxes = instances.get_fields()['pred_boxes'].tensor.tolist()
    pred_masks = np.array(instances.get_fields()['pred_masks'].cpu())
    print(pred_masks.shape, len(pred_masks[pred_masks == True]))

    response = {
        'scores': scores,
        'pred_classes': pred_classes,
        'pred_boxes': pred_boxes,
        'pred_masks': blosc.pack_array(pred_masks).hex(),
        'classes': classes
    }

    return jsonify(response)


# Default config for running Flask app
app.run(host="0.0.0.0", port=5000)
