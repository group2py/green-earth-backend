import os
import json
from io import BytesIO
from hashlib import sha256
from datetime import datetime
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def t(request):
    return render(request, 'a.html')

@csrf_exempt
def gerar_pdf(request):
        email = request.user.email
        email_hash = sha256(email.encode()).hexdigest()
        file_path = os.path.join('media', 'pdf', f'{email_hash}.pdf')

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{email_hash}.pdf"'

        buffer = BytesIO()

        p = canvas.Canvas(buffer, pagesize=letter)

        p.setFont("Helvetica", 12)

        p.drawString(20, 750, "CONTRATO DE PARCERIA ENTRE A ONG DE MEIO AMBIENTE E O USUÁRIO")
        p.drawString(20, 735, 'Este Contrato de Parceria (o "Contrato") é celebrado entre a ONG de Meio Ambiente')
        p.drawString(20, 720, 'doravante referida como "ONG" e o usuário identificado abaixo')
        p.drawString(20, 705, 'doravante referido como "Usuário".')

        p.drawString(20, 675, "1. OBJETIVO")
        p.drawString(20, 660, "A ONG e o Usuário concordam em estabelecer uma parceria com o objetivo")
        p.drawString(20, 645, "de colaborar em ações específicas de preservação e conservação do meio ambiente")
        p.drawString(20, 630, "conforme detalhado no Anexo A.")
        
        p.drawString(20, 600, "2. RESPONSABILIDADES DA ONG")
        p.drawString(20, 585, "A ONG se compromete a:")
        p.drawString(20, 570, "a) Fornecer orientação e suporte técnico relacionado às atividades de preservação ambiental.")
        p.drawString(20, 555, "b) Coordenar e supervisionar as atividades planejadas de acordo")
        p.drawString(20, 540, "com o cronograma definido no Anexo A.")
        p.drawString(20, 525, "c) Disponibilizar recursos, quando necessário, para a execução das atividades.")
        
        p.drawString(20, 495, "3. RESPONSABILIDADES DO USUÁRIO")
        p.drawString(20, 480, "O Usuário se compromete a:")
        p.drawString(20, 465, "a) Participar ativamente das atividades de preservação ambiental conforme estabelecido no Anexo A.")
        p.drawString(20, 450, "b) Cumprir as diretrizes de segurança e protocolos estabelecidos pela ONG durante as atividades.")
        p.drawString(20, 435, "c) Contribuir com recursos e esforços, conforme acordado entre as partes.")
        
        p.drawString(20, 405, "4. DURAÇÃO DA PARCERIA")
        p.drawString(20, 390, "A parceria estabelecida por meio deste Contrato terá início na data de assinatura e permanecerá")
        p.drawString(20, 375, "em vigor até a conclusão das atividades especificadas no Anexo A, a menos que seja")
        p.drawString(20, 360, "rescindida antecipadamente por ambas as partes.")
        
        p.drawString(20, 330, "5. CONFIDENCIALIDADE")
        p.drawString(20, 315, "Ambas as partes concordam em manter confidenciais todas as informações e materiais")
        p.drawString(20, 300, "compartilhados durante a execução deste Contrato.")
        
        p.drawString(20, 270, "6. ASSINATURAS")
        p.drawString(20, 255, "Este Contrato é assinado pelas partes abaixo como evidência de sua aceitação e comprometimento.")
        p.drawString(20, 240, "Assinatura da ONG: OngGreenEarth2023")
        p.drawString(20, 225, "Nome da ONG: Green Earth")
        p.drawString(20, 210, f"Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}/")
        
        p.drawString(20, 180, "Assinatura do Usuário: _______________________")
        p.drawString(20, 165, "Nome do Usuário: ___________________________")
        p.drawString(20, 150, f"Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}/")
        
        p.drawString(20, 120, "ANEXO A - Atividades Específicas")
        p.drawString(20, 105, "[Descreva detalhadamente as atividades de preservação ambiental")
        p.drawString(20, 90, "cronograma, recursos necessários e outras informações relevantes.]")
        
        p.drawString(20, 60, "Este Contrato representa o entendimento completo entre a ONG e o Usuário em relação à")
        p.drawString(20, 45, "parceria estabelecida e substitui todos os acordos anteriores, se houver. Este Contrato pode")
        p.drawString(20, 30, "ser modificado somente por escrito e assinado por ambas as partes.")
        
        p.drawString(20, 15, f"Assinado e aceito em Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}/")
        p.save()

        pdf = buffer.getvalue()
        buffer.seek(0)

        with open(file_path, 'wb') as pdf_file:
            pdf_file.write(pdf)

        buffer.close()
        
        pdf_url = f"{settings.BASE_DIR}/media/pdf/{email_hash}.pdf"

        pdf_content = {
            'success': 'Generate successfully',
            'pdf_url': pdf_url,
            'pdf': pdf
        }

        response.write(pdf_content)
        return response

