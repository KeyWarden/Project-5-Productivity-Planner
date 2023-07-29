from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .models import TaskGroup
from .serializers import GroupSerializer
from pro_plan.permissions import IsOwnerOrReadOnly


class TaskList(APIView):
    """List all Tasks"""
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(
            tasks, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """Manages Task Data Retrieval and Submission"""
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class GroupList(APIView):
    """List all Groups"""
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def get(self, request):
        groups = TaskGroup.objects.all()
        serializer = GroupSerializer(
            tasks, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GroupSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class GroupDetail(APIView):
    """Manages Group Data Retrieval and Submission"""
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            group = TaskGroup.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return group
        except TaskGroup.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(
            group, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(
            group, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
