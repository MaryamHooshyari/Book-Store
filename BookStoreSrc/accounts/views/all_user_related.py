from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from BookStoreSrc import settings
from ..forms import CustomUserCreationForm
from ..tokens import activation_token


def login_redirect(request):
    if request.user.is_staff:
        return redirect('staff_home')
    else:
        return redirect('home')


def activate(req, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(id=uid)
    except(TypeError, ValueError):
        user = None
    if user and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(req, 'حساب کاربری شما فعال شد. وارد شوید:)')
        return redirect('login')
    else:
        # messages.error(req, "Activation  link is Invalid.")
        return HttpResponse("Activation link is Invalid.")


def signup(req):
    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            site = get_current_site(req)
            mail_subject = "Confirmation message"
            message = render_to_string('registration/activate_email.html', {
                "user": user,
                'domain': site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            to_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(mail_subject, message, from_email, to_list, fail_silently=False)
            messages.success(req, "حساب کاربری با موفقیت ثبت شد، لینک تایید به ایمیل شما ارسال شده است.")
    else:
        form = CustomUserCreationForm()
    return render(req, 'registration/signup.html', {'form': form})
