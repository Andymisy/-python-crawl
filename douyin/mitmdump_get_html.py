import json
from save_to_mongo import save_user_data
from save_to_mongo import save_share_id

#利用mitmdump监听获取想要的用户数据
def response(flow):
    if 'aweme/v1/user/follower/list' in flow.request.url:
        resp = flow.response

        for user in json.loads(resp.text)['followers']:
            user_info = {}
            user_info['nickname'] = user['nickname']
            user_info['share_id'] = user['uid']
            user_info['signature'] = user['signature']
            user_info['douyin_ID'] = user['short_id']

            #获取到的share_id单独存放一个数据表中
            save_share_id(user_info['share_id'])
            #获取到的用户信息存放另一个表中
            save_user_data(user_info)


