from django import forms

class FormUpload(forms.Form):
    file_data = forms.FileField()
    teacher_id = forms.CharField()
    course_id = forms.IntegerField()
    classroom_id = forms.IntegerField()
    