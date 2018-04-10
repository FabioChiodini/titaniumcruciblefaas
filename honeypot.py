# from flask import Flask, jsonify, request
import urllib
def titaniumcruciblefaas(req):
    params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    f = urllib.urlopen("35.201.95.66", params)
    print f.read( )
    return jsonify({'result': 'ok'})
