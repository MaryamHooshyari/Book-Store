from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

"""This method will return the currently active user model - CustomUser model in this case"""
UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            """find the user with same email as input username"""
            user = UserModel.objects.get(Q(email__iexact=username))
        except UserModel.DoesNotExist:
            """
            Run the default password hasher once to reduce the timing
            difference between an existing and a nonexistent user (#20760)
            """
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            """
            if there was more than one object with the specific email 
            this will get the first one on database ordered by id
            * by the way it shouldn't happen because email's unique attribute is True in UserModel
            """
            user = UserModel.objects.filter(Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            """
            check_password: method in AbstractBaseUser to check if the password matches or not, returns boolean
            user_can_authenticate: method in ModelBackend to check if the user is active or not, returns boolean
            """
            return user
