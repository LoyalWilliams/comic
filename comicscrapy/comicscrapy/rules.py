#coding=utf-8


# 规则样例，都是统一采用xpath
# {
#     "domain":'163.bilibili.com',
#     'author-selector':'',
#     'name-selector':'',
#     'intr-selector':'',
#     'cover-selector':'',
#     'comic_url-selector':'',
#     'comic_type-selector':"",
#     'comic_type2-selector':'',
#     'collection-selector':'',
#     'recommend-selector':'',
#     'praise-selector':"",
#     'roast-selector':"",
#     'last_update_chapter-selector':'',
#     'last_update_time-selector':'',
#     'status-selector':"",
# }

rules=[
    {
        "domain":'163.bilibili.com',
        'comic_type-selector':"//dl[contains(@class,'sr-dl')]/dd[2]/a/text()",
        'praise-selector':"//dl[contains(@class,'sr-dl')]/dd[3]/span/text()",
        'roast-selector':"//dl[contains(@class,'sr-dl')]/dd[4]/span/text()",
        'status-selector':"//dl[contains(@class,'sr-dl')]/dd[1]/a[1]/text()",
    },
    {
        "domain":'www.shenmanhua.com',
        'author-selector':"//div[contains(@class,'jshtml')]//li[3]/text()",
        'name-selector':"//div[contains(@class,'jshtml')]//li[1]/text()",
        'cover-selector':"//div[contains(@id,'offlinebtn-container')]//img/@data-url",
        'comic_type-selector':"//div[contains(@class,'jshtml')]//li[4]/text()",
        'last_update_chapter-selector':"//div[contains(@class,'jshtml')]//li[2]/a/text()",
        'last_update_time-selector':"//div[contains(@class,'jshtml')]//li[5]/text()",
        'status-selector':"//div[contains(@class,'jshtml')]//li[2]/text()",
        'intr-selector':"//div[contains(@class,'jshtml')]//div[contains(@class,'wz')]/div[last()]/text()",
    },
    {
        "domain":'ac.qq.com',
        'author-selector':"//div[contains(@class,'works-intro-text')]/p/span[contains(@class,'first')]/em/text()",
        'name-selector':"//div[contains(@class,'works-intro-text')]/div/h2/strong/text()",
        'intr-selector':"//div[contains(@class,'works-intro-text')]/p[2]/text()",
        'cover-selector':"//div[contains(@class,'works-cover')]/a/img/@src",
        'collection-selector':'//*[@id="coll_count"]/text()',
        'roast-selector':"//div[contains(@class,'works-intro-text')]/p/span[2]/em/text()",
        'last_update_chapter-selector':'//*[@id="chapter"]/div[1]/ul/li[2]/a/text()',
        'last_update_time-selector':'//*[@id="chapter"]/div[1]/ul/li[2]/span[2]/text()',
        'status-selector':"//div[contains(@class,'works-cover')]/label[contains(@class,'works-intro-status')]/text()",
    },

]

def getRule(url):
    for rule in rules:
        if rule.get('domain') in url:
            return rule
    return None