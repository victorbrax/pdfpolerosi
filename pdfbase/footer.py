from reportlab.platypus         import Table
from utils.penhelp              import *

def footerSpaceCell(width, height):
    text = 'Proprietary and Confidential'
    res = Table([[text]], width, height)
    res.setStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), senciblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), 'white'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])
    return res
