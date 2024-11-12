from rest_framework import serializers

from management.models import Recipe

from management.models import Review


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields=['id','recipe_name','recipe_ingredients','instructions','recipe_cuisine','meal_type']
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['recipe_name','user','rating','comment']

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']

    def create(self,validated_data):  #after validation validated_data ie deserialized data is sent to create() function
        user=User.objects.create_user(username=validated_data['username'],
                                      password=validated_data['password'],
                                      email=validated_data['email'],
                                      first_name=validated_data['first_name'],
                                      last_name=validated_data['last_name'])
        return user
