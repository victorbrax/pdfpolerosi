from reportlab.platypus         import Table

def mainPag1(pdf, headerSpace, bodySpace, footerSpace, w, hList: list):
    mainTable = Table([
    [headerSpace(w, hList[0])],
    [bodySpace(w, hList[1])],
    [footerSpace(w, hList[2])],
    ],
    colWidths= w,
    rowHeights= hList
    )

    mainTable.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'red'), # Support Grid
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])

    mainTable.wrapOn(pdf, 0, 0)
    mainTable.drawOn(pdf, 0, 0)
    return