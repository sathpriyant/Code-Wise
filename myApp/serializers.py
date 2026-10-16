from rest_framework import serializers
from myApp.models import QuestionsDb

class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    language = serializers.ChoiceField(choices=QuestionsDb.language_choice,default="python")
    difficulty_level = serializers.ChoiceField(choices=QuestionsDb.difficulty_choice,default="easy")
    topic = serializers.CharField(max_length=200)
    notes = serializers.CharField(max_length=200)
    published_date = serializers.DateTimeField(read_only=True)
    sample_input = serializers.CharField(max_length=300)
    sample_output = serializers.CharField(max_length=300)
    is_active = serializers.BooleanField(default=True)