from django.core.mail import EmailMessage
import random
import string


class Util:
    def send_email(data):
        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        sent = email.send()
        # return True

    def get_random_string(length):
    # With combination of lower and upper case
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for i in range(length))
        print("password", password)
        # result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        # print random string
        return password