"""Http client fetch of API in JSON format

This module includes the function call_API() that will 
perform a http fetch request to the specified URL.
Successful request will return a Python dictionary.
"""

import http.client
import ssl
import json

def call_API(address, path, options):
    """Perform HTTP fetch request
    address - String containing domain-name:port or IP-address:port
    path - String containing location of data on API server
    options - SSL/TLS options
    Returns - Python dictionary containing decoded JSON data.
    On error, returns python dictionary with error and errorMessage properties.
    """

    request_headers = {
            "Accept": "application/json"
        }

    if options["use_ssl"]:
        context = ssl.create_default_context()
        context.check_hostname = options["check_hostname"]
        context.minimum_version = ssl.TLSVersion.TLSv1_2

        if options["custom_certs"]:
            context.load_cert_chain(certfile=options["certfile"], keyfile = options["keyfile"])
            context.load_verify_locations(cafile=options["cafile"])

    try:
        if options["use_ssl"]:
            conn = http.client.HTTPSConnection(address, timeout=5, context=context)
        else:
            conn = http.client.HTTPConnection(address, timeout=5)
    except Exception as x:
        return {"error":1,"errorMessage":"Create connection error: {}".format(x)}

    try:
        conn.request("GET", path, body="", headers=request_headers)
    except Exception as x:
        return {"error":2,"errorMessage":"HTTP request error: {}".format(x)}

    try:
        response = conn.getresponse()
    except Exception as x:
        return {"error":3,"errorMessage":"HTTP response error: {}".format(x)}

    if not response.status == 200:
        return {"error":4,"errorMessage":"Error HTTP status: " + str(response.status)}

    try:
        data = response.read() #  this is byte data
    except Exception as x:
        return {"error":5,"errorMessage":"HTTP data read error: {}".format(x)}

    strdata = str(data,"utf-8")

    if len(strdata) < 1:
        try:
            response.close()
        except:
            pass
        return {"error":6,"errorMessage":"Error response has no body"}

    try:
        jsonbody = json.loads(strdata) # python dictionary
    except Exception as x:
        return {"error":7,"errorMessage":"JSON decode error: {}".format(x)}

    try:
        response.close()
    except:
        None

    return jsonbody

if __name__ == "__main__":
    # For Debug perform the API fetch and display data
    #
    f = open("./config.json","r")
    config = json.load(f)
    f.close()

    options = {}
    options["use_ssl"]        = config["use_ssl"]
    options["check_hostname"] = config["ssl_check_hostname"]
    options["custom_certs"]   = config["ssl_custom_certs"]
    options["cafile"]         = config["ssl_CA_cert"]
    options["certfile"]       = config["ssl_client_cert"]
    options["keyfile"]        = config["ssl_client_key"]

    dataJson = call_API(config["address"], config["path"], options);
    
    print(json.dumps(dataJson, indent=4))