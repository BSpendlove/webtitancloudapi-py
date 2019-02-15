import webtitancloudapi
from pprint import pprint

api = webtitancloudapi.webtitanAPI('unitednet.webtitancloud.com',
                                   '4280225eaf4bdf241223aded7d4ec600',
                                   '2fd8e329c1c25fe11ef751d5ae3abd7b',
                                   '61e03ac87c78c623d660005a0e949f90',
                                   '426219c47998f19ae5807e82df3a6773', ssl_verify=False)

account_id = 1 #WebTitan Demo account
name = 'Testetsstst'
email = 'api@unitednet.co.uk'
user_lic = '100'
password = '5B7sr00iqH'

user_api = webtitancloudapi.UsersAPI(webtitan=api)
location_api = webtitancloudapi.LocationsAPI(webtitan=api)
globalblacklist_api = webtitancloudapi.GlobalBlacklistAPI(webtitan=api)
cloudkey_api = webtitancloudapi.CloudKeyAPI(webtitan=api)
systemstats_api = webtitancloudapi.SystemStatsAPI(webtitan=api)

 
pprint(user_api.get_all_accounts())
#pprint(user_api.create_account('APITester','api@unitednet.co.uk','10','pa55w0rD!'))
#pprint(location_api.update_location(1,'staticip',1,name='changednameviaapi'))
#pprint(cloudkey_api.get_user_cloudkey(1, 30))
#pprint(systemstats_api.get_system_top_users('allowed'))
#pprint(globalblacklist_api.update_global_blacklist_entry(17, comment='testapicomment'))