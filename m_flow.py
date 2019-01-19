#!/usr/bin/python3

from openpyxl import *

''' warning때문에 코드가 돌다 멈추는 경우가 있어서 warning ignore 설정 '''
import warnings
warnings.filterwarnings("ignore")

'''
함수화가 필요할 지 모르겠지만 일단 한다면..!
def edit_data(bbook, edate, estr):
    ### bbook : bankbook / edate : edit date / estr : edit string
'''    

#파일 이름
FName = 'Test.xlsx' 
doc = load_workbook(FName)

#추후에 하드코딩부분 변경(입력)
month=1     
SName = '지출관리_'+str(month)+'월'
sheet = doc.get_sheet_by_name(SName)

bbook = {'525073':3, 'N돌핀통장':4, '신한_입출금':7, 'cma RP':9, '우리_모바일':10, '세이프박스':12, '카카오페이':14}
#수정하려는 날짜+8, 역시 하드코딩부분 변경(입력)
edate = 30 
#코드 상으로는 여러줄 입력 가능. 여러줄 입력을 받아올 수 있을지가...
estr = '''Test Text Editing


=>10000'''  

#통장종류 하드코딩부분 변경(변수,입력)
sheet.cell(bbook['신한_입출금'],edate,value=estr)   

doc.save(FName)



'''
이렇게 문서를 읽은 상태에서
    1. 통장 종류 선택하면 row가 지정이 되고 (code FIN, html -)
    =>input type radio / 셀렉트박스
    2. 기본으로 오늘 날짜를 계산하되,       (code -, html -)
       날짜를 선택할 수 있게 해서 날짜가 지정되면
       column도 지정이 됨                   (code FIN, html -)
    => input type text(value 오늘 날짜, 수정가능) / 셀렉트박스
    3. "추가"할 문자열을 입력하면           
    => input type text, 함수에 값 전달(여기서부터 openpyxl) (함수 미정)
    4. 지정된 row,column cell에 문자열이 추가됨(code FIN)
    5. 변경된 엑셀 파일을 저장                  (code FIN, html -)
    => 저장 버튼!
    
    +++ 엑셀 파일을 browser에서 display 할 수 있을지?
    +++ 한다면 어떻게 display할 지?

    +++ sheet 이름도 '지출관리_1월'으로 하드코딩해놨지만
        월 선택을 하면 건드리는 시트도 달라지도록 추가 수정 필요!
'''
