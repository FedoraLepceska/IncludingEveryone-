from django.forms import ModelForm

from app.models import Lecture, Quiz


class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ("name", "video")

    def __init__(self, *args, **kwargs):
        super(LectureForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"


class AddQuestionForm(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"
