import pandas                   as pd
from utils.penhelp              import *
from reportlab.platypus         import Table, Paragraph
from reportlab.lib.styles       import ParagraphStyle
from reportlab.lib.enums        import TA_JUSTIFY

def bodySpaceCell2(width, height):
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

titleStyle = ParagraphStyle('title')
titleStyle.fontSize = 9
titleStyle.spaceAfter = 7

termsTxt = ParagraphStyle('termsTxt')
termsTxt.spaceAfter = 10
termsTxt.fontSize = 8.5
termsTxt.fontName = 'Helvetica'
termsTxt.leading = 10
termsTxt.alignment = TA_JUSTIFY

def _TermsParagraphList1():
    result = []

    title = Paragraph('<b>TÉRMINOS Y CONDICIONES GENERALES </b>', titleStyle)


    para1 = Paragraph('''
    <b>1. Partes: </b>Esta Orden de Compra se celebra entre la entidad de SENCINET que solicita el Servicio y/o Equipo y ha emitido la Orden de Compra (en adelante "SENCINET" o el "Contratante") y el Proveedor que va a proveer el Servicio y/o Equipo y a quien va dirigida la Orden de Compra (en adelante el "Proveedor" o el "Contratista"). SENCINET y el Proveedor se entenderán en adelante como las "Partes".
    ''', termsTxt)

    para2 = Paragraph('''
    <b>2. Formación de la Orden de Compra: </b>A menos que las Partes hayan suscrito un contrato de compra, a falta de éste, la Orden de Compra de SENCINET junto con estos Términos y Condiciones Generales constituyen el contrato entre las partes (en adelante el "Contrato"). SENCINET rechaza cualquier término o condición adicional o diferente a lo establecido en la Orden de Compra y estos Términos y Condiciones Generales. Se entiende que el Proveedor ha aceptado de manera tácita la Orden de Compra junto con estos Términos y Condiciones Generales.
    ''', termsTxt)

    para3 = Paragraph('''
    <b>3. Alcance de la Orden de Compra:</b> El Proveedor acuerda expresamente que proveerá los servicios y/o equipos establecidos en la Orden de Compra de conformidad con lo establecido en la Orden de Compra.
    ''', termsTxt)
    
    para4 = Paragraph('''
    <b>4. Obligaciones:</b> Será obligación de SENCINET: a) El pago oportuno al proveedor por servicios debidamente prestados y equipos debidamente suministrados y aceptados por SENCINET y/o el cliente de SENCINET (en adelante el "Cliente"), según la forma de pago establecida en esta Orden de Compra. 
    b) Facilitar la entrada a los sitios en donde se realizarán los Servicios. c) Cumplir la ley en todo momento. Será obligación del Proveedor: a) Realizar los Servicios conforme a los términos establecidos en esta Orden de Compra. b) Cumplir la ley en todo momento y mantener vigentes todos los permisos y las licencias que necesite para poder prestar los Servicios descritos en la presente Orden de Compra. c) Responder por todas las fallas, errores, negligencias, anomalías, inconsistencias suyas o de sus subcontratistas que se presenten en ejecución de esta Orden de Compra.  d) Cumplir oportunamente cualquiera de sus obligaciones de índole laboral (incluyendo salarios, prestaciones sociales e indemnizaciones). e) Proporcionar los comprobantes de pago en donde conste el cumplimiento de las obligaciones descritas en el punto 4 anterior en la periodicidad requerida por SENCINET. f) Dar cumplimiento a los requerimientos exigidos por SENCINET. g) Cumplir cualquier norma o reglamento interno de SENCINET o del Cliente, mientras realiza los Servicios. h) Preparar y entregar a SENCINET los informes que en cualquier tiempo solicite SENCINET. Dichos informes podrán ser compartidos por SENCINET con su Cliente. i) El Proveedor deberá cumplir con todas las normas y políticas que, en materia de salud ocupacional, seguridad industrial, ecología, empleo a la comunidad y asuntos públicos y comunidades, se tienen establecidas en la legislación del país o que establezcan SENCINET y/o el Cliente y le sean comunicadas previamente por SENCINET. j) Al finalizar la Orden de Compra, El Proveedor y sus subcontratistas deberán anexar una certificación del revisor fiscal en la que conste el cumplimiento de las obligaciones laborales y tributarias en relación con la ejecución de esta Orden de Compra. k) El Proveedor está obligado a prevenir y evitar cualquier situación que pudiera acarrear un conflicto de intereses entre el Cliente o SENCINET y el Proveedor. El Proveedor se compromete a no recibir o pagar honorarios, recompensas, comisiones o
    ''', termsTxt)


    result.append(title)
    result.append(para1)
    result.append(para2)
    result.append(para3)
    result.append(para4)
    return result

