from webtitancloudapi.webtitan import webtitanAPI
import requests

class CategoryAPI(object):
    jsonmap = {
        'id' : 'id',
        'policyid' : 'policyid',
        'categoryid' : 'categoryid',
        'offset' : 'offset',
        'limit' : 'limit',
        'allowed' : 'allowed',
        'notify' : 'notify'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def get_specific_customer_policy_category(self, account_id, policy_id, category_id):
        #http://apidoc.webtitancloud.com/#api-Categories-GetRestapiUsersIdPoliciesPolicyidCategoriesCategoryid
        apiUrl = '/users/%s/policies/%s/categories/%s' %(account_id, policy_id, category_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)
    
    def get_specific_customer_defaultpolicy_category(self, account_id, category_id):
        #http://apidoc.webtitancloud.com/#api-Categories-GetRestapiUsersIdPoliciesDefaultCategoriesCategoryid
        apiUrl = '/users/%s/policies/default/categories/%s' %(account_id, category_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_specific_customer_policy_categories(self, account_id, policy_id):
        #http://apidoc.webtitancloud.com/#api-Categories-GetRestapiUsersIdPoliciesPolicyidCategories
        apiUrl = '/users/%s/policies/%s/categories' %(account_id, policy_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_specific_customer_defaultpolicy_categories(self, account_id):
        #http://apidoc.webtitancloud.com/#api-Categories-GetRestapiUsersIdPoliciesDefaultCategories
        apiUrl = '/users/%s/policies/default/categories' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def update_specific_customer_policy_category(self, account_id, policy_id, category_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Categories-PostRestapiUsersIdPoliciesPolicyidCategoriesCategoryid
        payload = {
            'id' : account_id,
            'policyidid' : policy_id,
            'categoryid' : category_id
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/policies/%/categories/%s' %(account_id, policy_id, category_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def update_specific_customer_defaultpolicy_category(self, account_id, category_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Categories-PostRestapiUsersIdPoliciesDefaultCategoriesCategoryid
        payload = {
            'id' : account_id,
            'categoryid' : category_id
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/policies/default/categories/%s' %(account_id, category_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def update_specific_customer_policy_allcategories(self, account_id, policy_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Categories-PostRestapiUsersIdPoliciesPolicyidCategories
        payload = {
            'id' : account_id,
            'policyid' : policy_id
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/policies/%s/categories' %(account_id, policy_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def update_specific_customer_defaultpolicy_allcategories(self, account_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Categories-PostRestapiUsersIdPoliciesDefaultCategories
        payload = {'id':aaccount_id}
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/policies/default/categories' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)