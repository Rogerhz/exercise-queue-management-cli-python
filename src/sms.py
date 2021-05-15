# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC5232f8d0ea1887f94610e990d4f0ad64'
    auth_token = '2cda0ade1e282dfce4e60afff531ddbc'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+12169302626',
                        to='+'+to
                    )

    print(message.sid)