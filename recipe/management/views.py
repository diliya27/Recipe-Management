from django.shortcuts import render
from rest_framework import viewsets, status

from management.models import Recipe

from management.serializers import RecipeSerializer

from management.models import Review

from management.serializers import ReviewSerializer

from management.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class RecipeView(viewsets.ModelViewSet):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class ReviewView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated,]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class Reviewfilter(APIView):

    def get(self,request,pk):
        r=Review.objects.filter(recipe_name=pk)
        re=ReviewSerializer(r,many=True)
        return Response(re.data,status=status.HTTP_200_OK)

from django.contrib.auth.models import User

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('search')
        print(query)
        if query:
            r=Recipe.objects.filter(Q(recipe_name_icontains=query) | Q(meal_type_icontains=query)|Q(recipe_cuisine=query) | Q(recipe_ingredients=query))
            rp = RecipeSerializer(r,many=True)
        return Response(rp.data,status=status.HTTP_200_OK)

class SearchMeal(APIView):
    def get(self,request):
        query=request.query_params.get('meal_type')  #query_parameter ---{'search':'carrot'}
        if query:
            b=Recipe.objects.filter(meal_type=query)
            stu =RecipeSerializer(b,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)

class SearchIngredient(APIView):
    def get(self,request):
        query=request.query_params.get('recipe_ingredients')  #query_parameter ---{'search':'carrot'}
        if query:
            b=Recipe.objects.filter(recipe_ingredients__icontains=query)
            stu =RecipeSerializer(b,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)

class SearchCuisine(APIView):
    def get(self,request):
        query=request.query_params.get('recipe_cuisine')  #query_parameter ---{'search':'carrot'}
        if query:
            b=Recipe.objects.filter(recipe_cuisine=query)
            stu =RecipeSerializer(b,many=True)
        return Response(stu.data,status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':"Logout Successfully"},status=status.HTTP_200_OK)

