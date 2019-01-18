#!/usr/bin/python3

from openpyxl import *

fileName = 'mflow.xlsx'
doc = load_workbook(fileName)
sheet = doc.get_sheet_by_name('지출관리_1월')

'''
이렇게 문서를 읽은 상태에서
    1. 통장 종류 선택하면 row가 지정이 되고
    =>input type radio / 셀렉트박스
    2. 기본으로 오늘 날짜를 계산하되,
       날짜를 선택할 수 있게 해서 날짜가 지정되면
       column도 지정이 됨
    => input type text(value 오늘 날짜, 수정가능) / 셀렉트박스
    3. "추가"할 문자열을 입력하면
    => input type text, 함수에 값 전달(여기서부터 openpyxl)
    4. 지정된 row,column cell에 문자열이 추가됨
    5. 변경된 엑셀 파일을 저장
    => 저장 버튼!
    
    +++ 엑셀 파일을 browser에서 display 할 수 있을지?
    +++ 한다면 어떻게 display할 지?

    +++ sheet 이름도 '지출관리_1월'으로 하드코딩해놨지만
        월 선택을 하면 건드리는 시트도 달라지도록 추가 수정 필요!
'''
