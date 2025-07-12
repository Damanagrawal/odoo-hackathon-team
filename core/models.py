from django.contrib.auth.models import User
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    OFFERED = 'offered'
    REQUESTED = 'requested'
    SKILL_TYPE = [(OFFERED, 'Offered'), (REQUESTED, 'Requested')]
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPE)

class SwapRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    skill_offered = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='offered_swaps')
    skill_requested = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='requested_swaps')
    STATUS = [('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')]
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_given')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_received')
    swap = models.ForeignKey(SwapRequest, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()