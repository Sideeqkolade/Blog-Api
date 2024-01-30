from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import UserRegistrationSerializer, UserLoginSerializer, BlogPostSerializer


# create a class UserRegistrationView
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# creating a class UserLoginView
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'], password=serializer.validated_data['password']
            )
            
            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({'access_token': access_token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# create a class BlogPostListView
class BlogPostListView(APIView):
    permission_classes = [IsAuthenticated]

    # retrieving all blog posts
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)
    
    # creating a new blog post
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create a class BlogPostDetailView
class BlogPostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # retrieving a specific blog post
    def get(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)

        except BlogPost.DoesNotExist:
            return Response(
                {'error': 'Blog post not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)
    
    # updating a specific blog post
    def put(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        
        except BlogPost.DoesNotExist:
            return Response(
                {'error': 'Blog post not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BlogPostSerializer(blog_post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # deleting a specific blog post
    def delete(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response(
                {'error': 'Blog post not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)