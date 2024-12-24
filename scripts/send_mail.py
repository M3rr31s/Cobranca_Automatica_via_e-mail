import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class Send_mail:    
    def __init__(self, email_remetente='Email A Enviar',
                 senha_remetente='Senha E-mail A Enviar',
                 email_destinatarios=[],
                 titulo_email="Titulo Do Email",
                 corpo_email='Corpo Do Email a ser Enviado Formato HTML',
                 path_arquivos=None):
        
        self.cadastros = {
            'email_remetente': email_remetente,
            'senha_remetente': senha_remetente,
            'email_destinatarios': email_destinatarios,
            'titulo_email': titulo_email,
            'corpo_email': corpo_email,
            'path_arquivos': path_arquivos if path_arquivos else []
        }
        

    
    def __anexar_arquivos(self, email_msg):
        if self.cadastros['path_arquivos']:
            for file in self.cadastros['path_arquivos']:
                if os.path.isfile(file):
                    attachment = MIMEBase('application', 'octet-stream')
                    with open(file, 'rb') as f:
                        attachment.set_payload(f.read())
                        
                    encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition',
                                          f'attachment; filename={os.path.basename(file)}')
                    email_msg.attach(attachment)
                else:
                    print(f"Arquivos Não Encontrados : {file}")
                    
            
    def __envio_email(self):
        server_info = {
            'host': "smtp.gmail.com",
            'port': 587,
        }
        
        # Iniciar a conexão com o servidor
        server = smtplib.SMTP(server_info['host'], server_info['port'])
        server.ehlo()
        server.starttls()
        server.login(user=self.cadastros['email_remetente'], 
                     password=self.cadastros['senha_remetente'])
        
        # Criando o objeto de mensagem
        email_msg = MIMEMultipart()
        email_msg['From'] = self.cadastros['email_remetente']
        email_msg['To'] = ', '.join(self.cadastros['email_destinatarios'])
        email_msg['Subject'] = self.cadastros['titulo_email']
        
        # Corpo do e-mail
        email_msg.attach(MIMEText(self.cadastros['corpo_email'], 'html'))
        
        #Anexar Arquivos
        self.__anexar_arquivos(email_msg)
        
        # Envio do e-mail
        server.sendmail(self.cadastros['email_remetente'], 
                        self.cadastros['email_destinatarios'], 
                        email_msg.as_string())
        
        
        server.quit()
                
    def extract(self):
        print('Processo de E-mail iniciado...')
        self.__envio_email()
        print(f'Emails enviados com sucesso para : {self.cadastros['email_destinatarios']}')