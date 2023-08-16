# LIBRARIES PYTHON
import os
import json
from io import BytesIO
from typing import Any
from hashlib import sha256
from datetime import datetime

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# IMPORTS REPORTLAB
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# DJANGO
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# IMPORTS FILE OF OUTHER APP

# FILES APPS IMPORTS
from .utils import validate_fields, check_image
from .models import CrimeDenunciations, BlogPost, MediaOng, FinancialResources
from .serializers import CrimeDenunciationsModelsSerializer, BlogPostModelsSerializer, MediaOngModelsSerializer, FinancialResourcesSerializer


# LIST OBJECTS
class ListCrimeDenunciations(APIView):
    def get(self, request: HttpResponse):
        users = CrimeDenunciations.objects.all()
        serializers = CrimeDenunciationsModelsSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class ListBlogPost(APIView):
    def get(self, request: HttpResponse):
        users = BlogPost.objects.all()
        serializers = BlogPostModelsSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class ListMediaOng(APIView):
    def get(self, request: HttpResponse):
        users = MediaOng.objects.all()
        serializers = MediaOngModelsSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class ListFinancialResources(APIView):
    def get(self, request: HttpResponse):
        users_financial = FinancialResources.objects.all()
        serializers = FinancialResourcesSerializer(users_financial, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


# CREATE OBJECTS
class CreateCrimeDenunciations(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['description'], data['state'],
                               data['city'], data['address']):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CrimeDenunciationsModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_crime_denunciations = serializer.save()
        return Response({'success': 'Reported successfully!'}, status=status.HTTP_201_CREATED)

class CreateBlogPost(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['title'], data['description'],
                               data['state'], ['city']):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BlogPostModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_blog_post = serializer.save()
        return Response({'success': 'Post created successfully!'}, status=status.HTTP_201_CREATED)

class CreateMediaOng(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['title'], data['description'],):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MediaOngModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_media_ong = serializer.save()
        return Response({'success': 'Media created successfully!'}, status=status.HTTP_201_CREATED)

class CreateFinancialResources(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['title'], data['description']):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = FinancialResourcesSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_financial_resources = serializer.save()
        return Response({'success': 'Financial resources created successfully!'}, status=status.HTTP_201_CREATED)

# PICK UP AN OBJECTS
class GetCrimeDenunciations(APIView):
    def get(self, request: HttpResponse, pk):
        denunciations = get_object_or_404(CrimeDenunciations, pk=pk)

        if isinstance(denunciations, CrimeDenunciations):
            response = {
                    'id': denunciations.id,
                    'image': denunciations.image.url or None,
                    'user': None,
                    'description': denunciations.description,
                    'state': denunciations.state,
                    'city': denunciations.city,
                    'address': denunciations.address,
                    'number': denunciations.number,
                    'reference_point': denunciations.reference_point,
                    'phone': denunciations.phone,
                }
            format_user = {
                'user_id': denunciations.user.pk,
                'user': denunciations.user.username
            }
            response['user'] = format_user
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'denunciations is not an instance of CrimeDenunciations'}, status=status.HTTP_400_BAD_REQUEST)

class GetBlogPost(APIView):
    def get(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)

        if isinstance(post, BlogPost):
            response = {
                'image': post.image.url or None,
                'title': post.title,
                'description': post.description,
                'state': post.state,
                'city': post.city,
                'owner': None,
            }
            format_user = {
                'user_id': post.owner.pk,
                'user': post.owner.username
            }
            response['owner'] = format_user
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'Post is not an instance of BlogPost'}, status=status.HTTP_400_BAD_REQUEST)

class GetMediaOng(APIView):
    def get(self, request: HttpResponse, pk):
        media = get_object_or_404(MediaOng, pk=pk)

        if isinstance(media, MediaOng):
            response = {
                'image_before': media.image_before.url or None,
                'image_after': media.image_after.url or None,
                'title': media.title,
                'owner': None,
            }
            format_user = {
                'user_id': media.owner.pk,
                'user': media.owner.username
            }
            response['owner'] = format_user
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'Media is not an instance of MediaOng'}, status=status.HTTP_400_BAD_REQUEST)


# UPDATE OBJECTS
class UpdateBlogPost(APIView):
    def get(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostModelsSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)

        if isinstance(post, BlogPost):
            data = request.data
            
            if not validate_fields(data['title'], data['description'],
                                   data['state'], data['city'],
                                   data['address']):
                return Response({'error': 'fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

            post.title = data['title']
            post.description = data['description']
            post.state = data['state']
            post.city = data['city']
            post.address = data['address']
            post.save()
            return Response({'success': 'successfully changed post of data'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'post does not instance of BlogPost'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateMediaOng(APIView):
    def get(self, request: HttpResponse, pk):
        media = get_object_or_404(MediaOng, pk=pk)
        serializer = MediaOngModelsSerializer(media)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: HttpResponse, pk):
        media = get_object_or_404(BlogPost, pk=pk)

        if isinstance(media, MediaOng):
            data = request.data
            
            if not validate_fields(data['title'], data['description'],):
                return Response({'error': 'fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

            media.title = data['title']
            media.description = data['description']
            media.save()
            return Response({'success': 'successfully changed media of data'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'media does not instance of MediaOng'}, status=status.HTTP_400_BAD_REQUEST)


# DELETE OBJECTS
class DeleteBlogPost(APIView):
    def delete(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)

        if isinstance(post, BlogPost):
            post.delete()
            return Response({'success': 'post deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'post does not instance of BlogPost'}, status=status.HTTP_400_BAD_REQUEST)


# PDF Generate and Receive
class PdfGenerate(APIView):

    def post(self, request: HttpResponse):
        data = request.data
        print('Dados: ',data)

        if not validate_fields(data['email']):
            return Response({'error': 'field invalid'}, status=status.HTTP_400_BAD_REQUEST)
        
        email_hash = sha256(data['email'].encode()).hexdigest()
        file_path = os.path.join('pdf', f'{email_hash}.pdf')

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
        # response.write(pdf)
        return Response({'success': 'Generate successfully'}, status=status.HTTP_200_OK, content_type='application/pdf')
        # response['Content-Disposition'] = f'inline; filename="{email_hash}.pdf"'

class PdfReceive(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['email']):
            return Response({'error': 'field invalid'}, status=status.HTTP_400_BAD_REQUEST)

        email_hash = sha256(data['email'].encode()).hexdigest()
        file_path = os.path.join('pdf', f'{email_hash}.pdf')
        os.remove(file_path)
        file_path_new = os.path.join('pdf', f'{email_hash}_assinatura.pdf')

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
        
        p.drawString(20, 180, f"Assinatura do Usuário: {data['signature']}")
        p.drawString(20, 165, f"Nome do Usuário: {data['signature']}")
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
        return Response({'success': 'Subscription made successfully'}, status=status.HTTP_201_CREATED)
