# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='raksedakeerthi@gmail.com',
    to_emails='santhanaselvimoorthy06@psnacet.edu.in',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
