# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# IMPORTS FILE OF OUTHER APP

# FILES APPS IMPORTS
from .utils import validate_fields, check_image
from .models import CrimeDenunciations, BlogPost, MediaOng, NewMission
from .serializers import CrimeDenunciationsModelsSerializer, BlogPostModelsSerializer, MediaOngModelsSerializer, NewMissionModelsSerializer


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
    
class ListNewMission(APIView):
    def get(self, request: HttpResponse):
        users = NewMission.objects.all()
        serializers = NewMissionModelsSerializer(users, many=True)
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

        create_crime_denunciations = serializer.save(is_active=False)
        return Response({'success': 'Reported successfully!'}, status=status.HTTP_201_CREATED)

class CreateBlogPost(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['title'], data['description'],
                               data['state'], ['city']):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BlogPostModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_blog_post = serializer.save(is_active=False)
        return Response({'success': 'Post created successfully!'}, status=status.HTTP_201_CREATED)

class CreateMediaOng(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['title'], data['description'],):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MediaOngModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_media_ong = serializer.save(is_active=False)
        return Response({'success': 'Media created successfully!'}, status=status.HTTP_201_CREATED)
    
class CreateNewMission(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data['title'], data['description'],
                               data['state'], ['city']):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NewMissionModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        create_new_mission = serializer.save(is_active=False)
        return Response({'success': 'Mission created successfully!'}, status=status.HTTP_201_CREATED)


# PICK UP AN OBJECTS
class GetCrimeDenunciations(APIView):
    def get(self, request: HttpResponse, pk):
        denunciations = get_object_or_404(CrimeDenunciations, pk=pk)

        if isinstance(denunciations, CrimeDenunciations):
            response = {
                    'image': denunciations.image,
                    'user': denunciations.user,
                    'description': denunciations.description,
                    'state': denunciations.state,
                    'city': denunciations.city,
                    'address': denunciations.address,
                    'number': denunciations.number,
                    'reference_point': denunciations.reference_point,
                    'phone': denunciations.phone,
                }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'denunciations is not an instance of CrimeDenunciations'})

class GetBlogPost(APIView):
    def get(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)

        if isinstance(post, BlogPost):
            response = {
                'image': post.image,
                'title': post.title,
                'description': post.description,
                'state': post.state,
                'city': post.city,
                'owner': post.owner,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'Post is not an instance of BlogPost'})

class GetMediaOng(APIView):
    def get(self, request: HttpResponse, pk):
        media = get_object_or_404(MediaOng, pk=pk)

        if isinstance(media, MediaOng):
            response = {
                'image_before': media.image_before,
                'image_after': media.image_after,
                'title': media.title,
                'owner': media.owner,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'Media is not an instance of MediaOng'})

class GetNewMission(APIView):
    def get(self, request: HttpResponse, pk):
        mission = get_object_or_404(NewMission, pk=pk)

        if isinstance(mission, NewMission):
            response = {
                'owner': mission.owner,
                'title': mission.title,
                'description': mission.description,
                'state': mission.state,
                'city': mission.city,
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'Mission is not an instance of NewMission'})


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

class DeleteNewMission(APIView):
    def delete(self, request: HttpResponse, pk):
        mission = get_object_or_404(NewMission, pk=pk)

        if isinstance(mission, NewMission):
            mission.delete()
            return Response({'success': 'mission deleted successfully'}, status=status.HTTP_200_OK) 
        else:
            return Response({'instance error': 'mission does not instance of NewMission'}, status=status.HTTP_400_BAD_REQUEST)
