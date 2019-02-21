from webtitancloudapi.webtitan import webtitanAPI
import requests

class DefaultPolicyAPI(object):
    jsonmap = {
        'categoryid':'categoryid',
        'offset':'offset',
        'limit':'limit',
        'allowed':'allowed',
        'notify':'notify',
        'emailnotifications':'emailnotifications',
        'allowunclassified':'allowedunclassified', #Boolean
        'safesearch':'safesearch' #String ON or OFF... could of been a boolean at least... ;)
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def get_default_specific_filtercategory(self, categoryid):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-GetRestapiDefaultpolicyCategoriesCategoryid
        apiUrl = '/defaultpolicy/categories/%s' %(categoryid)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_default_filtering_policy(self):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-GetRestapiDefaultpolicy
        apiUrl = '/defaultpolicy'
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_default_filtering_policy_categories(self):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-GetRestapiDefaultpolicyCategories
        apiUrl = '/defaultpolicy/categories'
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def update_default_specific_filtercategory(self, categoryid, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-PostRestapiCategoriesCategoryid
        payload = {'id' : categoryid}
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/categories/%s' %(categoryid)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def update_default_filtering_policy(self, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-PostRestapiDefaultpolicy
        payload = {}
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/defaultpolicy'
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)

    def update_all_default_filtercategories(self, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-PostRestapiDefaultpolicyCategories
        payload = {}
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/defaultpolicy/categories'
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)