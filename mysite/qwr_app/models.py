from django.db import models
from collections import Counter



class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}'

    def get_reaction_counts(self):
        emojis = self.reactions.values_list('emoji', flat=True)
        counts = Counter(emojis)
        return dict(counts)



class Reaction(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='reactions')
    emoji = models.CharField(max_length=10)  # Например: "👍", "🔥", "😂"
    created_at = models.DateTimeField(auto_now_add=True)