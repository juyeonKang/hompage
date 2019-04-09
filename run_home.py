#!/usr/bin/python3

from bottle import route, run, request
from html_str import make_str
from feedparser import parse
import pymysql
from urllib.parse import unquote

@route('/')
def index():
    yas = parse('https://1boon.kakao.com/yas.atom')
    yas_link = yas['entries'][0]['link']
    yas_title = yas['entries'][0]['title']
    yas_date = yas['entries'][0]['published'][:8]+yas_link[-2:]
    saya = parse('https://1boon.kakao.com/saya.atom')
    saya_link = saya['entries'][0]['link']
    saya_title = saya['entries'][0]['title']
    saya_date = saya['entries'][0]['published'][:8]+saya_link[-2:]
    html_text = make_str()
    html_text = html_text.replace("yas_link",yas_link)
    html_text = html_text.replace("yas_title",yas_title)
    html_text = html_text.replace("yas_date",yas_date)
    html_text = html_text.replace("saya_link",saya_link)
    html_text = html_text.replace("saya_title",saya_title)
    html_text = html_text.replace("saya_date",saya_date)
    return html_text

@route('/bankbook', method='post')
def index():
    ### form 데이터 가져오기
    date = request.forms.get('date')
    FD=request.forms
    io = request.forms.get('i/o')
    tmp = request.forms.get('price')
    content = request.forms.get('content')
    content = content.encode('latin1').decode('utf-8')
    income=""
    outcome=""
    if(io=='income'):
        if (tmp[0]=='-'):
            income=tmp[1:]
        else:
            income=tmp
        string = """INSERT INTO %s
        (date, content, type, income) VALUES
        ('%s', '%s', '%s',"""+income+" );"
    else:
        if(tmp[0]!='-'):
            outcome='-'+tmp
        else:
            outcom=tmp
        string = """INSERT INTO %s
        (date, content, type, outcome) VALUES
        ('%s', '%s', '%s',"""+outcome+");"

    Type = request.forms.get('type')
    Type = Type.encode('latin1').decode('utf-8')
    table = request.forms.get('TBtype')
    table = table.encode('latin1').decode('utf-8')

    ### db control
    db = pymysql.connect(host="localhost",
                         user="ubuntu",
                         passwd="chemwriter1!",
                         db="bankbook")
    cursor=db.cursor()
    cursor.execute(string%(table,date,content,Type))
    db.commit()

    return 'test'

run(host='0.0.0.0', port=8080)
