from rest_framework import serializers
from .models import Project, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {"author": {"read_only": True}}
    
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        extra_kwargs = {
            "author": {"read_only": True},
            "project": {"read_only": True},
        }
    
    def create(self, validated_data):
        request = self.context.get("request")
        view = self.context.get("view")
        project = Project.objects.get(id=view.kwargs.get("project_pk"))
        validated_data["author"] = request.user
        validated_data["project"] = project
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
