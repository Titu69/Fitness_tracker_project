from django import forms
#from .models import UserProfile, Workout, Meal, Hydration
from django import forms
from datetime import date
from mongoengine import Document, StringField, FloatField, DateField
from .data.food_calories import FOOD_CALORIES
from .data.workout import WORKOUT_CALORIES
from django import forms
from datetime import date

class UserProfileForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(min_value=0, required=True)
    #weight = forms.FloatField(min_value=0, required=True)
    

class WorkoutForm(forms.Form):
    #user_id = forms.CharField(label='User ID')
    workout_type = forms.ChoiceField(
        choices=[(k, k) for k in WORKOUT_CALORIES.keys()],
        label='Workout Type'
    )
    duration = forms.IntegerField(label='Duration (minutes)', min_value=1)
    date = forms.DateField(widget=forms.SelectDateWidget)

class MealForm(forms.Form):
    #user = forms.CharField(required=True)
    FOOD_CHOICES = [(food, food) for food in FOOD_CALORIES.keys()]
    food_items = forms.ChoiceField(choices=FOOD_CHOICES, required=True)
    #calories = forms.FloatField(min_value=0, required=True)
    date = forms.DateField(initial=date.today, required=True)


class HydrationForm(forms.Form):
    #user_id = forms.CharField(required=True)
    water_intake_liters = forms.FloatField(min_value=0, required=True)
    date = forms.DateField(initial=date.today, required=True)