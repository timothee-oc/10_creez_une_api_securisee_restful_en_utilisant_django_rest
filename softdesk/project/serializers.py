from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author', 'created_time']

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        read_only_fields = ['user', 'project', 'role', 'author']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['author', 'created_time', 'project']
    
    def validate_assignee(self, value):
        project_id = self.context.get('request').parser_context.get('kwargs').get('project_pk')

        if value and not Contributor.objects.filter(project=project_id, user=value).exists():
            raise serializers.ValidationError("L'utilisateur assigné doit être contributeur du projet")
        
        return value

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['uuid', 'author', 'issue', 'created_time']
