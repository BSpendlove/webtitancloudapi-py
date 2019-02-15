from webtitancloudapi.webtitan import webtitanAPI
import requests

class UsersAPI(object):
    jsonmap = {
        'accountname':'accountname',
        'name':'name',
        'email':'email',
        'description':'description',
        'license':'license',
        'password':'password',
        'timezone':'timezone'}

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def create_account(self, account_name, account_email, account_license, account_password, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Users-PostRestapiUsers
        payload = {
            'accountname' : account_name,
            'email' : account_email,
            'license' : account_license,
            'password' : account_password
            }

        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users'
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def delete_account(self, account_id):
        #http://apidoc.webtitancloud.com/#api-Users-DeleteRestapiUsersId
        apiUrl = '/users/%s' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.delete)
        return(req)

    def get_account(self, account_id):
        #http://apidoc.webtitancloud.com/#api-Users-GetRestapiUsersId
        apiUrl = '/users/%s' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_all_accounts(self):
        #http://apidoc.webtitancloud.com/#api-Users-GetRestapiUsers
        apiUrl = '/users'
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def update_account(self, account_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Users-PostRestapiUsersId
        payload = {
            'id' : account_id
            }

        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        print(payload)
        apiUrl = '/users/%s' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)
    
