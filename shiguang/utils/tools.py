import uuid

import oss2

from utils.AliyunConf import *


# 上传二进制流文件到阿里云
def upload_to_ali(icon):
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth(AccessKeyId, AccessKeySecret)
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'http://oss-cn-beijing.aliyuncs.com', BucketName)
    # 随机图片名称
    filename = "shiguang/" + get_filename() + icon.name
    # icon.read() 二进制流文件
    result = bucket.put_object(filename, icon.read())

    icon_url = "https://wc-blog.oss-cn-beijing.aliyuncs.com/" + filename
    return result.status, icon_url


# 生成随机文件名
def get_filename():
    filename = uuid.uuid4()
    return str(filename)
