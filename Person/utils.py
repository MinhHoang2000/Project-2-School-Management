from .serializers import PersonSerializer, HealthSerializer


def create_person(person_data):
    person = PersonSerializer(data=person_data)
    person.is_valid(raise_exception=True)
    return person.save()

def update_person(person, person_data):
    person_serializer = PersonSerializer(person, data=person_data, partial=True)
    person_serializer.is_valid(raise_exception=True)
    person_serializer.save()

def create_health(health_data):
    health_serializer = HealthSerializer(data=health_data)
    health_serializer.is_valid(raise_exception=True)
    return health_serializer.save()

def update_health(student_health, health_data):
    health_serializer = HealthSerializer(student_health, data=health_data, partial=True)
    health_serializer.is_valid(raise_exception=True)
    health_serializer.save()