from flask import jsonify


def success_response(data=None):
    status = {"status": "success"}
    if data:
        data.update(status)
    else:
        data = status

    return jsonify(data)


def error_response(message=""):
    return jsonify({"status": "error", "message": message})
