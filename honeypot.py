import http.client
def titaniumcruciblefaas(req):
    connection =  httplib.HTTPConnection('35.201.95.66:80')
    body_content = 'BODY CONTENT GOES HERE'
    connection.request('PUT', '/', body_content)
    result = connection.getresponse()
    return {'result': 'ok'}                                 
