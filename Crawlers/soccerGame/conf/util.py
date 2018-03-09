#encoding=utf-8
from  lxml import html
from random import choice
from collections import defaultdict

def extractors(http_content):
    message_li = []
    xptah_obj = html.fromstring(http_content)
    em_list = xptah_obj.xpath('//div[@class="container margin_top_10 ovs"]/ div[1] / div[1] / div[2] / ul/li')
    print len(em_list)
    for li in em_list:
        try:
            import ipdb
            ipdb.set_trace()
            message_li.append(li.xpath("./text()")[0])
        except:
            pass
    return message_li

def soccer_hupu_extractors(http_content):
    message_list = list()
    message_dict = dict()
    xpath_obj = html.fromstring(http_content)
    soccer_info_list = xpath_obj.xpath('//ul[@class="calendar-con-items J_gameLists"]/li')
    for soccer_single_info in soccer_info_list:
        message_dict['title'] = soccer_single_info.xpath('./p[@class="gptop"]/text()')[0]
        message_dict['team_home'] = soccer_single_info.xpath('./div[@class="game_l"]/span[1]/a/text()')[0]
        message_dict['team_visiting'] = soccer_single_info.xpath('./div[@class="game_l"]/span[2]/a/text()')[0]
        have_result = soccer_single_info.xpath('./div[@class="game_r"]/span[@class="spt sp_top"]')
        if have_result:
            message_dict['result'] = soccer_single_info.xpath('./div[@class="game_r"]/span/text()')[0]
            message_dict['battlefield'] = soccer_single_info.xpath('./p[@class="gptop"]/a/@href')[0]
        else:
            message_dict['start_time'] = soccer_single_info.xpath('./div[@class="game_r"]/span/text()')[0]
            message_dict['prospect'] = soccer_single_info.xpath('./p[@class="gptop"]/a/@href')[0]
        message_list.append(message_dict)
    return message_list

def soccer_hupu_extractors_dict(http_content):
    message_list = http_content.get('result').get('data')
    print(len(http_content.get('result').get('data')))
    message_result_list = list()
    for message_singe_info in message_list:
        message_dict = dict()
        message_dict['赛程'] = message_singe_info.get('leagueDesc') + message_singe_info.get('lunDesc')
        message_dict['主队'] = message_singe_info.get('home_name')
        message_dict['客队'] = message_singe_info.get('away_name')
        message_dict['比赛时间'] = message_singe_info.get('startTime')
        message_dict['赛程状态'] = message_singe_info.get('endedDesc')
        if "已结束" in message_dict['赛程状态']:
            message_dict['比赛结果'] = str(message_singe_info.get('home_score')) + ':' + str(message_singe_info.get('away_score'))
        # message_singe_info['url_info'] =
        message_result_list.append(message_dict.copy())
    return message_result_list





def get_random_ua():
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)" ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400) ',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE) ',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E) ',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E) ',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0',
        'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    ]

    return choice(user_agents)