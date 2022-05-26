from django import forms
from .models import Experiences


CHOICES = [('あり','あり'),('なし','なし')]
class ExperienceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.label_suffix=" "
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields['certification'].widget.attrs.update({'class':'selecter'})
        self.fields['予備校'] = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Experiences
        fields = ['certification','faculty','予備校', 'title','common_test_score','score', 'study_time', 'how_to_study','how_to_study_site','motivation', 'study_method',  'description','advices']
        labels = {'certification': '資格または大学名を検索※',
                 'faculty':'学部',
                 '予備校':'予備校※',
                 'title': 'タイトル※',
                 'common_test_score':'共通テスト得点(率)',
                 'score':'2次試験得点(率)',
                 'study_time': '本格的に受験勉強を始めた時期',
                 'how_to_study': 'おすすめ教材',
                 'how_to_study_site':'使用したサービス',
                 'motivation':'モチベーション維持に役に立ったもの',
                 'study_method':'共通テスト対策方法',
                 'description':'二次試験(一般入試)対策方法',
                 'advices':'受験生に向けてアドバイス',
                 }
        widgets = {
                'how_to_study' : forms.Textarea(attrs={'rows':3,'cols':2,'placeholder':'おすすめ参考書、塾に行っていた方はおすすめの講座も是非'
                }),
                'how_to_study_site':forms.Textarea(attrs={'rows':1,'placeholder':'youtubeのチャンネルやwebサイト名'}),
                'motivation':forms.Textarea(attrs={'rows':2}),
                    'study_method':forms.Textarea(attrs={'rows':5,'cols':1,'placeholder':'共通テストの勉強方法'}),
                    'description':forms.Textarea(attrs={'rows':7,'cols':1,'placeholder':'具体的に行った勉強方法や注意することなどをお書きください'}),
                    'advices':forms.Textarea(attrs={'rows':5,'cols':1,'placeholder':'試験や勉強方法に関することだけでなく、当日のアドバイスなどもあれば是非お書きください'}),
                    }


    
