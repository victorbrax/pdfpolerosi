from reportlab.platypus         import Table
from utils.penhelp              import *
import pandas                   as pd

def bodySpaceCell1(width, height):
    # Main Sizes
    widthList = [
        width * 5 / 100, # Left Padding
        width * 40 / 100, # Left Column
        width * 50 / 100, # Right Column
        width * 5 / 100, # Right Padding
    ]

    heigthList = [
        height * 25 / 100, 
        height * 12 / 100,  
        height * 12 / 100, 
        height * 19 / 100, 
        height * 32 / 100, 

    ]

    res = Table([
        ['', _initialTableData(), _soldToTable(), ''],
        ['', _mainPoTable(), ''],
        ['', _itemInfoTable(), ''],
        ['', '', _totalsTable(), ''],
        ['', '', '', ''],
    ], widthList, heigthList)

    res.setStyle([
        # General
        # ('GRID', (0, 0), (-1, -1), 1, 'RED'), # Support Help

        ('LEFTPADDING', (0, 0), (-1, -1), 0),   # Zero Padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),  # Zero Padding
        ('TOPPADDING', (0, 0), (-1, -1), 0),    # Zero Padding
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0), # Zero Padding

        # Initial Table 
        ('ALIGN', (1, 0), (2, 0), 'CENTER'),
        ('VALIGN', (1, 0), (2, 0), 'MIDDLE'),

        # Poor Tables
        ('TOPPADDING', (1, 1), (2, 2), 5),
        ('LEFTPADDING', (1, 1), (2, 2), 5),
        ('VALIGN', (1, 1), (2, 2), 'TOP'),
        ('ALIGN', (1, 1), (2, 2), 'LEFT'),
        
        ('SPAN', (1, 1), (2, 1)),
        
        ('SPAN', (1, 2), (2, 2)),
        
        # Bottom Table
        # ('SPAN', (1, 3), (2, 3)),
        ('ALIGN', (1, 3), (2, 3), 'CENTER'),
        ('VALIGN', (1, 3), (2, 3), 'TOP'),
    ])
    return res

def _initialTableData(): # With Pandas
    data = [
     ['Order', ''],
     ['Order Date', ''],
     ['Supplier Name', ''],
     ['Supplier Country', ''],
]
    df = pd.DataFrame(data=data)
    df.columns = df.loc[0] # Get header
    df = df.drop(0) # Drop it

    res = [df.columns.tolist()] # To save columns
    res.extend(df.values.tolist()) # To save values

    widthList = [90, 130]
    res = Table(res, widthList, 15)

    res.setStyle([
        ('GRID', (0, 0), (-1, -1), 1, 'BLACK'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, 8), senciblue),
        ('TEXTCOLOR', (0, 0), (0, 8), 'white'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
      
    ])
    return res

def _soldToTable():
    widthList = [35, 195]

    res = Table([
        ['Sold To', 'SENCINET LATAM BRASIL LTDA'],
        ['', 'BRAZIL'],
        ['', 'RODOVIA JORNALISTA FRANCISCO AMORATO'],
        ['', 'AGUIRRE PROENCA KM 9'],
        ['', 'S/N'],
        ['', 'CHACARAS ASSAY'],
        ['', '13186-904'],
        ['', 'SP'],
        ['', 'HORTOLANDIA'],
        ['', '7428025600013'],
    ], widthList, 10)

    res.setStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1) , 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1) , 0),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
    ])
    return res

def _itemInfoTable():
    widthList = [
        40, # LINE
        160, # ITEM
        85, # PRICE
        60, # QT
        60, # ORDERED
        ]

    res = Table([
        ['Line', 'Item', 'Price', 'Quantity', 'Ordered'],
        ['1', 'B', 'C','D', 'E'],
        ['', 'XXXX-X', '','', ''],
    ], widthList, 15)

    res.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'WHITE'), # General
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),

    ('BACKGROUND', (0, 0), (6, 0), senciblue), # First Header
    ('FONTNAME', (0, 0), (6, 0), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 0), (6, 0), 'white'),
    ])
    return res

def _mainPoTable():
    widthList = [
        85, # SUPPLIER NUMBER
        70, # PAYMENTS TERMS
        50, # FOB
        100, # SHIPPING METHOD
        ]

    res = Table([
        ['Supplier Number', 'Payment Terms', 'FOB', 'Shipping Method'],
        ['A', 'B', 'C', 'D'],
        ['','Contact', ''],
        ['', 'JOAO GOMES', ''],
        ['', 'joao.gomes@sencinet.com'],
    ], widthList, 15)

    res.setStyle([
        ('ALIGN', (0, -1), (0, -1), 'RIGHT'),
        ('VALIGN', (0, -1), (0, -1), 'MIDDLE'),
      
        ('GRID', (0, 0), (-1, -1), 1, 'RED'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),

        ('BACKGROUND', (0, 0), (3, 0), senciblue), # First Header
        ('FONTNAME', (0, 0), (3, 0), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (3, 0), 'WHITE'),

        ('SPAN', (1, 2), (3, 2)), # Second Header
        ('SPAN', (0, 3), (3, 3)), # Name
        ('SPAN', (0, 4), (3, 4)), # E-mail
        
        ('BACKGROUND', (0, 2), (3, 2), senciblue), # Second Header
        ('FONTNAME', (0, 2), (3, 2), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 2), (3, 2), 'WHITE'),

        ('FONTNAME', (1, 3), (1, 3), 'Helvetica-Bold'),
        ('VALIGN', (1, 3), (1, 3), 'TOP'),
    ])
    return res

def _totalsTable():
    data = [ # Estes dados irão vir do Excel
    ['Total', 'XX'],
]
    widthList = [70, 100]

    res = Table(data, widthList, 16)

    res.setStyle([
    ('GRID', (0, 0), (-1, -1), 1, 'WHITE'),

    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('FONTNAME', (0, 1), (1, 1), 'Helvetica'),
    ('ALIGN', (1, 0), (1, 1), 'RIGHT'),
    
    ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 0), (0, 0), 'WHITE'),
    ('BACKGROUND', (0, 0), (0, 0), sencilightblue), 
    
    ('FONTNAME', (0, 0), (0, 1), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0, 0), (0, 1), 'WHITE'),
    ('BACKGROUND', (0, 1), (0, 1), senciblue),
    ])
    return res