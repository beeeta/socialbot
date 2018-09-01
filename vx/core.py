"""
从文件传输助手接收指令，对需要自动回复的群会话进行管理
"""
import os,json

from wxpy import *


cur_dir = os.path.dirname(__file__)

USE_DESC = """
使用说明：
bili......
"""

status_template = """已被托管的会话有：
{} """

FILE_HELPER = 'filehelper'


bot = Bot(cache_path='login_cache')

@bot.register(msg_types=TEXT)
def abc(msg):
    # 如果是指令
    if msg.sender.name == FILE_HELPER:
        if msg.text == 'ls':
            # show in ctrl rooms
            file_path = os.path.join(cur_dir, 'status.json')
            with open(file_path, 'r', encoding='utf-8') as f:
                status_js = json.loads(f.read())
                msg.reply(status_template.format(status_js.get('list', '')))
        try:
            index = msg.text.index(' ')
            pre_ct = msg.text[:index]
            suf_ct = msg.text[index + 1:]
            _handler_rooms(msg,pre_ct, suf_ct)
        except ValueError:
            logging.warning('input command message:%s format error' % msg.text)
            msg.reply('input command message:%s format error, the correct is [up/down] [target user or group id]'
                            % msg.Content, toUserName=FILE_HELPER)


def _handler_rooms(msg, pre_ct, suf_ct):
    contacts = bot.search()
    if not contacts:
        logging.warning('find no chats by name %s' % suf_ct)
        msg.reply('find no chats by name %s' % suf_ct, toUserName=FILE_HELPER)
    else:
        contacts = [(ct, ct.__class__.__name__) for ct in contacts]

    if pre_ct == 'up':
        pass
    elif pre_ct == 'down':
        pass