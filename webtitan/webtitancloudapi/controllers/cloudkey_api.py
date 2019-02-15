from webtitancloudapi.webtitan import webtitanAPI
import requests

class CloudKeyAPI(object):
    jsonmap = {
        'id':'id',
        'logname':'logname',
        'keyid':'keyid',
        'expiresafter':'expiresafter',
        'expiresafterperiod':'expiresafterperiod',
        'maxuse':'maxuse',
        'validfrom':'validfrom',
        'validto':'validto',
        'comment':'comment',
        'active':'active'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def create_cloud_key(self, account_id, **kwargs):
		#http://apidoc.webtitancloud.com/#api-Cloudkeys-CreateCloudKey
        payload = {
            'id':account_id
            }

        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/cloudkeys/?' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def delete_cloud_key(self, account_id, cloudkey_id):
		#http://apidoc.webtitancloud.com/#api-Cloudkeys-DeleteCloudKey
        apiUrl = '/users/%s/cloudkeys/%s' %(account_id. cloudkey_id)
        req = self.webtitan.query(apiurl, method=requests.delete)
        return(req)

    def get_user_cloudkey(self, account_id, cloudkey_id):
        #http://apidoc.webtitancloud.com/#api-Cloudkeys-GetCloudKey
        apiUrl = '/users/%s/cloudkeys/%s' %(account_id, cloudkey_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_user_cloudkeys(self, account_id):
		#http://apidoc.webtitancloud.com/#api-Cloudkeys-GetCloudKeys
        apiUrl = '/users/%s/cloudkeys' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)