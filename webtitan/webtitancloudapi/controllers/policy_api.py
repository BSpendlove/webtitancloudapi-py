from webtitancloudapi.webtitan import webtitanAPI
import requests

class PolicyAPI(object):
    jsonmap = {
        'id' : 'id',
        'name' : 'name',
        'description' : 'description',
        'policyid' : 'policyid',
        'emailnotifications' : 'emailnotifications',
        'allowedunclassified' : 'allowunclassified',
        'safesearch' : 'safesearch'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def create_customer_policy(self, account_id, policy_name, policy_description, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Customer_Policies-PostRestapiUsersIdPolicies
        payload = {
            'id' : account_id,
            'name' : policy_name,
            'description' : policy_description
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/policies' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def delete_customer_policy(self, account_id, policy_id):
        #http://apidoc.webtitancloud.com/#api-Customer_Policies-DeleteRestapiUsersIdPoliciesPolicyid
        apiUrl = '/users/%s/policies/%s' %(account_id, policy_id)
        req = self.webtitan.query(apiUrl, method=requests.delete)
        return(req)

    def get_customer_policy(self, account_id, policy_id):
        #http://apidoc.webtitancloud.com/#api-Customer_Policies-GetRestapiUsersIdPoliciesPolicyid
        apiUrl = '/users/%s/policies/%s' %(account_id, policy_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_customer_nondefault_policies(self, account_id):
        #http://apidoc.webtitancloud.com/#api-Customer_Policies-GetRestapiUsersIdPolicies
        apiUrl = '/users/%s/policies' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def update_customer_policy(self, account_id, policy_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Customer_Policies-PostRestapiUsersIdPoliciesPolicyid
        payload = {
            'id' : account_id,
            'policyid' : policy_id
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/policies/%s' %(account_id, policy_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)