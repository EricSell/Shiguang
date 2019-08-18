import random

from django.core.cache import cache
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from utils.Tencent_conf import *


def send_msg(phone_numbers):
    ssender = SmsSingleSender(appid, appkey)
    code = get_code()
    cache.set(phone_numbers, code, timeout=180)
    params = [code, 3]  # 当模板没有参数时，`params = []`
    try:
        result = ssender.send_with_param(86, phone_numbers,
                                         template_id, params, sign=sms_sign, extend="",
                                         ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
        return True
    except HTTPError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
        return False


# 随机验证码
def get_code():
    code = ""
    for i in range(4):
        code += str(random.choice(range(10)))
    return code
