import smtplib
from email.mime.text import MIMEText

# Configurar los detalles del servidor de correo electrónico
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'otiniano.guille@gmail.com'
smtp_password = 'Otidagui12'

# Crear un mensaje de correo electrónico
msg = MIMEText('Este es un mensaje de prueba.')

msg['Subject'] = 'Informe de candidatos'
msg['From'] = 'otiniano.guille@gmail.com'
msg['To'] = 'karina.elizabeth@gmail.com'

# Conectar al servidor de correo electrónico y enviar el mensaje
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, msg['To'], msg.as_string())
    server.quit()
    print('Correo electrónico enviado exitosamente')
except Exception as e:
    print('Error al enviar el correo electrónico:', str(e))