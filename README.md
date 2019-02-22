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

### update_default_specific_filtercategory(categoryid, **kwargs)

Used to update a specific category in the default policy (eg. Allow = True/False)
- categoryid : Category ID that relates to the specific Category

### update_default_filtering_policy

Used to update the default filtering policy

### update_all_default_filtercategories

Used to update every default filter category

## CategoryAPI

### get_specific_customer_policy_category(account_id, policy_id, category_id)

Used to get a specific custom policy category
- account_id : Account ID that relates to the account
- policy_id : Policy ID that relates to the custom Policy
- category_id : Category ID that relates to the specific category

### get_specific_customer_defaultpolicy_category(account_id, category_id)

Used to get specific category in the customers default policy
- account_id : Account ID that relates to the account
- category_id : Category ID that relates to the specific category

### get_specific_customer_policy_categories(account_id, category_id)

Used to get all categories in a specific custom policy
- account_id : Account ID that relates to the account
- category_id : Category ID that relates to the specific category

### get_specific_customer_defaultpolicy_categories(account_id)

Used to get all categories in the customers default policy
- account_id : Account ID that relates to the account

### update_specific_customer_policy_category(account_id, policy_id, category_id, **kwargs)

Used to update the specific category in a custom policy
- account_id : Account ID that relates to the account
- policy_id : Policy ID that relates to the custom Policy
- category_id : Category ID that relates to the specific category

### update_specific_customer_defaultpolicy_category(account_id, category_id, **kwargs)

Used to update the specific category in the customers default policy
- account_id : Account ID that relates to the account
- category_id : Category ID that relates to the specific category

### update_specific_customer_policy_allcategories(account_id, policy_id, **kwargs)

Used to update every category in the custom policy
- account_id : Account ID that relates to the account
- policy_id : Policy ID that relates to the custom Policy

### update_specific_customer_defaultpolicy_allcategories(account_id, **kwargs)

Used to update every category in the customers default policy
- account_id : Account ID that relates to the account

## SystemStatsAPI

### get_system_overview(**kwargs)

Used to get an overview of things such as total DNS requests, total domains allowed/blocked... Use kwargs from the Rest API documentation on apidoc.webtitancloud.com for optional parameters to filter on dates etc.. or get a date range

### get_system_top_categories(system_type)

Used to get top categories accessed
- system_type : Allowed, Blocked or Bypassed

### get_system_top_domains(system_type)

Used to get the top domains visited (can be filtered on date or date range)
- system_type : Allowed, Blocked or Bypassed

### get_system_top_users(system_type)

Used to get the top users (can be filtered on date or date range)
- system_type : Allowed, Blocked or Bypassed

## CustomerStatsAPI

### get_customer_overview(account_id)

Used to get an overview for a specific account/customer
- account_id : Account ID that relates to the account

### get_customer_top_categories(account_id, category_type)

Used to get top categories accessed by a specific customer
- account_id : Account ID that relates to the account
- category_type : Allowed/Blocked or Bypassed

### get_customer_top_domains(account_id, domain_type)

Used to get top domains visited by a specific customer
- account_id : Account ID that relates to the account
- domain_type : Allowed/Blocked or Bypassed

### get_customer_top_users(account_id, user_type)

Used to get top internal users in a specific account/customer
- account_id : Account ID that relates to the account
- user_type : Allowed/Blocked or Bypassed

## PolicyAPI
