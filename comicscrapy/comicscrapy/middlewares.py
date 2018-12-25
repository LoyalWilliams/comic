#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

from settings import USER_AGENTS

# 随机的User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", useragent)
