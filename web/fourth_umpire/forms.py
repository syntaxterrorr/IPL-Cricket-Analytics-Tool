from django import forms
from .models import Match

team_choice = (
        (1,	'Mumbai Indians'),
        (2,	'Royal Challengers Bangalore'),
        (3,	'Chennai Super Kings'),
        (4,	'Kings XI Punjab'),
        (5,	'Rajasthan Royals'),
        (6,	'Delhi Daredevils'),
        (7, 'Sunrisers Hyderabad'),
        (8,	'Kolkata Knight Riders'),
)



class InningsSecond(forms.Form):
    team2 = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Your Team")
    team1 = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Opponent Team")
