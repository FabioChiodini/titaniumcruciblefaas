# from flask import Flask, jsonify, request
import os
import logging
import logstash
import sys
import logging.handlers
import requests

#if 'LOG_HOST' not in os.environ:
#    raise(Exception("LOG_HOST NOT DEFINED"))

#host = os.environ['LOG_HOST']

test_logger = logging.getLogger('python-http-logger')
test_logger.setLevel(logging.INFO)
#test_logger.addHandler(logging.handlers.HTTPHandler(host, '/', method='POST'))
test_logger.addHandler(logging.handlers.HTTPHandler('35.190.59.153', '/', method='POST'))

#app = Flask(__name__)

def titaniumcruciblefaas(req):
    extra = {
        'ip': request.environ.get('X-Forwarded-For', request.remote_addr),
        'url': req.full_path,
    }
    test_logger.info('honeypot: ', extra=extra)
    #result = request.environ.get('X-Forwarded-For', request.remote_addr)
    #new line
    return {'result': ok}

#    data_to_log.update(req.headers)

#@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
#def honey(path):
#    log_request(request)
#    return jsonify({'result': 'ok'})

#if __name__ == '__main__':
#app.run(host="0.0.0.0",port=8080)
