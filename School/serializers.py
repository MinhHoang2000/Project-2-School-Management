from Teacher.models import Teacher
from Teacher.utils import get_current_teacher
from Teacher.serializers import TeacherSerializer
from django.db.models import fields
from rest_framework import serializers

from .models import ClassRecord, Classroom, Course, TeachingInfo, Timetable
CHOICES_DAY = [('Mon', 'Monday'),
               ('Tue', 'Tuesday'),
               ('Wed', 'Wednesday'),
               ('Thu', 'Thusday'),
               ('Fri', 'Friday'),
               ('Sat', 'Saturday'),
               ('Sun', 'Sunday')]
CHOICES_SHIFT = (
        ("M1", "7:15-8:00"),
        ("M2", "8:10-8:55"),
        ("M3", "9:05-9:50"),
        ("M4", "10:05-10:50"),
        ("M5", "11:00-11:45"),
        ("A1", "13:00-13:45"),
        ("A2", "13:55-14:10"),
        ("A3", "14:50-15:35"),
        ("A4", "15:50-16:35"),
        ("A5", "16:45-17:30"),
    )
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
    
    def validate_class_name(self, value):
        if not Classroom.objects.filter(class_name=value):
                return False
        return True

class TeachingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeachingInfo
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'
class ClassRecordSerializer(serializers.ModelSerializer):
    CLASSIFICATION = (
    ("A", "Tot"),
    ("B", "Kha"),
    ("C", "Trung Binh"),
    ("D", "Yeu")
    )
    course_id = serializers.IntegerField()
    classroom_id = serializers.IntegerField()
    teacher_id = serializers.CharField()
    note = serializers.CharField(required=False)
    student_num = serializers.IntegerField(required=False)
    classification = serializers.ChoiceField(choices=CLASSIFICATION, allow_blank=True,required=False)
    shift = serializers.ChoiceField(choices=CHOICES_SHIFT,required=False)
    day_of_week = serializers.ChoiceField(choices=CHOICES_DAY,required=False)
    study_week = serializers.CharField(required=False)
    semester = serializers.IntegerField(required=False)
    school_year = serializers.CharField(required=False)

    class Meta:
        model = ClassRecord
        fields = ['id', 'course_id', 'classroom_id', 'teacher_id', 'note', 'student_num',
        'classification', 'shift', 'day_of_week', 'study_week', 'semester', 'school_year']
    
    def create(self, validated_data):
        teacher = Teacher.objects.get(pk=validated_data.pop('teacher_id'))
        course = Course.objects.get(pk=validated_data.pop('course_id'))
        classroom = Classroom.objects.get(pk=validated_data.pop('classroom_id'))
        classrecord = ClassRecord.objects.create(
            teacher=teacher,
            course = course,
            classroom = classroom,
            **validated_data
        )
        classrecord.save()
        return classrecord

    def update(self, instance, validated_data):
        
        instance.note = validated_data.get('note', instance.note)
        instance.student_num = validated_data.get('student_num', instance.student_num)
        instance.classification = validated_data.get('classification', instance.classification)
        instance.save()
        return instance