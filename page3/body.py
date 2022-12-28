import pandas                   as pd
from utils.penhelp              import *
from reportlab.platypus         import Table, Paragraph
from reportlab.lib.styles       import ParagraphStyle
from reportlab.lib.enums        import TA_JUSTIFY

def bodySpaceCell3(width, height):
    # Main Sizes
    widthList = [
        width * 5 / 100, # Left Padding
        width * 42 / 100, # Left Column
        width * 6 / 100, # Center Column
        width * 42 / 100, # Right Column
        width * 5 / 100, # Right Padding
    ]

    heigthList = [
        height * 6 / 100,  # Top Padding
        height * 88 / 100, # Content
        height * 6 / 100,  # Bottom Padding
    ]

    res = Table([
        ['', '', '', '', ''],
        ['', _TermsParagraphList1(), '', _TermsParagraphList2(), ''],
        ['', '', '', '', ''],
    ], widthList, heigthList)

    res.setStyle([
        # ('GRID', (0, 0), (-1, -1), 1, 'RED'), # Support Help

        ('LEFTPADDING', (1, 0), (-1, -1), 0),   # Zero Padding
        ('RIGHTPADDING', (1, 0), (-1, -1), 0),  # Zero Padding
        ('TOPPADDING', (1, 0), (-1, -1), 0),    # Zero Padding
        ('BOTTOMPADDING', (1, 0), (-1, -1), 0), # Zero Padding
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ])
    return res

termsTxt = ParagraphStyle('termsTxt')
termsTxt.spaceAfter = 10
termsTxt.fontSize = 8.5
termsTxt.fontName = 'Helvetica'
termsTxt.leading = 10
termsTxt.alignment = TA_JUSTIFY

def _TermsParagraphList1():
    result = []

    para1 = Paragraph('''
    <b>7. Terminación de la Orden de Compra: </b>Serán causales de terminación de la Orden de Compra: a) La finalización de esta, por cumplimiento de las obligaciones, el objeto y el plazo contenido en esta Orden de Compra. b) El mutuo acuerdo de las partes, en cuyo caso no habrá lugar a indemnización a favor de ninguna. c) La decisión unilateral de SENCINET, en cualquier momento, mediante comunicación escrita con 30 días de antelación. Si SENCINET decide terminar esta Orden de Compra, deberá cancelar al Proveedor el valor de los Servicios debidamente prestados hasta la fecha de terminación sin lugar a indemnización o cargos adicionales de terminación. d) El incumplimiento grave e injustificado de esta Orden de Compra de cualquiera de las PARTES. Se entenderá por incumplimiento grave e injustificado de SENCINET, el atraso en el pago de dos meses de servicio de forma consecutiva, sin ninguna justificación ni acción. El incumplimiento grave e injustificado del proveedor se entenderá como el incumplimiento de cualquier obligación bajo la presente Orden de Compra y los atrasos en los plazos establecidos en la presente Orden de Compra, sin ninguna causal de exoneración. e) La terminación por cualquier causa de esta Orden de Compra entre SENCINET y el Cliente.
    ''', termsTxt)

    para2 = Paragraph('''
    <b>8. Confidencialidad: </b>Toda la información que se llegue a compartir, revelar o conocer en virtud de la relación comercial está sujeta a los términos de confidencialidad dispuestos en los Acuerdos de Confidencialidad y Contrato celebrado entre las Partes.
    ''', termsTxt)

    para3 = Paragraph('''
    <b>9. Cláusula Penal: </b>Si la Orden de Compra se resuelve o termina por incumplimiento de las obligaciones del Proveedor, éste deberá pagar a SENCINET el veinte por ciento (20%) del valor de la Orden de Compra a título de pena no compensatoria. EL Proveedor será responsable de pagar dicha pena y los perjuicios causados por su incumplimiento. SENCINET podrá demandar al Proveedor, junto con el pago de la pena, la indemnización de perjuicios causados. Para asegurar el pago de dicha pena, SENCINET podrá descontarlo de cualquier valor debido al Proveedor.
    ''', termsTxt)
    
    para4 = Paragraph('''
    <b>10. Legislación y Jurisdicción: </b>La Orden de Compra se regirá e interpretará de conformidad con las leyes del país donde se ejecute la Orden de Compra. Para la solución de toda clase de conflictos que se presenten a propósito del desarrollo, ejecución y terminación de la Orden de Compra, siempre y cuando no se tenga un contrato firmado, las partes se someterán a la jurisdicción de los jueces de tal país. 
    ''', termsTxt)
    
    para5 = Paragraph('''
    <b>11. 11. Personal del Proveedor: </b>a)El Proveedor declara para todos los efectos de esta Orden de Compra, que obra como contratista independiente y por tanto, no existirá relación laboral alguna entre SENCINET y el Proveedor, o el personal que éste utilice en la ejecución de la presente Orden de Compra, es el mismo patrono del personal encargado de prestar los Servicios por la cual le corresponden a el Proveedor, el pago de salarios, prestaciones sociales de toda índole y cualquier indemnización que, de acuerdo con leyes laborales, con los contratos de trabajo, pactos convenciones colectivas, corresponda o puedan corresponder a tal personal. Queda claramente entendido que. El Proveedor reembolsará a SENCINET cualquier valor que deba pagar SENCINET (incluyendo gastos de legales) en caso de que SENCINET deba asumir algún costo en relación de reclamaciones de personal del Proveedor a SENCINET o al Cliente. El 
    ''', termsTxt)

    result.append(para1)
    result.append(para2)
    result.append(para3)
    result.append(para4)
    result.append(para5)
    return result

def _TermsParagraphList2():
    result = []

    para6 = Paragraph('''
    reembolso deberá realizarse dentro de los treinta días calendarios siguientes a la notificación por parte de SENCINET. SENCINET bajo ningún concepto será responsable por daños o lesiones que sufran empleados o subcontratistas del Proveedor durante la ejecución de la presente Orden de Compra. b) SENCINET podrá solicitar al Proveedor la sustitución de cualquier funcionario suyo, incluidos los supervisores, que a su juicio no estuvieren cumpliendo adecuadamente con sus funciones. El requerimiento en tal sentido deberá formularse por escrito y deberá el Proveedor realizar la sustitución en el plazo máximo de quince (15) días siguientes a la fecha de requerimiento. c) El Proveedor garantiza que el personal y Subcontratistas que utilice para realizar los Servicios bajo la presente Orden de Compra será competente, apropiado y calificado y cumplirá con las expectativas de SENCINET. d) SENCINET se reserva el derecho de prohibir la entrada a personal del Proveedor al sitio de instalación o cualquier otro sitio en donde deban realizarse Servicios, cuando considere que dicho personal no es idóneo.
    ''', termsTxt)

    result.append(para6)
    return result