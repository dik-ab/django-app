from django import forms
from .models import Experiences


class ExperienceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields['certification'].widget.attrs.update({'class':'chosen form-control'})
        

    class Meta:
        model = Experiences
        fields = ['certification', 'title','score', 'study_time', 'how_to_study', 'url',  'description']
        labels = {'certification': '資格または大学名を検索',
                 'title': 'タイトル',
                 'score': '得点または得点率',
                 'study_time': '取得までにかかった時間',
                 'how_to_study': '使った参考書名やサイト名',
                 'url': 'サイトのURL(もしあれば)',
                 'description': '内容',
                 }

    