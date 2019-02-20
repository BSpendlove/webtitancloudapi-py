from webtitancloudapi.webtitan import webtitanAPI
import requests

class DefaultPolicyAPI(object):
    jsonmap = {
        'id':'categoryid',
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

    def get_default_filtering_policy(self):
        #http://apidoc.webtitancloud.com/#api-Default_Policy-GetRestapiDefaultpolicy
        apiUrl = '/defaultpolicy'
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)