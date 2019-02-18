from webtitancloudapi.webtitan import webtitanAPI
import requests

class GlobalWhitelistAPI(object):
    jsonmap = {
        'domain':'domain',
        'subdomains':'subdomains',
        'log_requests':'log_requests',
        'comment':'comment',
        'whitelistid':'whitelistid',
        'whitelist':'whitelist',
        'offset':'offset',
        'limit':'limit'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def create_global_whitelist_entry(self, domain, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Globalwhitelist-PostRestapiWhitelist
        payload = {
            'domain': domain
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/whitelist'
        req = self.webtitan.query(apiUrl, method = requests.post, data=payload, json_handle=False)
        return(req)

    def delete_global_whitelist_entry(self, whitelist_id):
        #http://apidoc.webtitancloud.com/#api-Globalwhitelist-DeleteRestapiWhitelistWhitelistid
        apiUrl = '/whitelist/%s' %(whitelist_id)
        req = self.webtitan.query(apiUrl, method=requests.delete)
        return(req)

    def get_global_whitelist_entry(self, whitelist_id):
        #http://apidoc.webtitancloud.com/#api-Globalwhitelist-GetRestapiWhitelistWhitelistid
        apiUrl = '/whitelist/%s' %(whitelist_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def list_global_whitelist_entries(self, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Globalwhitelist-GetRestapiWhitelist
        apiUrl = '/whitelist'
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    #Import function not created yet

    def update_global_whitelist_entry(self, whitelist_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Globalwhitelist-PostRestapiWhitelistWhitelistid
        payload = {
                'whitelistid' : whitelist_id
            }
        apiUrl = '/whitelist/%s' %(whitelist_id)
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)
