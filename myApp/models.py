from django.db import models

# Create your models here.
"""
schema : questiondb
fields : title, language, notes, difficulty_level, sample_input, sample_output, topic, published_date, is_active
"""
class QuestionsDb(models.Model):
    title = models.CharField(max_length=200)

    language_choice = (
        ("python","Python"),
        ("java","Java")
    )
    language = models.CharField(max_length=100,choices=language_choice)

    difficulty_choice = (
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )
    difficulty_level = models.CharField(max_length=100,choices=difficulty_choice)

    topic = models.CharField(max_length=200)

    notes = models.TextField()

    published_date = models.DateTimeField(auto_now_add=True)

    sample_input = models.TextField()

    sample_output = models.TextField()

    is_active = models.BooleanField(default=True)
    