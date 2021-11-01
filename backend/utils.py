from flask import jsonify
import re
import unidecode


def success_response(data=None):
    status = {'status': 'success'}
    if data:
        data.update(status)
    else:
        data = status

    return jsonify(data)


def error_response(message=''):
    return jsonify({'status': 'error', 'message': message})


def sanitizeString(string):
    string = re.sub('ª', ' ', string)
    string = re.sub('º', ' ', string)
    string = re.sub('°', ' ', string)

    # remove all accents
    string = unidecode.unidecode(string)

    # Remove all Markup tags in string
    p = re.compile(r'<.*?>')
    string = p.sub('', string)

    string = re.sub(r'[^A-Za-z0-9]+', '', string)

    return string.lower()
