from datetime import timedelta
from datetime import datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

 
FACEBOOK_CLIENT_ID = '<your client id>'
FACEBOOK_CLIENT_SECRET = '<your client secret>'
FACEBOOK_ACCESS_TOKEN = '<your access token>'
FACEBOOK_ACCOUNT_ID = '<your account id>'

 
def get_campaign_statistics_for_day(date, account_id):
    date_string = date.strftime("%Y-%m-%d")

    ad_account = AdAccount(account_id)

    ###################### fields = 열(기본값:성과) https://developers.facebook.com/docs/marketing-api/insights/parameters/v15.0 ######################
    # account_name (광고 계정 이름)
    # campaign_name (캠페인명)
    # campaign_id
    # adset_name (광고세트명)
    # adset_id
    # ad_name (소구명)
    # ad_id
    # clicks (클릭)
    # reach (도달: 노출과 달리 중복 포함x)
    # impressions (노출)
    # spend (지출금액 추정)
    # actions (ex 참여 클릭 전환 등) https://developers.facebook.com/docs/marketing-api/reference/ads-action-stats/
    ## cpc (클릭당 평균 비용(전체))
    ## cpm (1,000회 노출에 대한 평균 비용)
    ## cpp (1,000명에게 도달하는 평균 비용 추정)
    ## ctr (클릭률 > 노출 대비 클릭)
    fields = [
    'campaign_name',
    'adset_name',
    'ad_name',
    'clicks',
    'reach',
    'impressions',
    'spend',
    ]

    ###################### params = 매게변수 https://developers.facebook.com/docs/marketing-api/insights/parameters/v15.0 ######################

    params = {
    ###################### breakdowns = 분석데이터 https://developers.facebook.com/docs/marketing-api/insights/breakdowns ######################
    # 자주 사용 되는 데이터
    # gender (성별)
    # Publisher_platform (노출 플랫폼) 
    # platform_position (노출 위치) 
    # device_platform (플랫폼 및 기기)
    # ad_format_asset, age, app_id, body_asset, call_to_action_asset, country, description_asset, gender, image_asset, mmm, place_page_id, 
    # impression_device, is_conversion_id_modeled, link_url_asset, product_id, region, skan_campaign_id, skan_conversion_id, 
    # title_asset, video_asset, dma, frequency_value, hourly_stats_aggregated_by_advertiser_time_zone, hourly_stats_aggregated_by_audience_time_zone,
    'breakdowns':['device_platform'],

    ###################### time_range = 시간 범위 #########################
    'time_range': {
        'since': date_string,
        'until': date_string
        # 'since': "2022-01-18",
        # 'until': "2022-01-18"
    },

    # 'lever': 'ad', 'adset', 'campaign', 'account'
    'level': 'ad',

    # 각 광고에 대해 반환되는 최대 제품 ID 수
    'limit': 100000
    }

    ad_insights = ad_account.get_insights(fields, params)

    # do whatever you want with the statistics in JSON format
    print(ad_insights) 

    return ad_insights

 
if __name__ == '__main__':

    FacebookAdsApi.init(FACEBOOK_CLIENT_ID, FACEBOOK_CLIENT_SECRET, FACEBOOK_ACCESS_TOKEN)

    facebook_account_id = f'act_{FACEBOOK_ACCOUNT_ID}'

    my_date = (datetime.now() - timedelta(1))

    get_campaign_statistics_for_day(my_date, facebook_account_id)
