from reportlab.platypus         import Table, Image
from utils.penhelp              import *

def headerSpaceCell(width, height):
    widthList = [
    width * 30 / 100, # Logotype
    width * 70 / 100, # PO Number
]

    logopath = 'images\Logo_vert.png' # SenciLogo
    logowidht = widthList[0]
    logo = Image(logopath, logowidht, 70, kind='proportional')

    res = Table([
        [logo, _poNumber(777774)]
        ], widthList, height)

    res.setStyle([
        # General
        # ('GRID', (0, 0), (-1, -1), 1, 'BLUE'), # Support Help

        ('ALIGN', (0, 0), (1, 0), 'CENTER'), 
        ('VALIGN', (0, 0), (1, 0), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (1, 0), 0),
        ('BOTTOMPADDING', (0, 0), (1, 0), 0), 
    
        # PO Text
        ('FONTNAME', (0, 0), (1, 0), 'Helvetica-Bold'),
    ])
    return res

def _poNumber(num):
    return f'PURCHASE ORDER {num}'
