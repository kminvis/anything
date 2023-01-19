from datetime import timedelta
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

 
FACEBOOK_CLIENT_ID = '<your client id>'
FACEBOOK_CLIENT_SECRET = '<your client secret>'
FACEBOOK_ACCESS_TOKEN = '<your access token>'
FACEBOOK_ACCOUNT_ID = '<your account id>'

 
            ######################################## 분석할 기간 ########################################
date_since = "2023-01-01"
date_until = "2023-01-19"

 
def get_campaign_statistics_for_day(account_id):
    ad_account = AdAccount(account_id)

    fields = [
    'ad_id',
    'campaign_name',
    'adset_name',
    'ad_name',
    'clicks',
    'reach',
    'impressions',
    'cpc',
    'spend'
    ]

    params = {
    'breakdowns':[
        'publisher_platform', 
        'platform_position', 
        'impression_device'
        ],

    'time_range': {
        'since': date_since,
        'until': date_until
    },

    'level': 'ad',

    'limit': 100000
    }

    first_ad_insights = ad_account.get_insights(fields, params)
    first_ad_list = []
    for first_insight in first_ad_insights:
        try:
            cpc = float(first_insight['cpc'])
            click = int(first_insight['clicks'])
            ######################################## 원하는 수식 설정 ########################################
            if cpc < 300 and click > 5:
                insight_data = {
                    '광고ID': first_insight['ad_id'],
                    '캠페인': first_insight['campaign_name'],
                    '광고세트': first_insight['adset_name'],
                    '클릭': first_insight['clicks'],
                    '도달': first_insight['reach'],
                    '노출': first_insight['impressions'],
                    'cpc': first_insight['cpc'],
                    '지출금액': first_insight['spend'],
                    '소구제목': first_insight['title_asset'],
                    '플랫폼': first_insight['publisher_platform'], 
                    '노출위치': first_insight['platform_position'], 
                    '노출기기': first_insight['impression_device'],
                }
                first_ad_list.append(insight_data)
        except:
            pass

    # 위 광고 성별 확인하기
    for first_ad in first_ad_list:
        first_ad['성별'] = gender(facebook_account_id, first_ad['광고ID'])

    best_ads = pd.DataFrame((first_ad_list))
    print(best_ads)
    
            ######################################## 엑셀로 저장하기 ########################################
    best_ads.to_excel(f'{date_since}-{date_until}.xlsx')




def gender(account_id, best_ad_id):
    ad_account = AdAccount(account_id)
    fields = [
    'ad_id',
    'clicks'
    ]

    params = {
    'breakdowns':['gender'],

    'time_range': {
        'since': date_since,
        'until': date_until
    },

    'level': 'ad',

    'limit': 100000
    }

    second_ad_insights = ad_account.get_insights(fields, params)
    
    male_ad_click = 0
    female_ad_click = 0
    for second_insight in second_ad_insights:
        if second_insight['ad_id'] == best_ad_id:
            if second_insight['gender'] == "male":
                male_ad_click = int(second_insight['clicks'])
            if second_insight['gender'] == "female":
                female_ad_click = int(second_insight['clicks'])
    if male_ad_click > female_ad_click:
        ad_gender = "male"
    else:
        ad_gender = "female"

    return ad_gender
    

if __name__ == '__main__':

    FacebookAdsApi.init(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, FACEBOOK_ACCESS_TOKEN)

    facebook_account_id = f'act_{FACEBOOK_ACCOUNT_ID}'

    get_campaign_statistics_for_day(facebook_account_id)
