# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# IMPORTS FILE OF OUTHER APP


# FILES APPS IMPORTS
from .utils import validate_fields, check_image
from .models import CrimeDenunciations, BlogPost, MediaOng
from .serializers import CrimeDenunciationsModelsSerializer, BlogPostModelsSerializer, MediaOngModelsSerializer


class CreateCrimeDenunciations(ModelViewSet):
    queryset = CrimeDenunciations.objects.all()
    serializer_class = CrimeDenunciationsModelsSerializer

    def list(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_serializer())
        data = request.data
        
        if not validate_fields(data['user'], data['description'], data['state'], data['city'], data['address'], data['number'], data['reference_point']):
            return Response({'error': 'fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_crime_denunciations = serializer.save()
        return Response({'success': 'Reported successfully!'}, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request: HttpResponse, pk):
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
            serializer = self.get_serializer(response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error':'user is not an instance of Users'}, status=status.HTTP_400_BAD_REQUEST)
        

class CreateBlogPost(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostModelsSerializer

    def list(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data
        image_file = request.data.get('image')
        if not validate_fields(data['title'], data['description'], data['state'], data['city']):
            return Response({'error':'fields invalids'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_blog_post = serializer.save()
        return Response({'success':'Post created successfully'}, status=status.HTTP_201_CREATED)

    def retrieve(self, request: HttpResponse, pk):
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
            serializer = self.get_serializer(response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Post is not an instance of BlogPost'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)

        if isinstance(post, BlogPost):
            serializer = self.get_serializer(post, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({'success': 'Post successfully updated!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Post is not an instance of BlogPost'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: HttpResponse, pk):
        post = get_object_or_404(BlogPost, pk=pk)

        if isinstance(post, BlogPost):
            post.delete()
            return Response({'success': 'Post deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'post does not instance of BlogPost'}, status=status.HTTP_400_BAD_REQUEST)


class CreateMediaOng(ModelViewSet):
    queryset = MediaOng.objects.all()
    serializer_class = MediaOngModelsSerializer

    def list(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: HttpResponse):
        queryset = self.filter_queryset(self.get_queryset())
        data = request.data

        if not validate_fields(data['title']):
            return Response({'error':'field invalid'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_media_ong = serializer.save()
        return Response({'success':'Media created successfully'}, status=status.HTTP_201_CREATED)

    def retrieve(self, request: HttpResponse, pk):
        media = get_object_or_404(MediaOng, pk=pk)
        
        if isinstance(media, MediaOng):
            response = {
                'image_before': media.image_before,
                'image_after': media.image_after,
                'title': media.title,
                'owner': media.owner,
            }
            serializer = self.get_serializer(response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'media is not an instance of MediaOng'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request: HttpResponse, pk):
        media = get_object_or_404(MediaOng, pk=pk)

        if isinstance(media, MediaOng):
            serializer = self.get_serializer(media, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            media = serializer.save()
            return Response({'success':'Media successfully updated!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Media is not an instance of MediaOng'}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request: HttpResponse, pk):
        media = get_object_or_404(MediaOng, pk=pk)

        if isinstance(media, MediaOng):
            media.delete()
            return Response({'success': 'Media deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'media does not instance of MediaOng'}, status=status.HTTP_400_BAD_REQUEST)
