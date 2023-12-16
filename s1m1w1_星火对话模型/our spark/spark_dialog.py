import SparkApi
# import pandas as pd

# from tqdm import tqdm
# from read_data import *

# 以下密钥信息从控制台获取
appid = "f54bca1a"  # 填写控制台中获取的 APPID 信息
api_secret = "ZGJmMjY3YWFmNGY5N2Q1YWMwOGZlMjFh"  # 填写控制台中获取的 APISecret 信息
api_key = "2e7516edf376713eb5d99fc812a87ed5"  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“generalv2”
# domain = "generalv2"  # v2.0版本
domain = "plugin"  # v2.0版本

# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址

text = []


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


# if __name__ == '__main__':
#     prompt = ['']
#     text.clear
#     # instructions, inputs, outputs = read_json('./data_demo\school_math_0.25M.json')

#     datas, inputs, processes, res = read_csv1('data_demo\math23k_test_zh.csv')

#     output_ifly_COT = []
#     output_ifly = []
#     for input, process in tqdm(zip(inputs, processes)):
#         # print(input)
#         input = input.strip('\"')
#         query1 = input + '\n' + '只输出结果'
#         query2 = input + '\n' + process + '只输出结果'
#         question1 = checklen(getText("user", query1))
#         question2 = checklen(getText("user", query2))
#         # SparkApi.answer = ""
#         # print("星火: ", end="")
#         # SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question1)
#         # getText("assistant", SparkApi.answer)
#         # output_ifly.append(SparkApi.answer)

#         SparkApi.answer = ""
#         print("星火: ", end="")
#         SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question2)
#         getText("assistant", SparkApi.answer)
#         output_ifly_COT.append(SparkApi.answer)

#     # datas['Spark_outputs'] = output_ifly
#     datas['Spark_outputs_COT'] = output_ifly_COT
#     datas.to_csv('data_demo\math23k_test_zh.csv', index=False)


#     # for name in ['数学概念阐释', '数学题抽象', '数学题干改编', '题目纠错', '个性化推荐', '数学题干生成', '对比解题思路']:
#     #     datas, inputs, outputs = read_csv('data_demo\\'+ name +'.xlsx')
#     #     output_ifly_COT = []

#         # for input in tqdm(inputs):
#         #     Input = input
#         #     question = checklen(getText("user", Input))
#         #     SparkApi.answer = ""
#         #     print("星火: ", end="")
#         #     SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
#         #     getText("assistant", SparkApi.answer)
#         #     output_ifly.append(SparkApi.answer)

#     #     datas['Spark_outputs'] = output_ifly
#     #     datas.to_excel('data_demo\\'+ name +'.xlsx', index=False)

#     # with open('./data_demo/Spark.txt', 'w', encoding='utf-8') as f:
#     #     f.write('\n'.join(output_ifly))
if __name__ == '__main__':
    while (1):
        query = input("please ask:")
        question = checklen(getText("user", query))
        SparkApi.answer = ""
        print("星火: ", end="")
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        getText("assistant", SparkApi.answer)
