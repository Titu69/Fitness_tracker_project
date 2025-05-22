from django import forms
#from .models import UserProfile, Workout, Meal, Hydration
from django import forms
from datetime import date

from django import forms
from datetime import date

class UserProfileForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(min_value=0, required=True)
    #weight = forms.FloatField(min_value=0, required=True)
    

class WorkoutForm(forms.Form):
    user_id = forms.CharField(required=True)
    workout_type = forms.CharField(max_length=100, required=True)
    duration = forms.IntegerField(min_value=0, required=True)
    calories_burned = forms.FloatField(min_value=0, required=True)
    date = forms.DateField(initial=date.today, required=True)

class MealForm(forms.Form):
    user_id = forms.CharField(required=True)
    food_items = forms.CharField(widget=forms.Textarea, required=True)
    calories = forms.FloatField(min_value=0, required=True)
    date = forms.DateField(initial=date.today, required=True)

class HydrationForm(forms.Form):
    user_id = forms.CharField(required=True)
    water_intake_liters = forms.FloatField(min_value=0, required=True)
    date = forms.DateField(initial=date.today, required=True)
