from datetime import timedelta
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

 
FACEBOOK_CLIENT_ID = '<your client id>'
FACEBOOK_CLIENT_SECRET = '<your client secret>'
FACEBOOK_ACCESS_TOKEN = '<your access token>'

 
def get_campaign_statistics_for_day(date, account_id):
    date_string = date.strftime("%Y-%m-%d")

    ad_account = AdAccount(account_id)

    fields = [
    'account_name',
    'campaign_name',
    'campaign_id',
    'adset_name',
    'adset_id',
    'ad_name',
    'ad_id',
    'impressions',
    'clicks',
    'spend',
    'actions',
    'reach'
    ]

    params = {
    'breakdowns':['device_platform'],
    'time_range': {
        'since': date_string,
        'until': date_string
    },
    'level': 'ad',
    'limit': 100000
    }

    ad_insights = ad_account.get_insights(fields, params)

    # do whatever you want with the statistics in JSON format
    print(ad_insights) 

    return ad_insights

 

if __name__ == '__main__':

    FacebookAdsApi.init(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, FACEBOOK_ACCESS_TOKEN)

    facebook_account_id = 'act_<your account id>'

    my_date = (datetime.now() - timedelta(1))

    get_campaign_statistics_for_day(my_date, facebook_account_id)
