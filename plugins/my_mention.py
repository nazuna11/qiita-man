# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import urllib.parse

@respond_to('.*教えて')
def mention_func(message):
    print(message.body["text"])
    target_word = urllib.parse.quote(message.body["text"].replace("教えて",""))
    message.reply(f'ググれや https://qiita.com/search?utf8=%E2%9C%93&sort=&q={target_word}') # メンション

@listen_to('教えて')
def listen_func(message):
    print(message.body["text"])
    target_word = urllib.parse.quote(message.body["text"].replace("教えて",""))
    message.reply(f'ググれや https://qiita.com/search?utf8=%E2%9C%93&sort=&q={target_word}')                           # メンション
