#!/usr/bin/python3

from bottle import route, run
from html_str import make_str
from feedparser import parse

@route('/')
def index():
    t1, t2, t3, t4, t5 = make_str()
    yas = parse('https://1boon.kakao.com/yas.atom')
    yas_link = yas['entries'][0]['link']
    yas_title = yas['entries'][0]['title']
    yas_date = yas['entries'][0]['published'][:8]+yas_link[-2:]
    saya = parse('https://1boon.kakao.com/saya.atom')
    saya_link = saya['entries'][0]['link']
    saya_title = saya['entries'][0]['title']
    saya_date = saya['entries'][0]['published'][:8]+saya_link[-2:]
    html_text = t1+yas_link+t2+'<strong style=letter-spacing:0.05em;line-height:1.5em;font-size:1.35em;>'+yas_title+'</strong><br>'+yas_date+t3+saya_link+t4+'<strong style=letter-spacing:0.05em;line-height:1.5em;font-size:1.35em;>'+saya_title+'</strong><br>'+saya_date+t5
    return html_text


run(host='0.0.0.0', port=8080)
