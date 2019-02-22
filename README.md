# webtitancloudapi-py

This small project is just a python API that queries the rest API for the WebTitan DNS filtering solution. This page will be updated in the future after I've finished all the APIs to configure categories, users, locations, etc...


## APIs

UsersAPI
LocationsAPI
GlobalBlacklistAPI
GlobalWhitelistAPI
CloudKeyAPI
DefaultPolicyAPI
CategoryAPI
SystemStatsAPI
CustomerStatsAPI
PolicyAPI
InternalUsersAPI

## UsersAPI

### create_account(account_name, account_email, account_license, account_password, **kwargs)

Used to create an account in the WebTitan Portal
- account_name : Name for the WebTitan Account
- account_email : Email address used for login and email notifications
- account_license : Local license number that needs to be unique between accounts
- account_password : Account password

### delete_account(account_id)

Used to delete an account in the WebTitan Portal
- account_id : Account ID that relates to the account

### get_account(account_id)

Used to return specific information about the users account (eg. id, license etc..)
- account_id : Account ID that relates to the account

### get_all_account

Used to get all accounts that are configured within the WebTitan Portal. This will only return accounts that you have access to (eg. Global Admin will return ALL accounts, whereas specific accounts will only return nested accounts that they have created)

### update_account(account_id, **kwargs)

Used to update the account (such as password, license, email etc...)
- account_id : Account ID that relates to the account

## LocationsAPI

### create_location(account_id, location_type, location_name, **kwargs)

Used to create a location for a specific user account (eg. Static IP location so the public IP address has permission to query the DNS server)
- account_id : Account ID that relates to the account
- location_type : Type of location such as staticip, dynamicip, etc... (find via the WebTitan Restful API documentation)
- location_name : Name of the location is required when creating a new location...

### delete_location(account_id, location_type, location_id)

Used to delete a location for a specific user account
- account_id : Account ID that relates to the account
- location_type : Location type needs to be specified (eg. staticip, dynamicip)
- location_name : Name of the location is also required to delete it

### get_user_location(account_id, location_type, location_id)

Used to get details of a specific type of location assoicated to the WebTitan account
- account_id : Account ID that relates to the account
- location_type : Location type needs to be specified
- location_id : Location ID that relates to the location

### get_user_locations(account_id, location_type)

Used to get details of all locations of a specific type associate to the WebTitan account
- account_id : Account ID that relates to the account
- location_type : Location type needs to be specified (By default, this is 'staticip' if not passed)

### update_location(account_id, location_type, location_id. **kwargs)

Used to update a specific location assosicated to the WebTitan account
- account_id : Account ID that relates to the account
- location_type : Location type needs to be specified
- location_id : Location ID that relates to the location

## GlobalBlacklistAPI

### create_global_blacklist(domain)

Used to create a global blacklist entry that affects all accounts
- domain : Example: bbc.co.uk or google.com

### delete_global_blacklist(blacklist_id)

Used to delete a global blacklist entry
- blacklist_id : Blacklist ID that relates to the Blacklist entry

### get_global_blacklist(blacklist_id)

Used to get details of a specific global blacklist entry
- blacklist_id : Blacklist ID that relates to the Blacklist entry

### list_global_blacklist_entries

Used to get every global Blacklist entry configured in WebTitan

### update_global_blacklist_entry(blacklist_id, **kwargs)

Used to update a specific global Blacklist entry
- blacklist_id : Blacklist ID that relates to the Blacklist entry
- kwargs can be found when listing the global blacklist (eg. incude subdomains...)

## GlobalWhitelistAPI
### create_global_whitelist_entry(domain)

Used to create a global whitelist entry that affects all accounts
- domain : Example: bbc.co.uk or google.com

### delete_global_whitelist_entry(whitelist_id)

Used to delete a global whitelist entry
- whitelist_id : Whitelist ID that relates to the Whitelist entry

### get_global_whitelist_entry(whitelist_id)

Used to get details of a specific global whitelist entry
- whitelist_id : Whitelist ID that relates to the Whitelist entry

### list_global_whitelist_entries

Used to get every global Whitelist entry configured in WebTitan

### update_global_whitelist_entry(whitelist_id, **kwargs)

Used to update a specific global Whitelist entry
- whitelist_id : Whitelist ID that relates to the Whitelist entry
- kwargs can be found when listing the global whitelist (eg. include subdomains...)

## CloudKeyAPI

### create_cloud_key(account_id, **kwargs)

Used to create a cloud key for the specific WebTitan user
- account_id : Account ID that relates to the account

### delete_cloud_key(account_id, cloudkey_id)

Used to delete a cloud key for the specific WebTitan user
- account_id : Account ID that relates to the account
- cloudkey_id : Cloudkey ID that relates to the Cloudkey

### get_user_cloudkey(account_id, cloudkey_id)

Used to get specific details about a specific cloudkey
- account_id : Account ID that relates to the account
- cloudkey_id : Cloudkey ID that relates to the Cloudkey

### get_user_cloudkeys(account_id)

Used to list all details about a users cloudkey
- account_id : Account ID that relates to the account

## DefaultPolicyAPI

### get_default_specific_filtercategory(categoryid)

Used to get specific details on a filter category that exist in the default policy
- categoryid : Category ID that relates to the specific Category (can be found via get_default_filtering_policy_categories())

### get_default_filtering_policy

Used to get specific details about the policy itself (not categories) such as: safesearch enabled? Email notificiations enabled?

### get_default_filtering_policy_categories

Used to get all categories of the default filtering policy
