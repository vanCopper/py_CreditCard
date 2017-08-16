#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/8/15'

from cards import merchants_bank
from cards import spd_bank
import dominate
from dominate.tags import *

html_temp = u'''
<div class="templatemo-content-widget white-bg">
                <!--<i class="fa fa-times"></i>-->
                <div class="media">
                  <div class="media-left">
                      <img class="media-object" src="../images/%s" alt="Sunset">
                  </div>
                  <div class="media-body">
                    <a href="%s">
                      <h2 class="media-heading text-uppercase">%s</h2>
                    </a>
                    <p>发布日期/到期日期：%s</p>
                  </div>
                </div>
              </div>'''
if __name__ == '__main__':

    while True:
        html_f = open('temp.html', 'r')
        html_t = html_f.read()
        # 招商银行
        m_data = merchants_bank.get_promotions()
        save_html = ''
        for item in m_data:
            save_html += html_temp % (item.get('type')+'.jpg', item.get('url'), item.get('title'), item.get('date'))
        f = open('html/merchants_bank.html', 'w')
        html_final = html_t % ('active','','', '招商银行信用卡中心',save_html.encode('utf-8'))
        f.write(html_final)
        f.flush()
        f.close()

        # 浦发银行
        spd_data = spd_bank.get_promotions()
        save_html = ''
        for item in spd_data:
            save_html += html_temp % (item.get('type')+'.png', item.get('url'), item.get('title'), item.get('date'))
        f = open('html/spd_bank.html', 'w')
        html_final = html_t % ('', 'active', '', '浦发银行信用卡中心', save_html.encode('utf-8'))
        f.write(html_final)
        f.flush()
        f.close()
        print 'running...'
        import  time
        time.sleep(86400)