def public_pdf_view(request, email):
    email_hash = sha256(email.encode()).hexdigest()
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdf', f'{email_hash}.pdf')
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{email_hash}.pdf"'
            return response
    else:
        return HttpResponse("PDF not found.")

@csrf_exempt
def receber_pdf(request):
    email = request.user.email
    
    email_hash = sha256(email.encode()).hexdigest()
    file_path = os.path.join('media', 'pdf', f'{email_hash}.pdf')
    os.remove(file_path)
    file_path_new = os.path.join('media', 'pdf', f'{email_hash}_assinatura.pdf')

    assinatura = 'PedroDev'
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(20, 750, "CONTRATO DE PARCERIA ENTRE A ONG DE MEIO AMBIENTE E O USUÁRIO")
    p.drawString(20, 735, 'Este Contrato de Parceria (o "Contrato") é celebrado entre a ONG de Meio Ambiente')
    p.drawString(20, 720, 'doravante referida como "ONG" e o usuário identificado abaixo')
    p.drawString(20, 705, 'doravante referido como "Usuário".')
    
    p.drawString(20, 675, "1. OBJETIVO")
    p.drawString(20, 660, "A ONG e o Usuário concordam em estabelecer uma parceria com o objetivo")
    p.drawString(20, 645, "de colaborar em ações específicas de preservação e conservação do meio ambiente")
    p.drawString(20, 630, "conforme detalhado no Anexo A.")
    
    p.drawString(20, 600, "2. RESPONSABILIDADES DA ONG")
    p.drawString(20, 585, "A ONG se compromete a:")
    p.drawString(20, 570, "a) Fornecer orientação e suporte técnico relacionado às atividades de preservação ambiental.")
    p.drawString(20, 555, "b) Coordenar e supervisionar as atividades planejadas de acordo")
    p.drawString(20, 540, "com o cronograma definido no Anexo A.")
    p.drawString(20, 525, "c) Disponibilizar recursos, quando necessário, para a execução das atividades.")
    
    p.drawString(20, 495, "3. RESPONSABILIDADES DO USUÁRIO")
    p.drawString(20, 480, "O Usuário se compromete a:")
    p.drawString(20, 465, "a) Participar ativamente das atividades de preservação ambiental conforme estabelecido no Anexo A.")
    p.drawString(20, 450, "b) Cumprir as diretrizes de segurança e protocolos estabelecidos pela ONG durante as atividades.")
    p.drawString(20, 435, "c) Contribuir com recursos e esforços, conforme acordado entre as partes.")
    
    p.drawString(20, 405, "4. DURAÇÃO DA PARCERIA")
    p.drawString(20, 390, "A parceria estabelecida por meio deste Contrato terá início na data de assinatura e permanecerá")
    p.drawString(20, 375, "em vigor até a conclusão das atividades especificadas no Anexo A, a menos que seja")
    p.drawString(20, 360, "rescindida antecipadamente por ambas as partes.")
    
    p.drawString(20, 330, "5. CONFIDENCIALIDADE")
    p.drawString(20, 315, "Ambas as partes concordam em manter confidenciais todas as informações e materiais")
    p.drawString(20, 300, "compartilhados durante a execução deste Contrato.")
    
    p.drawString(20, 270, "6. ASSINATURAS")
    p.drawString(20, 255, "Este Contrato é assinado pelas partes abaixo como evidência de sua aceitação e comprometimento.")
    p.drawString(20, 240, "Assinatura da ONG: OngGreenEarth2023")
    p.drawString(20, 225, "Nome da ONG: Green Earth")
    p.drawString(20, 210, f"Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}/")
    
    p.drawString(20, 180, f"Assinatura do Usuário: {assinatura}")
    p.drawString(20, 165, f"Nome do Usuário: {assinatura}")
    p.drawString(20, 150, f"Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}/")
    
    p.drawString(20, 120, "ANEXO A - Atividades Específicas")
    p.drawString(20, 105, "[Descreva detalhadamente as atividades de preservação ambiental")
    p.drawString(20, 90, "cronograma, recursos necessários e outras informações relevantes.]")
    
    p.drawString(20, 60, "Este Contrato representa o entendimento completo entre a ONG e o Usuário em relação à")
    p.drawString(20, 45, "parceria estabelecida e substitui todos os acordos anteriores, se houver. Este Contrato pode")
    p.drawString(20, 30, "ser modificado somente por escrito e assinado por ambas as partes.")
    
    p.drawString(20, 15, f"Assinado e aceito em Data: {datetime.now().day}/{datetime.now().month}/{datetime.now().year}/")
    p.save()

    pdf = buffer.getvalue()
    buffer.seek(0)

    with open(file_path_new, 'wb') as pdf_file:
        pdf_file.write(pdf)

    buffer.close()
    pdf_url = f"{settings.BASE_DIR}/media/pdf/{file_path_new}.pdf"
    print(pdf_url)
    return None

   