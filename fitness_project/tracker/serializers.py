'''
from rest_framework import serializers
from .models import UserProfile, Workout, Meal, Hydration

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class HydrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydration
        fields = '__all__'
'''

# serializers.py
from rest_framework import serializers

class UserProfileSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=False, allow_blank=True)
    age = serializers.IntegerField(required=False)

    def create(self, validated_data):
        from .models import UserProfile
        return UserProfile(**validated_data).save()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()  # store UserProfile id or name
    workout_type = serializers.CharField()
    duration = serializers.IntegerField()
    calories_burned = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, validated_data):
        from .models import Workout, UserProfile
        # Assume 'user' is a string representing UserProfile id or name
        user_identifier = validated_data.pop('user')
        user_profile = UserProfile.objects.get(id=user_identifier)
        workout = Workout(user=user_profile, **validated_data)
        workout.save()
        return workout

    def update(self, instance, validated_data):
        from .models import UserProfile
        if 'user' in validated_data:
            user_identifier = validated_data.pop('user')
            instance.user = UserProfile.objects.get(id=user_identifier)
        instance.workout_type = validated_data.get('workout_type', instance.workout_type)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.calories_burned = validated_data.get('calories_burned', instance.calories_burned)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

class MealSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    meal_type = serializers.CharField()
    calories = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, validated_data):
        from .models import Meal, UserProfile
        user_identifier = validated_data.pop('user')
        user_profile = UserProfile.objects.get(id=user_identifier)
        meal = Meal(user=user_profile, **validated_data)
        meal.save()
        return meal

    def update(self, instance, validated_data):
        from .models import UserProfile
        if 'user' in validated_data:
            user_identifier = validated_data.pop('user')
            instance.user = UserProfile.objects.get(id=user_identifier)
        instance.meal_type = validated_data.get('meal_type', instance.meal_type)
        instance.calories = validated_data.get('calories', instance.calories)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

class HydrationSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    amount = serializers.FloatField()  # liters or ml
    date = serializers.DateField()

    def create(self, validated_data):
        from .models import Hydration, UserProfile
        user_identifier = validated_data.pop('user')
        user_profile = UserProfile.objects.get(id=user_identifier)
        hydration = Hydration(user=user_profile, **validated_data)
        hydration.save()
        return hydration

    def update(self, instance, validated_data):
        from .models import UserProfile
        if 'user' in validated_data:
            user_identifier = validated_data.pop('user')
            instance.user = UserProfile.objects.get(id=user_identifier)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

