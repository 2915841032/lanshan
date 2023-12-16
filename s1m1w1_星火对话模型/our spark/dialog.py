import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
import os
import random
import time
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket  # 使用websocket_client

class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, Spark_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(Spark_url).netloc
        self.path = urlparse(Spark_url).path
        self.Spark_url = Spark_url

    # 生成url
    def create_url(self):
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.Spark_url + '?' + urlencode(v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url


# 收到websocket错误的处理
def on_error(ws, error):
    pass
    # print("### error:", error)


# 收到websocket关闭的处理
def on_close(ws,one,two):
    print(" ")


# 收到websocket连接建立的处理
def on_open(ws):
    thread.start_new_thread(run, (ws,))


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, domain= ws.domain,question=ws.question))
    ws.send(data)


# 收到websocket消息的处理
def on_message(ws, message):
    # print(message)
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        # print(content,end ="")
        global answer
        answer += content
        if status == 2:
            ws.close()


def gen_params(appid, domain, question):
    """
    通过appid和用户的提问来生成请参数
    """
    data = {
        "header": {
            "app_id": appid,
            "uid": "adm"
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "random_threshold": 0.5,
                "max_tokens": 2048,
                "auditing": "default"
            }
        },
        "payload": {
            "message": {
                "text": question
            }
        }
    }
    return data

def ask(history, text):
    appid = "e97d3136"
    api_key = "b25338415789cf13a0091d64a1b3381e"
    api_secret = "MDExMGZmZjFjMzRhOTkzNzczMGEyMzgw"
    Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"
    domain = 'generalv2'

    question = history
    question.append({"role": "user", "content": text})

    global answer
    answer = ''
    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    question.append({"role": "assistant", "content": answer})
    return question, answer

if __name__ == "__main__":
    folder_path=r'C:\Users\sounding.ai\Desktop\Spark_Demo-main\our spark\result'
    folder_path_zh=r'C:\Users\sounding.ai\Desktop\Spark_Demo-main\our spark\result_zh'
    txt_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

    for txt_file in txt_files:
        file_name = os.path.basename(txt_file)
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        question =[]
        print(txt_file)
        Input =content+'\n'+"请将这段文字翻译成中文"
        question, ans = ask(question, Input)
        print("星火: "+ans, end = "")
        # print(folder_path_zh+file_name)
        with open(folder_path_zh+'\\'+file_name, 'a', encoding='utf-8-sig') as f:
            f.write(str(ans))
        time.sleep(random.randint(3,8))



    '''
    history = [
        {"role": "user", "content": "我喜欢红色，记住。"},
        {"role": "assistant", "content": "你为什么喜欢这个颜色？"},
        {"role": "user", "content": "你还记得我喜欢什么颜色吗？告诉我。"},
        {"role": "assistant", "content": "根据你之前所说过的，你喜欢红色。 "},
    ]
    text = "谢谢你记得我喜欢的颜色，你知道它的反色是什么吗？"
    ans = ask(history, text)
    print(ans)
    '''

'''
if __name__ == "__main__":
    appid = '2b83817e'
    api_key = '6d20d9fd4cc1aa158ef824af5ea7a805'
    api_secret = 'YzgxZGQ1OWVjYTFlMzNmMTA0NTQ5MzVj'
    # Spark_url = 'wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/j4gql8f2m5m2_v1'
    Spark_url = 'wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/zyncaa3e2d9c_v1'
    domain = 'generalv2'

    # appid = "e97d3136"
    # api_key = "b25338415789cf13a0091d64a1b3381e"
    # api_secret = "MDExMGZmZjFjMzRhOTkzNzczMGEyMzgw"
    # Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"
    # domain = 'generalv2'
    # domain = 'plugin'

    # uid = "mingzhao5"

    # question = [
    #     {"role": "user", "content": "My name is White."},
    #     {"role": "assistant", "content": "Hello White, nice to meet you! How can I assist you today?"},
    #     {"role": "user", "content": "What's my name?"}
    # ]

    question = [
        {"role": "user", "content": "我喜欢白色，记住。"},
        {"role": "assistant", "content": "我完全理解你喜欢白色，这是一种很纯净、宁静的颜色。你还有其他喜欢的事物或者特别的记忆吗？我很愿意听你分享。"},
        {"role": "user", "content": "你还记得我喜欢什么颜色吗？告诉我。"}
    ]

    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = question
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
'''

'''
                [
                    {"role": "user", "content": "你是谁"} # 用户的历史问题
                    {"role": "assistant", "content": "....."}  # AI的历史回答结果
                    # ....... 省略的历史对话
                    {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
                ]
'''


