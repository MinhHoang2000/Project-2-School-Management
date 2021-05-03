from .serializers import PersonSerializer, HealthSerializer


def create_person(data):
    person = PersonSerializer(data=data)
    person.is_valid(raise_exception=True)
    return person.save()

def create_health(health_data):
    health_serializer = HealthSerializer(data=health_data)
    health_serializer.is_valid(raise_exception=True)
    return health_serializer.save()