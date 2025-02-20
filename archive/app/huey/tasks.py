from app.utilities.email_service import EmailService, EmailServiceSettings
from . import run


@run.task()
def send_email(
    email_service_settings: EmailServiceSettings,
    email_to: list[str],
    email_subject: str,
    email_message: str,
) -> None:
    print("SENDING EMAIL")
    email_service = EmailService(email_service_settings)
    email_service.recipients(email_to).subject(email_subject).body(email_message)
    email_service.send()
    return
