import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ingreso import ingresar


def confirmacion_correo(correo):
    proveedor_correo = 'smtp.gmail.com: 587'
    remitente = 'losdeatras865@gmail.com'
    password = 'adsi86520'
    servidor = smtplib.SMTP(proveedor_correo)
    servidor.starttls()
    servidor.ehlo()
    servidor.login(remitente, password)
    mensaje = "<h1>creaste una una nueva cuenta en ADSI 865</h1>"
    msg = MIMEMultipart()
    msg.attach(MIMEText(mensaje, 'html'))
    msg['From'] = remitente
    msg['To'] = correo
    msg['Subject'] = 'papeleria los de atras'
    servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
    return ingresar()