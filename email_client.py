
import os
from time import sleep
from jinja2 import Environment, FileSystemLoader
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def html(santa, person):
    j2_env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    return j2_env.get_template('mailtemplate.html').render(giver=santa, receiver=person)

def sendEmail(santa, person):
    subject = 'Secret Santa \'23'
    mail_body = html(santa, person)

    santa_temp = santa.get_username()
    file = open(santa_temp + ".html", "w")
    file.write(mail_body)
    file.close()

    send_email(santa, subject, mail_body)
    return

def send_email(santa, subject, content_html):
    sleep(1)

    message = Mail(
        from_email="rameez2612@gmail.com",
        # to_emails=santa.email,
        to_emails=["rameez2612+santa@gmail.com"],
        subject=subject,
        html_content=content_html
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e.message)


def fire_emails(ss_list):
	for santa, santee in ss_list:
		sendEmail(santa, santee)