from pymongo import MongoClient

#链接数据库
client = MongoClient(host='127.0.0.1', port=27017)
db = client.test

#share_id表
def save_share_id(share_id):
    table = db.douyin_share_id
    total_id = table.find({})
    if share_id not in total_id:
        user = {}
        user['share_id'] = share_id
        table.insert_one(user)

#用户信息表（有share_id，但没有粉丝数，点赞数）
def save_user_data(data):
    table = db.douyin_user
    #存储数据
    table.insert_one(data)

def get_id():
    table = db.douyin_share_id

    share_id = table.find_one_and_delete({})

    return share_id
#用户信息表（无share_id，但有粉丝数，关注数，点赞数）
def save_user_info(data):

    table = db.douyin_user_info
    table.insert_one(data)




