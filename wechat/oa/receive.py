import xml.etree.ElementTree as ET


def parse_xml_msg(web_data):
    """
    从 web_data 返回的 xml 中解析 消息
    :param web_data:
    :return:
    """
    if len(web_data) == 0:
        return None
    xml_data = ET.fromstring(web_data)
    msg_type = xml_data.find("MsgType").text

    if msg_type == 'text':
        msg = TextMsg(xml_data)
        return msg
    elif msg_type == "image":
        pass


class Msg(object):
    """
    基本消息，所有消息都有的属性
    """
    def __init__(self, xml_data):
        self.ToUserName = xml_data.find('ToUserName').text
        self.FromUserName = xml_data.find('FromUserName').text
        self.CreateTime = xml_data.find('CreateTime').text
        self.MsgType = xml_data.find('MsgType').text
        self.MsgId = xml_data.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.Content = xml_data.find('Content').text

