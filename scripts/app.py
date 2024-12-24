from scripts.collect_client_info import Colect_client_info
x = Colect_client_info().extract_data()

for i in x:

    #Send email infos
    import passwords as p

    #Cliente Dict
    infos = {
        '[Client Name]' : 'name_client',
        "[Product Name]" : 'description',
        "[Quantity]" : 'quantity',
        "[Unit Price]" : 'price',
        "[Total]" : 'full_price',
        "[Client Address]" : 'address',
        "[Client City]" : 'city',
        "[Client State]" : 'state',
        "[Client Phone]" : 'phone',
    }

    #Function Replace Info HTML to Cliente Info
    def replace_info(html_content, client_data):
        for key, value_key in infos.items():
            value = client_data.get(value_key, '')
            html_content = html_content.replace(key, str(value))  # Substituir no conteúdo HTML
        return html_content

    #Archive Charge
    with open("scripts/charge.html", "r", encoding="utf-8") as file:
        corpo_email = file.read()
        
    html_customized = replace_info(html_content=corpo_email, client_data=i)
    
    #Script Send Mail
    from scripts.send_mail import Send_mail
    teste = Send_mail(email_destinatarios=[i['email']],
                                        email_remetente=p.user,
                                        senha_remetente=p.pw,
                                        titulo_email='Invoice Notification - GreenTech Solutions',
                                        corpo_email=html_customized,
                                        path_arquivos=['']
                                        ).extract()