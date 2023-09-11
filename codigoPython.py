from imap_tools import MailBox, AND
import os

# Substitua com suas credenciais e o servidor IMAP apropriado
email = "EMAIL"
senha = "SENHA DO EMAIL"
imap_server = 'imap.terra.com.br'

# Conecte-se à caixa de correio
with MailBox(imap_server).login(email, senha) as meu_email:
    # SET: seleciona a pasta de onde deseja buscar os emails (no caso, "DPK")
    meu_email.folder.set('DPK')

    # Critério para buscar emails do remetente específico com anexos .xml
    criterio = AND(from_="ENDEREÇO DE EMAIL DO REMETENTE ")

    # Inicialize um contador de anexos
    contador_anexos = 0

    # Itere sobre os emails que atendem ao critério
    for email in meu_email.fetch(criterio):
        for anexo in email.attachments:
            if anexo.filename.lower().endswith('.xml'):
                # Diretório onde os anexos serão salvos (pasta local "DPK")
                pasta_destino = "DPK"
                nome_arquivo = os.path.join(pasta_destino, anexo.filename)
                with open(nome_arquivo, 'wb') as arquivo:
                    arquivo.write(anexo.payload)
                contador_anexos += 1

# Imprima o total de anexos .xml encontrados e salvos na pasta "DPK"
print(f"Total de anexos .xml encontrados e salvos na pasta 'DPK': {contador_anexos}")
