"""中间件，可以添加下载中过程一些配置，需要在设置文件setting中配置还起作用"""
import random
import time

from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException

from ScrapyStudy.public.Log import Log
from ScrapyStudy.user_agents import agents

log = Log().get_logger()


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        log.info(spider.name)
        # agent = random.choice(agents)  # 随机获取一个请求头
        # request.headers["User-Agent"] = agent


# class CookiesMiddleware(object):
#     """ 换Cookie """
#
#     def process_request(self, request, spider):
#         cookie = random.choice(cookies)
#         request.cookies = cookie

class SeleniumMiddleware(object):
    """ 抓取js动态生成代码中间件 Selenium"""

    def process_request(self, request, spider):
        # log.info(spider.name)
        try:
            spider.driver.get(request.url)  # 驱动网页，很耗时
            # spider.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        except TimeoutException as e:
            log.info('加载网页超时')
        time.sleep(2)
        return HtmlResponse(url=spider.driver.current_url, body=spider.driver.page_source,
                            encoding="utf-8", request=request)
