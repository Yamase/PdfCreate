from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser

def m2i(m):
    return m/25.4*72

def i2m(i):
    return i/72*25.4

#源真ゴシック
GEN_SHIN_GOTHIC_MEDIUM_TTF ="./fonts/genshingothic-20150607/GenShinGothic-Monospace-Medium.ttf"

#白紙を作る
#ページサイズは1/72インチで定義される　つまりタプルの数値/72*25.4 mmになる
FILENAME = 'HelloWorld2.pdf'
testpage = (m2i(210), m2i(297))
c = canvas.Canvas(FILENAME, pagesize=portrait(testpage))

#フォント登録
pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_MEDIUM_TTF))
font_size =20
c.setFont('GenShinGothic', font_size)

#真ん中に文字列描画
width, height = A4
c.drawCentredString(width/2, height/2 - font_size*0.4, 'こんにちは、世界')
c.drawString(m2i(100), m2i(100), u'100x100に配置')

#Canvasに書き込み
c.showPage()
c.save()

webbrowser.open(FILENAME)