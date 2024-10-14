from flask import Blueprint, request
from markupsafe import escape
import api.service as service

blueprint = Blueprint("routes", __name__)


@blueprint.route("/")
def home():
    return "<h1>LLM RESTful API</h1>"


@blueprint.route("/api/chat/", methods=["POST"])
def post_chat():
    input_args = request.get_json()

    if input_args is None:
        return {"message": "empty payload"}

    message = input_args.get("message")

    if message is None:
        return {"message": "no message parameter in the payload"}

    return service.chat(message=message)
