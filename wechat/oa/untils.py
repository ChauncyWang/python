import hashlib

from wechat.oa import config


def validate_token(web_input, token=config.token):
    """
    对请求进行验证,判断是否为微信客户端的请求
    :param web_input: 请求参数
    :param token: token 码,要和公众号平台设置的一致
    :return: 验证成功返回请求的 echostr 参数
    """
    if len(web_input) == 0:
        return "Hello,this is token validation page!"
    print("token 验证中...")
    signature = web_input.signature
    timestamp = web_input.timestamp
    nonce = web_input.nonce
    echostr = web_input.echostr
    # 进行加密(按 token timestamp nonce 字典排序连接成字符串,然后 对字符串进行 sha1 加密)
    validate = [token, timestamp, nonce]
    validate.sort()
    validate = "".join(validate)
    sha1 = hashlib.sha1(validate.encode("UTF8"))
    hashcode = sha1.hexdigest()

    if hashcode == signature:
        print("验证成功!")
        return echostr
    else:
        print("验证失败!")
        return ""
