from django.http import JsonResponse
from .forms import UserProfileForm, WorkoutForm, MealForm, HydrationForm
from .models import UserProfile, Workout, Meal, Hydration
from django.shortcuts import render,redirect


# User Profile
def create_user_profile(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        UserProfile(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
           ).save()
        return redirect('read')
    return render(request, 'tracker/Profile.html', {'form': form})
 
def register_users_list(request):
    registers=UserProfile.objects.all()
    return render(request,'tracker/read_data.html',{'employees':registers})


# Workout
def log_workout(request):
    form = WorkoutForm(request.POST or None)
    if form.is_valid():
        user = UserProfile.objects(id=form.cleaned_data['user_id']).first()
        if not user:
            return JsonResponse({'error': 'User not found'}, status=404)
        Workout(
            user=user,
            workout_type=form.cleaned_data['workout_type'],
            duration=form.cleaned_data['duration'],
            calories_burned=form.cleaned_data['calories_burned'],
            date=form.cleaned_data['date']
        ).save()
        return JsonResponse({'message': 'Workout logged successfully'}, status=201)
    return JsonResponse({'errors': form.errors}, status=400)


# Meal
def log_meal(request):
    form = MealForm(request.POST or None)
    if form.is_valid():
        user = UserProfile.objects(id=form.cleaned_data['user_id']).first()
        if not user:
            return JsonResponse({'error': 'User not found'}, status=404)
        Meal(
            user=user,
            food_items=form.cleaned_data['food_items'],
            calories=form.cleaned_data['calories'],
            date=form.cleaned_data['date']
        ).save()
        return JsonResponse({'message': 'Meal logged successfully'}, status=201)
    return JsonResponse({'errors': form.errors}, status=400)


# Hydration
def log_hydration(request):
    form = HydrationForm(request.POST or None)
    if form.is_valid():
        user = UserProfile.objects(id=form.cleaned_data['user_id']).first()
        if not user:
            return JsonResponse({'error': 'User not found'}, status=404)
        Hydration(
            user=user,
            water_intake_liters=form.cleaned_data['water_intake_liters'],
            date=form.cleaned_data['date']
        ).save()
        return JsonResponse({'message': 'Hydration logged successfully'}, status=201)
    return JsonResponse({'errors': form.errors}, status=400)
