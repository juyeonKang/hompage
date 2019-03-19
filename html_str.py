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