def _TermsParagraphList2():
    result = []

    para5 = Paragraph('''
    dádivas a cualquier representante, empleado, subcontratista o familiar del cualquier representante, empleado o subcontratista del Cliente o SENCINET. l) En caso de que el proveedor vaya a realizar trabajos en alturas el personal del CONTRATISTA deberá estar certificada en trabajo en alturas por la entidad autorizada para esto. m) Todos los elementos de protección personal que use el Proveedor para la prestación de los Servicios se deberán encontrar en buen estado y de solicitarlo SENCINET deberán contar con la certificación y controles del fabricante para garantizar que se encuentran en buen estado y que son aptos para uso. n) Responder por cualquier daño a las instalaciones o bienes de SENCINET o el Cliente, ocasionado por el personal del Proveedor. o) Actuar durante la vigencia de la presente Orden de Compra en forma responsable y diligente. p) Dar cumplimiento a la política de anticorrupción y soborno de SENCINET y cualquier ley o norma local aplicable. q) Responder por cualquier daño a las instalaciones o bienes de SENCINET o terceros, ocasionado por el personal del Proveedor. r) Informar a SENCINET tan pronto tenga conocimiento, la existencia de errores en el diseño de los Equipos. s) Proporcionar los manuales de instalación, uso y mantenimiento y demás documentación relevante y necesaria respecto de los Equipos. EL Proveedor en este acto autoriza a SENCINET (o su Cliente en caso de que el Cliente sea el usuario final) para que distribuya, copia y revele dicha documentación
    ''', termsTxt)

    para6 = Paragraph('''
    <b>5. Valor y Forma de pago:</b> a) El valor acordado en la Orden de Compra es el total a pagar por SENCINET y cubre la totalidad de gastos y costos incurridos por SENCINET para la prestación de los Servicios y/o Equipos. b) Salvo que se establezca algo diferente en la Orden de Compra, SENCINET pagará al Proveedor por los Servicios efectivamente prestados y Equipos suministrados y aceptados por SENCINET, mes vencido dentro de los sesenta (60) días calendario siguientes a la presentación de la factura correspondiente en las oficinas de SENCINET. Dichas facturas deberán ir acompañadas de los reportes de la labor realizada debidamente firmados por el funcionario que SENCINET haya designado para ello. c) En caso de que los precios se establezcan en moneda diferente a la moneda local, el proveedor facturará a SENCINET en moneda local utilizando la tasa representativa del mercado que certifique el gobierno local o quien haga sus veces en la fecha de facturación. d) Los precios de los equipos se establecen en la Orden de Compra. Salvo que en la Orden de Compra se estipule algo diferente, los precios son precios DDP (Delivery Duty Paid – INCOTERMS 2010) en el lugar que se especifique en la Orden de Compra.
  ''', termsTxt)

    para7 = Paragraph('''
    <b>6. Fuerza Mayor Caso Fortuito:</b> a) Las partes deberán cumplir con todas las obligaciones derivadas de esta Orden de Compra. En caso de incumplimiento de cualquiera de estas, la parte incumplida incurrirá en responsabilidad, salvo que el incumplimiento sea producto de fuerza mayor o caso fortuito debidamente comprobado. b) Cuando alguna de las partes se vea afectada por circunstancias constitutivas de fuerza mayor o caso fortuito que le impidan o demoren el cumplimiento de esta Orden de Compra, lo comunicará por escrito a la otra, anexando prueba siquiera sumaria de la ocurrencia del hecho constitutivo de fuerza mayor o caso fortuito. Una vez el hecho sea comunicado, las Partes decidirán mutuamente, si es necesario suspender de los términos de la presente Orden de Compra o cambiar los términos de esta, para continuar con su ejecución.
    ''', termsTxt)

    result.append(para5)
    result.append(para6)
    result.append(para7)
    return result