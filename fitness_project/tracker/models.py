# models.py
from mongoengine import Document, StringField, IntField, DateField, ReferenceField, FloatField

class UserProfile(Document):
    name = StringField(required=True, max_length=100)
    email = StringField(max_length=100)
    age = IntField()

    def __str__(self):
        return f"{self.name} ({self.email})"

class Workout(Document):
    user = ReferenceField(UserProfile, required=True)
    workout_type = StringField(required=True)
    duration = IntField(required=True)  # duration in minutes
    calories_burned = IntField()
    date = DateField(required=True)

    def __str__(self):
        return f"Workout({self.workout_type}) for {self.user.name} on {self.date}"

class Meal(Document):
    user = ReferenceField(UserProfile, required=True)
    meal_type = StringField(required=True)  # e.g., Breakfast, Lunch, Dinner
    calories = IntField(required=True)
    date = DateField(required=True)

    def __str__(self):
        return f"Meal({self.meal_type}) for {self.user.name} on {self.date}"

class Hydration(Document):
    user = ReferenceField(UserProfile, required=True)
    amount = FloatField(required=True)  # amount in liters or ml
    date = DateField(required=True)

    def __str__(self):
        return f"Hydration({self.amount}L) for {self.user.name} on {self.date}"
