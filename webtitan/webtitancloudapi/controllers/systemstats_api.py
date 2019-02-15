from webtitancloudapi.webtitan import webtitanAPI
import requests

class SystemStatsAPI(object):
    system_stats_mapper = {
        'date':'date',
        'start':'start',
        'end':'end'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def get_system_overview(self, **kwargs):
        #http://apidoc.webtitancloud.com/#api-System_Stats-GetRestapiStatsDate
        payload = {}

        payload.update(self.webtitan.payloadBuilder(self.system_stats_mapper, **kwargs))
        print(payload)
        apiUrl = '/stats'
        req = self.webtitan.query(apiUrl, method=requests.get, params=payload)
        return(req)
    
    def get_system_top_categories(self, system_type):
        #http://apidoc.webtitancloud.com/#api-System_Stats-GetRestapiStatsCategoriesTypeDate
        apiUrl = '/stats/categories/%s' %(system_type)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_system_top_domains(self, system_type):
        #http://apidoc.webtitancloud.com/#api-System_Stats-GetRestapiStatsDomainsTypeDate
        apiUrl = '/stats/domains/%s' %(system_type)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_system_top_users(self, system_type):
        #http://apidoc.webtitancloud.com/#api-System_Stats-GetRestapiStatsUsersTypeDate
        apiUrl = '/stats/users/%s' %(system_type)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)