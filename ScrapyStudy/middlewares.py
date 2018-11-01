import random

from ScrapyStudy.user_agents import agents

"""中间件，可以添加下载中过程一些配置，需要在设置文件setting中配置还起作用"""


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)  # 随机获取一个请求头
        request.headers["User-Agent"] = agent

# class CookiesMiddleware(object):
#     """ 换Cookie """
#
#     def process_request(self, request, spider):
#         cookie = random.choice(cookies)
#         request.cookies = cookie
