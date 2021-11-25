import requests
import json

# 鉄道遅延情報のjsonサイトからデータを取得
url =  "https://tetsudo.rti-giken.jp/free/delay.json"
delay_data = json.load("20211125.json")

# WEB_HOOK_URLはSlackの設定で準備で発行したURLを設定
WEB_HOOK_URL = "https://hooks.slack.com/services/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"
"
"""
requests.post(WEB_HOOK_URL,json.dumps)

#print (delay_data)
"""


print (delay_data)
print(type(delay_data))
print (delay_data[1])
