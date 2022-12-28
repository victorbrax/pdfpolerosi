from reportlab.lib.pagesizes    import A4
from reportlab.platypus         import Table
from reportlab.lib              import colors

width, height = A4 # The A4 paper is considered a tuple for ReportLab (w, h)

# Main Size
# Defining the percentages of how much we want for each part
heightList = [ 
    height * 13 / 100, # Header
    height * 84 / 100, # Body
    height *  3 / 100, # Footer
]

# Pallete
senciblue = colors.HexColor('#0A617E')
sencilightblue = colors.HexColor('#4b9bb6')
offwhite = colors.HexColor('#e1e1e1')

# Page No. Central
def pageNo(pdf):
    pageNo = pdf.getPageNumber()
    x = width * 92 / 100
    y = height * 1.25 / 100

    pdf.setFontSize(8)
    pdf.setFillColor('white')
    pdf.drawString(x, y, f'{pageNo}')

    return

# Pen Toolkit 
def drawCoordinates(pdf):
    pdf.setFont('Helvetica', 9)
    pdf.drawString(100,810, 'x100')
    pdf.drawString(150,810, 'x150')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(250,810, 'x250')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(350,810, 'x350')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(450,810, 'x450')
    pdf.drawString(500,810, 'x500')
    pdf.drawString(550,810, 'x550')

    pdf.drawString(10,50, 'y50')
    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,150, 'y150')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,250, 'y250')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,350, 'y350')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,450, 'y450')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,550, 'y550')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,650, 'y650')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,750, 'y750')
    pdf.drawString(10,800, 'y800') 
    pdf.drawString(10,850, 'y850') 

def Hello_World():
    return 'Thank you, God.'