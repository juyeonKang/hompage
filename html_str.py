#<!-- html 코드 temp -->

def make_str():
    text = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="ContentType" content='text/html; charset=utf-8'/>
    <meta charset="UTF-8"/>
    <link href="http://fonts.googleapis.com/earlyaccess/jejugothic.css" rel="stylesheet">

    <style>
    h1{font-size:3em;text-align:center;}
    .date{
        font-size:2em; 
        font-family:"Jeju Gothic",sans-serif;
        line-height:1em;
        text-align:center;
    }
    .grid-container{
        display:grid;
        grid:10em 10em 10em 10em / auto 70% auto; 
        background-color:white;
    }
    .button{
        background-color:#54494b;
        margin:1.3% 0px;
        border:none;
        color:#f1f7ed;
        border-radius:12px;
        width:100%;
        text-align:center;
        text-decoration:none;
        font-size:3em;
        font-family:"Jeju Gothic", sans-serif;
        line-height:3em; 
        cursor:pointer;
    }

    </style>
    </head>
    
    <body>
    <h1>Personal page</h1>

    <div>
    <form class=form action="/bankbook" accept-charset="utf8" method="post">
    날짜:
    <input name="date" type="date" id="currentDate"/>
      |
    <input name="i/o" type="radio" value="income"/>수입
    <input name="i/o" type="radio" value="outcome"/>지출
      |
    금액:
    <input name="price" type=text"/>
    <br><br>
    내용:
    <input name="content" type="text"/>
      |
    <select name="type">
        <option value="">type</option>
        <option value="수입">수입</option>
        <option value="금융">금융</option>
        <option value="공금">공금</option>
        <option value="식비">식비</option>
        <option value="간식">간식</option>
        <option value="카페">카페</option>
        <option value="이벤트">이벤트</option>
        <option value="경조비">경조비</option>
        <option value="교통비">교통비</option>
        <option value="의료비">의료비</option>
        <option value="미용">미용</option>
        <option value="여가">여가</option>
        <option value="유흥">유흥</option>
        <option value="자기개발">자기개발</option>
        <option value="기타">기타</option>
    </select>
      |
    <select name="TBtype">
        <option value="">결제수단</option>
        <option value="card">카드</option>
        <option value="cash">현금</option>
        <option value="b_525073">계좌_525073</option>
        <option value="b_cma">계좌_CMA RP</option>
        <option value="b_위비">계좌_위비</option>
        <option value="b_신한">계좌_신한</option>
        <option value="b_세이프박스">계좌_세이프박스</option>
        <option value="b_수협">계좌_수협</option> 
       <option value="적_스무살">스무살적금</option>
        <option value="적_kia">KIA 적금</option>
        <option value="적_두산">두산 적금</option>
        <option value="적_수협">수협 적금</option>
        <option value="b_302">N돌핀통장</option>
    </select>
    <br><br>
    <input type="submit" value="ENTER">
    </form>
    <script>
    document.getElementById('currentDate').value = new Date().toISOString().substring(0, 10);
    </script>
    <!-- 날짜입력 참고링크 : https://hianna.tistory.com/319?category=706939 -->
    </div>
    <br><br><br>

    <div class="grid-container">
        <div></div>
        <a href='yas_link' class="button">익뚜의 야스</a>
        <div></div>

        <div></div>
        <div class="date">
        <strong style=letter-spacing:0.05em; line-height:1.5em; font-size:1.35em;>yas_title</strong><br>yas_date</div>
        <div></div>

        <div></div>
        <a href='saya_link' class="button">육아부부의 사야이</a>
        <div></div>

        <div></div>
        <div class="date">
        <strong style=letter-spacing:0.05em; line-height:1.5em; font-size:1.35em;>saya_title</strong><br>saya_date</div>
        <div></div>

        <div></div>
        <a href='https://www.boannews.com' class="button">보안뉴스</a>
        <div></div>        
    </div>
    </body>
    </html> 
    """
    return (text) 

def make_str_back():
    str = """
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
        <input type="button" value="뒤로가기" onclick="history.back(-1);">
    </body>
    </html>
"""
    return str
