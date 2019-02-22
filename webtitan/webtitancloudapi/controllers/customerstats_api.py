from webtitancloudapi.webtitan import webtitanAPI
import requests

class CustomerStatsAPI(object):
    customer_stats_mapper = {
        'id' : 'id',
        'type' : 'type',
        'date' : 'date',
        'start' : 'start',
        'end' : 'end',
        'limit' : 'limit'
        }

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def get_customer_overview(self, account_id):
        #http://apidoc.webtitancloud.com/#api-Customer_Stats-GetRestapiUsersIdStatsDate
        apiUrl = '/users/%s/stats' %(account_id)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_customer_top_categories(self, account_id, category_type):
        #http://apidoc.webtitancloud.com/#api-Customer_Stats-GetRestapiUsersIdStatsCategoriesTypeDate
        apiUrl = '/users/%s/stats/categories/%s' %(account_id, category_type)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_customer_top_domains(self, account_id, domain_type):
        #http://apidoc.webtitancloud.com/#api-Customer_Stats-GetRestapiUsersIdStatsDomainsTypeDate
        apiUrl = '/users/%s/stats/domains/%s' %(account_id, domain_type)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)

    def get_customer_top_users(self, account_id, user_type):
        #http://apidoc.webtitancloud.com/#api-Customer_Stats-GetRestapiUsersIdStatsUsersTypeDate
        apiUrl = '/users/%s/stats/users/%s' %(account_id, user_type)
        req = self.webtitan.query(apiUrl, method=requests.get)
        return(req)