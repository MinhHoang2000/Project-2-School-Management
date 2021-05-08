from Person.serializers import AchievementSerializer
from Person.models import Achievement

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
# Create your views here.

class ListAchievement(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show list achievement
    def get(self, request):
        list_achievement = Achievement.objects.all()
        achievement = AchievementSerializer(list_achievement, many=True)
        return Response(achievement.data, status=status.HTTP_200_OK)
    
    # POST -- create a achievement
    def post(self, request):
        achievement = AchievementSerializer(data=request.data)
        try:
            achievement.is_valid(raise_exception=True)
            achievement.save()
            return Response(achievement.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(achievement.errors, status=status.HTTP_400_BAD_REQUEST)

class AchievementDetail(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show achievement detail information
    def get(self, request, achievement_id):
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
            achievement_serializer = AchievementSerializer(achievement)
            return Response(achievement_serializer.data, status=status.HTTP_200_OK)
        except Achievement.DoesNotExist:
            return Response('Achievement does not exist !', status=status.HTTP_400_BAD_REQUEST)
    
    # PUT -- update achievement information
    def put(self, request, achievement_id):
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
            achievement_serializer = AchievementSerializer(achievement, data=request.data, partial=True)
            try:
                achievement_serializer.is_valid(raise_exception=True)
                achievement_serializer.save()
                return Response(achievement_serializer.data, status=status.HTTP_200_OK)
            except serializers.ValidationError:
                return Response(achievement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Achievement.DoesNotExist:
            return Response('Achievement does not exist !', status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE -- delete achievement
    def delete(self, request, achievement_id):
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
            achievement.delete()
            return Response('Delete successfully !', status=status.HTTP_200_OK)
        except Achievement.DoesNotExist:
            return Response('Achievement does not exist !', status=status.HTTP_400_BAD_REQUEST)