from django.http import JsonResponse
from .forms import UserProfileForm, WorkoutForm, MealForm, HydrationForm
from .models import UserProfile, Workout2, Meal, Hydration2
from django.shortcuts import render,redirect
from .data.food_calories import FOOD_CALORIES
from .data.workout import WORKOUT_CALORIES
import json



def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


# User Profile
def create_user_profile(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        UserProfile(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
           ).save()
        return redirect('read')
    return render(request, 'tracker/profile.html', {'form': form})
 
def register_users_list(request):
    registers=UserProfile.objects.all()
    return render(request,'tracker/dashboard.html',{'employees':registers})


# Workout
def log_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            user = request.session.get('mongo_user')
            if not user:
                return JsonResponse({'error': 'User not found'}, status=404)

            workout_type = form.cleaned_data['workout_type']
            duration = form.cleaned_data['duration']  # ✅ extract duration first
            calories_burned_per_min = WORKOUT_CALORIES.get(workout_type, 0)
            total_calories = calories_burned_per_min * duration

            Workout2(
                user=user,
                workout_type=workout_type,
                duration=duration,
                calories_burned=total_calories,
                date=form.cleaned_data['date']
            ).save()

            return JsonResponse({'message': f'Workout ({workout_type}) logged with {total_calories} cal burned'}, status=201)
    else:
        form = WorkoutForm()

    context = {
        'form': form,
        'workout_calories_json': json.dumps(WORKOUT_CALORIES)
    }
    return render(request, 'tracker/add_workout.html', context)

# Meal
""" def log_meal(request):
    form = MealForm(request.POST or None)
    if form.is_valid():
        user = str(request.user.username)
        if not user:
            return JsonResponse({'error': 'User not found'}, status=404)
        food = form.cleaned_data['food_items']
        calories = FOOD_CALORIES.get(food, 0)  # Default to 0 if not found
        Meal(
            user=user,
            meal_type=food,
            calories=calories,
            date=form.cleaned_data['date']
        ).save()
        return JsonResponse({'message': 'Meal logged successfully'}, status=201)
    return JsonResponse({'errors': form.errors}, status=400)
 """

# Hydration
def log_hydration(request):
    if request.method == 'POST':
        form = HydrationForm(request.POST)
        if form.is_valid():
            user = request.session.get('mongo_user')  # Get from form, not request.user
            Hydration2(
                user_id=user,
                water_intake_liters=form.cleaned_data['water_intake_liters'],
                date=form.cleaned_data['date']
            ).save()
            return JsonResponse({'message': 'Hydration logged successfully'}, status=201)
        return JsonResponse({'errors': form.errors}, status=400)
    
    # If GET request, show a form (for development or testing)
    form = HydrationForm()
    return render(request, 'tracker/log_hydration.html', {'form': form})

def log_meal_html(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            user = request.session.get('mongo_user')
            if not user:
                return JsonResponse({'error': 'User not found'}, status=404)
            
            food = form.cleaned_data['food_items']
            calories = FOOD_CALORIES.get(food, 0)

            Meal(
                user=user,
                meal_type=food,
                calories=calories,
                date=form.cleaned_data['date']
            ).save()
            return JsonResponse({'message': f'Meal ({food}) logged with {calories} cal'}, status=201)
    else:
        form = MealForm()

    context = {
        'form': form,
        'food_calories_json': json.dumps(FOOD_CALORIES)
    }
    return render(request, 'tracker/Meal.html', context)