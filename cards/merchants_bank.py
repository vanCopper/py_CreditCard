#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 招商银行
__mtime__ = '2017/8/15'

import requests
import json
r_url = 'http://cc.cmbchina.com/SvrAjax/PromotionChange.ashx?city=021&type=specialsale'
p_url = 'http://cc.cmbchina.com'
def get_promotions():
    r = requests.get(r_url)
    s_list = []
    if r.status_code == 200:
        json_str = r.text[1:-1]
        json_str = json_str.replace('result','"result"')
        json_str = json_str.replace('totalRecord','"totalRecord"')
        json_str = json_str.replace('list','"list"')
        json_str = json_str.replace('LinkUrl','"LinkUrl"')
        json_str = json_str.replace('Title','"Title"')
        json_str = json_str.replace('LinkFlag','"LinkFlag"')
        json_str = json_str.replace('Area','"Area"')
        json_str = json_str.replace('IsHot','"IsHot"')
        json_str = json_str.replace('IsNew','"IsNew"')
        json_str = json_str.replace('Date','"Date"')
        s_data = json.JSONDecoder().decode(json_str)

        for item in s_data.get('list'):
            obj = {}
            obj['type'] = 'merchants_bank'
            obj['title'] = item.get('Title')
            obj['date'] = item.get('Date')
            obj['url'] = p_url + item.get('LinkUrl')
            s_list.append(obj)
    return s_list
