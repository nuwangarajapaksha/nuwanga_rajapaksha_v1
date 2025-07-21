import logging

from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils.timezone import now

from nuwanga_rajapaksha_v1 import settings
from .forms import ContactForm

logger = logging.getLogger(__name__)


def footer_contact_view(request):
    if request.method == 'POST':
        logger.info(
            "Contact form POST received ‑ ip=%s ‑ path=%s ‑ at=%s",
            request.META.get("REMOTE_ADDR"),
            request.path,
            now().isoformat(timespec="seconds"),
        )
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            logger.debug("Validated data: %s", cd)
            email = EmailMessage(
                subject=f"Message from {cd['name']}",
                body=f"From: {cd['name']} <{cd['email']}>\n\n{cd['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['nuwangarajapaksha@gmail.com'],
                headers={'Reply-To': cd['email']}
            )

            try:
                email.send()
                logger.info("Email sent successfully from %s", cd["email"])
                messages.success(request, "✅ Your message has been sent successfully!")
            except Exception as e:
                logger.exception("Unexpected error sending contact email from %s", cd["email"])
                messages.error(request, "❌ Failed to send your message.")
        else:
            logger.error("Invalid contact form: %s", form.errors.as_json())
            messages.error(request, "⚠️ Please enter the correct details.")

    # Redirect to the same page to avoid resubmission on refresh
    # return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect("%s#footer" % request.META.get('HTTP_REFERER', '/'))

