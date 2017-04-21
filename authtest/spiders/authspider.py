# -*- coding: utf-8 -*-

import scrapy
import logging

class authspider(scrapy.Spider):
    name = 'authspider'
    logger = logging.getLogger()
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'user_locale=zh-CN; remote_way=http',
        'Host':'git.oschina.net',
        'Origin':'https://git.oschina.net',
        'Referer':'https://git.oschina.net/login',
        
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    }
    def start_requests(self):
        yield scrapy.Request("https://git.oschina.net/login",callback = self.login_test)
    def login_test(self,response):
        self.logger.debug("start login")     
        token = response.xpath("//body/div[@class='ui grid page center aligned']/div[1]/div[1]/form/div/input[2]/@value").extract()[0]
        #每建立一次连接，都会生成一个token来表示用户身份
        self.logger.debug("token :"+token)
        yield scrapy.FormRequest.from_response(response,headers = self.headers,formdata={'user[login]':'15527519386@163.com',
                                                            'user[password]':'112358',
                                                                'authenticity_token':token},callback = self.after_login)
    def after_login(self,response):
        print response
    """description of class"""


