# LIBRARIES PYTHON
from typing import Any

# DJANGO REST FRAMEWORK IMPORTS
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# DJANGO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# FILES APPS IMPORTS
from .utils import validate_fields
from authentication.models import Users
from .models import Volunteers, NewMission
from .tasks import notice_new_mission_volunteers
from .serializers import VolunteersModelsSerializers, NewMissionModelsSerializer


# LIST OBJECTS
class ListVolunteers(APIView):
    def get(self, request: HttpResponse):
        contributors = Volunteers.objects.all()
        serializer = VolunteersModelsSerializers(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ListNewMission(APIView):
    def get(self, request: HttpResponse):
        users = NewMission.objects.all()
        serializers = NewMissionModelsSerializer(users, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

# CREATE OBJECTS
class CreateVolunteers(APIView):
    def post(self, request: HttpResponse):
        data = request.data
        print(data['help'])
        if not validate_fields(data['help']):
            return Response({'error': 'Fields invalids'}, status=status.HTTP_400_BAD_REQUEST)

        serializers = VolunteersModelsSerializers(data=data)
        serializers.is_valid(raise_exception=True)
        create_volunteers = serializers.save()
        return Response({'success': 'registered volunteer. Thanks for being a part!'}, status=status.HTTP_201_CREATED)

class CreateNewMission(APIView):
    def post(self, request: HttpResponse):
        data = request.data

        if not validate_fields(data.get('title', ''),
                               data.get('description', ''),
                               data.get('state', ''),
                               data.get('city', '')):
            return Response({'error': 'fields invalid'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = NewMissionModelsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_new_mission = serializer.save()
        new_mission_id = create_new_mission.id

        emails_volunteers = [i.user.email for i in Volunteers.objects.all() if i.user.email]
        notice_new_mission_volunteers.delay(new_mission_id, emails_volunteers)
        return Response({'success': 'Mission created successfully!'}, status=status.HTTP_201_CREATED)

# PICK UP AN OBJECTS
class GetVolunteers(APIView):
    def get(self, request: HttpResponse, pk):
        volunteers = get_object_or_404(Volunteers, pk=pk)

        if isinstance(volunteers, Volunteers):
            response = {
                    'user': volunteers.user,
                    'help': volunteers.help,
                }
            format_user = {
                'user_id': volunteers.user.pk,
                'user': volunteers.user.username
            }
            response['user'] = format_user
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'volunteers is not an instance of Volunteers'})

class GetNewMission(APIView):
    def get(self, request: HttpResponse, pk):
        mission = get_object_or_404(NewMission, pk=pk)

        if isinstance(mission, NewMission):
            response = {
                'id_mission': mission.id,
                'owner': None,
                'title': mission.title,
                'description': mission.description,
                'state': mission.state,
                'city': mission.city,
                'volunteers': None,
            }
            format_user = {
                'user_id': mission.owner.pk,
                'user': mission.owner.username
            }
            format_volunteers = {
                'voluntary': [
                    {
                        'id': volunteer.user.id,
                        'username': volunteer.user.username,
                    }
                    for volunteer in mission.volunteers.all()
                ]
            }
            response['owner'] = format_user
            response['volunteers'] = format_volunteers
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'Mission is not an instance of NewMission'}, status=status.HTTP_400_BAD_REQUEST)


# DELETE OBJECTS
class DeleteVolunteers(APIView):
    def delete(self, request: HttpResponse, pk):
        volunteers = get_object_or_404(Volunteers, pk=pk)

        if isinstance(volunteers, Volunteers):
            volunteers.delete()
            return Response({'success': 'volunteers deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'instance error': 'volunteers does not instance of Volunteers'}, status=status.HTTP_400_BAD_REQUEST)
        
class VerifyVoluntary(APIView):
    def get(self, request: HttpResponse, pk):
        user = get_object_or_404(Users, pk=pk)

        if isinstance(user, Users):
            print(user)
            user_voluntary = Volunteers.objects.filter(user__id=user.id).first()
            if user_voluntary:
                return Response({'success': 'the user is a volunteer'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'user is not volunteer'}, status=status.HTTP_400_BAD_REQUEST)
       
        return Response({'error': 'user is not an instance of Users'}, status=status.HTTP_400_BAD_REQUEST)