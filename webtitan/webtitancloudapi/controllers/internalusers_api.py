from webtitancloudapi.webtitan import webtitanAPI
import requests

class InternalUsersAPI(object):
    jsonmap = {
        'id' : 'id',
        'userid' : 'userid',
        'policyid' : 'policyid'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def get_internal_user(self, account_id, userid):
        #http://apidoc.webtitancloud.com/#api-Internalusers-GetRestapiUsersIdUsersUserid
        apiUrl = '/users/%s/users/%s' %(account_id, userid)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def list_customer_internal_users(self, account_id):
        #http://apidoc.webtitancloud.com/#api-Internalusers-GetRestapiUsersIdUsers
        apiUrl = '/users/%s/users' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def update_internal_user_policy(self, account_id, userid):
        #http://apidoc.webtitancloud.com/#api-Internalusers-PostRestapiUsersIdUsersUserid
        payload = {
            'id' : account_id,
            'userid' : userid
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/users/%s' %(account_id, userid)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)