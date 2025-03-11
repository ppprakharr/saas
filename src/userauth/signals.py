from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    if not user.email:
        # GitHub sometimes doesn't send email, so generate a placeholder
        user.email = f"{user.username}@example.com"
        user.save()
