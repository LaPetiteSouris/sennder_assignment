# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from api.handlers import template_handler
from api.utils import logger

ghibli = Blueprint('sennder', __name__)
log = logger.define_logger(__name__)


@ghibli.route('v1/ping', methods=['GET'])
def index():
    return jsonify({'response': 'pong'}), 200


@ghibli.route('v1/template', methods=['GET'])
def template():
    response = template_handler.on_request(request)
    return jsonify(response), 200