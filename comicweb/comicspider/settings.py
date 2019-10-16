#coding=utf-8

rules=[
    {
        "domain":'163.bilibili.com',
        'chapter-selector':''
    },
    {
        "domain":'www.shenmanhua.com',
        'chapter-selector':'#topic1 li a'
    },
    {
        "domain":'ac.qq.com',
        'chapter-selector':'.chapter-page-all a'
    }

]

def getRule(url):
    for rule in rules:
        if rule.get('domain') in url:
            return rule
    return None

# print getRule('https://manhua.163.com/source/4316808070150070932')