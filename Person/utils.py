from .serializers import AchievementSerializer, PersonSerializer, HealthSerializer


def create_person(person_data):
    person = PersonSerializer(data=person_data)
    person.is_valid(raise_exception=True)
    return person.save()

def update_person(person, person_data):
    person_serializer = PersonSerializer(person, data=person_data, partial=True)
    person_serializer.is_valid(raise_exception=True)
    person_serializer.save()

def create_health(health_data):
    health = HealthSerializer(data=health_data)
    health.is_valid(raise_exception=True)
    return health.save()

def update_health(student_health, health_data):
    health_serializer = HealthSerializer(student_health, data=health_data, partial=True)
    health_serializer.is_valid(raise_exception=True)
    health_serializer.save()

def create_achievement(achievement_data):
    achievement = AchievementSerializer(data=achievement_data)
    achievement.is_valid(raise_exception=True)
    return achievement.save()

def update_achievement(student_achievement, achievement_data):
    achievement_serializer = AchievementSerializer(student_achievement, data=achievement_data, partial = True)
    achievement_serializer.is_valid(raise_exception=True)
    achievement_serializer.save()