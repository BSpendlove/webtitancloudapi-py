from webtitancloudapi.webtitan import webtitanAPI
import requests

class GlobalBlacklistAPI(object):
    jsonmap = {
        'domain':'domain',
        'subdomains':'subdomains',
        'log_requests':'log_requests',
        'comment':'comment',
        'blacklistid':'blacklistid',
        'blacklist':'blacklist',
        'offset':'offset',
        'limit':'limit'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def create_global_blacklist_entry(self, domain, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Globalblacklist-PostRestapiBlacklist
        payload = {
            'domain': domain
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/blacklist'
        req = self.webtitan.query(apiUrl, method = requests.post, data=payload, json_handle=False)
        return(req)

    def delete_global_blacklist_entry(self, blacklist_id):
        #http://apidoc.webtitancloud.com/#api-Globalblacklist-DeleteRestapiBlacklistBlacklistid
        apiUrl = '/blacklist/%s' %(blacklist_id)
        req = self.webtitan.query(apiUrl, method=requests.delete)
        return(req)

    def get_global_blacklist_entry(self, blacklist_id):
        #http://apidoc.webtitancloud.com/#api-Globalblacklist-GetRestapiBlacklistBlacklistid
        apiUrl = '/blacklist/%s' %(blacklist_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    #Import blacklist entries- need to create some kind of JSON parser so it's easier to use for people that don't want to write domains in json...

    def list_global_blacklist_entries(self, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Globalblacklist-GetRestapiBlacklist
        apiUrl = '/blacklist'
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def update_global_blacklist_entry(self, blacklist_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Globalblacklist-PostRestapiBlacklistBlacklistid
        payload = {
                'blacklistid' : blacklist_id
            }
        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/blacklist/%s' %(blacklist_id)
        req = self.webtitan.query(apiUrl, method=requests.post, data=payload, json_handle=False)
        return(req)