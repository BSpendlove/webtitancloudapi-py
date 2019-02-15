from webtitancloudapi.webtitan import webtitanAPI
import requests

class LocationsAPI(object):
    jsonmap = {
        'id':'id',
        'type':'type',
        'ip':'ip',
        'name':'name',
        'hostname':'hostname',
        'tag':'tag'}
        

    def __init__(self, webtitan=None):
        if webtitan:
            self.webtitan = webtitan
        else:
            self.webtitan = webtitanAPI()

    def create_location(self, account_id, location_type, location_name, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Locations-CreateLocation
        payload = {
            'id' : account_id,
            'type' : location_type,
            'name' : location_name
            }

        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/locations/%s' %(account_id, location_type)
        req = self.webtitan.query(apiUrl, method = requests.post, data=payload, json_handle=False)
        return(req)

    def delete_location(self, account_id, location_type, location_id):
        #http://apidoc.webtitancloud.com/#api-Locations-DeleteLocation
        apiUrl = '/users/%s/locations/%s/%s' %(account_id, location_type, location_id)
        req = self.webtitan.query(apiUrl, method=requests.delete)
        return(req)
    
    def get_user_location(self, account_id, location_type, location_id):
        #http://apidoc.webtitancloud.com/#api-Locations-GetLocation
        if not location_type:
            location_type = 'staticip'

        apiUrl = '/users/%s/locations/%s/%s' %(account_id, location_type, location_id)
        req = self.webtitan.query(apiUrl, method = requests.get)

    def get_user_locations(self, account_id, location_type=None):
        #http://apidoc.webtitancloud.com/#api-Locations-GetLocations
        if not location_type:
            location_type = 'staticip'
            
        apiUrl = "/users/%s/locations/%s" %(account_id, location_type)
        req = self.webtitan.query(apiUrl, method = requests.get)
        return(req)

    def update_location(self, account_id, location_type, location_id, **kwargs):
        #http://apidoc.webtitancloud.com/#api-Locations-UpdateLocation
        payload = {
            'id': account_id,
            'type': location_type,
            'locationid': location_id
            }

        payload.update(self.webtitan.payloadBuilder(self.jsonmap, **kwargs))
        apiUrl = '/users/%s/locations/%s/%s' %(account_id, location_type, location_id)
        req = self.webtitan.query(apiUrl, method = requests.post, data=payload, json_handle=False)
        return(req)
