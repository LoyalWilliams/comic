#coding=utf-8

rules=[{
    "domain":'manhua.163.com',
    'chapter-selector':''
},

]

def getRule(url):
    for rule in rules:
        if rule.get('domain') in url:
            return rule
    return None

# print getRule('https://manhua.163.com/source/4316808070150070932')