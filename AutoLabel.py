from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser

#インチ：メートル変換関数
def m2i(m):
    return m/25.4*72
def i2m(i):
    return i/72*25.4

#A-oneの26101をつかったラベル作成
def print_on26101(c, row, column, first_l, second_l = None, third_l = None, size = 5):
    '''A-oneの26101にラベルを印刷するための関数　英数半角で9文字を超える場合は2, 3行に分けたほうが良い'''
    font_size = size
    if first_l == None and second_l != None:
        first_l = second_l
        second_l = None

    if row > 11 or column > 7:
        print('Row or Column is overflow!')
        return

    #ラベル位置の指定
    x = m2i(17.5 + 13 * (column - 1))
    y = m2i(15.5 + 13 * (row - 1))

    if second_l == None and third_l == None:
        c.drawCentredString(x, y+0.4*font_size, first_l)
    elif third_l ==None:
        c.drawCentredString(x, y-0.2*font_size, first_l)
        c.drawCentredString(x, y + 0.9*font_size, second_l)
    else:
        c.drawCentredString(x, y - 0.7 * font_size, first_l)
        c.drawCentredString(x, y+0.4*font_size, second_l)
        c.drawCentredString(x, y + 1.5 * font_size, third_l)

def sheet_on26101(filename, printlist):
    '''printlistに辞書リストを渡す
    辞書リストには枚数, first_l, second_l, third_lを指定
    second_l以降は任意 あとは勝手にやってくれる
    ただし総数が60枚を超えるとエラー
    '''
    # 源真ゴシック
    GEN_SHIN_GOTHIC_MEDIUM_TTF = "./fonts/genshingothic-20150607/GenShinGothic-Monospace-Medium.ttf"

    # はがきサイズを作る
    testpage = (m2i(100), m2i(148))
    c = canvas.Canvas(filename, pagesize=portrait(testpage), bottomup=False)

    # フォント登録
    pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_MEDIUM_TTF))
    font_size = 5
    c.setFont('GenShinGothic', font_size)

    counter = 0
    for i in printlist:
        for j in range(i['num']):
            row = 1 + counter//6
            column = 1 + counter%6
            first_l = i['first_l']
            try:
                second_l = i['second_l']
            except KeyError:
                second_l = None
            try:
                third_l = i['third_l']
            except KeyError:
                third_l = None
            print_on26101(c,row, column, first_l, second_l, third_l)
            counter += 1
            if counter == 60:
                #60枚以上書き込んだら、新しいページに続ける
                c.showPage()
                pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_MEDIUM_TTF))
                font_size = 5
                c.setFont('GenShinGothic', font_size)
                counter = 0
    # Canvasに書き込み
    if counter != 0:
        c.showPage()
    c.save()

# #源真ゴシック
# GEN_SHIN_GOTHIC_MEDIUM_TTF ="./fonts/genshingothic-20150607/GenShinGothic-Monospace-Medium.ttf"
# #はがきサイズを作る
# FILENAME = 'test2.pdf'
# testpage = (m2i(100), m2i(148))
# c = canvas.Canvas(FILENAME, pagesize=portrait(testpage), bottomup=False)
# #フォント登録
# pdfmetrics.registerFont(TTFont('GenShinGothic', GEN_SHIN_GOTHIC_MEDIUM_TTF))
# font_size =5
# c.setFont('GenShinGothic', font_size)
# print_on26101(c, 1, 1, '200 ng/ul', 'mCherry', 'template')
# print_on26101(c, 1, 2, '200 uM', 'primer-F')
# print_on26101(c, 2, 1, '10x KOD', 'buffer')
# print_on26101(c, 2, 1, '10x KOD', 'buffer')
# print_on26101(c, 2, 2, '10x KOD', 'buffer')
# print_on26101(c, 2, 3, '10x KOD')
# #Canvasに書き込み
# c.showPage()
# c.save()
# webbrowser.open(FILENAME)
if __name__ == '__main__':
    printlist1 = (
        {'num': 16,
         'first_l': '10x KOD',
         'second_l': 'buffer',
         'third_l': None,
         },
        {'num': 16,
         'first_l': '2 mM',
         'second_l': 'dNTP',
         'third_l': None,
         },
        {'num': 16,
         'first_l': '25 mM',
         'second_l': 'MgSO4',
         'third_l': None,
         },
        {'num': 12,
         'first_l': '2 uM',
         'second_l': 'Forward',
         'third_l': 'primer',
         },
        {'num': 4,
         'first_l': '2 uM',
         'second_l': 'Forward',
         'third_l': 'primer',
         },
        {'num': 16,
         'first_l': '2 uM',
         'second_l': 'Reverse',
         'third_l': 'primer',
         },
        {'num': 9,
         'first_l': '200 pg/ul',
         'second_l': 'mCherry',
         'third_l': 'template',
         },
        {'num': 9,
         'first_l': '200 pg/ul',
         'second_l': 'mStrawberry',
         'third_l': 'template',
         },
        {'num': 9,
         'first_l': '200 pg/ul',
         'second_l': 'mOrange',
         'third_l': 'template',
         },
        {'num': 9,
         'first_l': '200 pg/ul',
         'second_l': 'EYFP',
         'third_l': 'template',
         },
        {'num': 4,
         'first_l': 'Loading',
         'second_l': 'buffer',
         'third_l': None,
         },
        {'num': 12,
         'first_l': 'Loading',
         'second_l': 'buffer',
         'third_l': None,
         },
        {'num': 16,
         'first_l': 'DNA',
         'second_l': 'ladder',
         'third_l': None,
         },
        {'num': 16,
         'first_l': '10x T4',
         'second_l': 'ligation',
         'third_l': 'buffer',
         },
        {'num': 16,
         'first_l': '変性',
         'second_l': 'バッファー',
         },
        {'num': 16,
         'first_l': 'タンパク質',
         'second_l': 'マーカー',
         },
        {'num': 16,
         'first_l': 'sfGFP',
         },
        {'num': 16,
         'first_l': '10 uM',
         'second_l': 'フルオレ',
         'third_l':'セイン',
         },
        {'num': 16,
         'first_l': '2% SDS',
         },
        {'num': 16,
         'first_l': '8M 塩酸',
         'second_l': 'グアニジン',
         },
    )
    sheet_on26101('LabelSet-Center.pdf', printlist1)
    webbrowser.open('LabelSet-Center.pdf')