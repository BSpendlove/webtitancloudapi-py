import requests
import json
from pprint import pprint
from requests_oauthlib import OAuth1

class webtitanAPI(object):
    def __init__(self, server, consumer_key, consumer_secret, access_token, access_secret, ssl_verify=True):
        self.server = server
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.ssl_verify = ssl_verify
        self.auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
        self.serverApiUrl = "https://%s:8443/restapi" %(server)

    def payloadBuilder(self, objmap=None, **kwargs):
        """ build the REST payload """
        payload = {}
        for key, val in kwargs.items():
            if key in objmap:
                payload[objmap[key]] = val
        return payload

    def query(self, entrypoint, method=requests.get, data=None, params=None, auth=None, json_handle=True):
        headers = {}

        if data != None:
            if type(data) != str:
                if json_handle:
                    data = json.dumps(data)
                    headers['Content-Type'] = 'application/json'
                else:
                    headers['Content-Type'] = 'application/x-www-form-urlencoded'
                    
            if method == requests.get:
                method = requests.post

        p = method(
            self.serverApiUrl + entrypoint,
            data=data,
            params=params,
            headers=headers,
            auth=self.auth,
            verify=self.ssl_verify
            )

        response = json.loads(p.text)

        if p.status_code == 404:
            print("Resource could not be found within the WebTitan API")

        #debug
        if 'data' not in response:
            return(response)

        return(response['data'])
