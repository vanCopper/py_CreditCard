#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 浦发银行
__mtime__ = '2017/8/16'
import requests
import json
r_url = 'http://ccc.spdb.com.cn/was5/web/search'
def get_promotions():
    s_list = []
    post_data = {'metadata':'relTime|Link|title', 'channelid':225958, 'pageSize':20, 'page':1, 'searchword':''}
    r = requests.post(r_url, post_data)
    if r.status_code == 200:
        result = json.JSONDecoder().decode(r.text)
        for item in result.get('rows'):
            obj = {}
            obj['type'] = 'spd_bank'
            obj['title'] = item.get('title')
            obj['date'] = str(item.get('relTime').encode('utf-8')).split(' ')[0]
            obj['url'] =  item.get('Link')
            s_list.append(obj)

    return s_list


if __name__=='__main__':
    get_promotions()
