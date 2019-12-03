from twilio.rest import Client

acc_id = 'AC2d6e0a4e450d17f6ee5e6859202a295a'
auth_token = 'check later'

jo_client = Client(acc_id, auth_token)

nubs = ['+12405955599', '+19786970682','+15084397808','+18572048762']

for nub in nubs:
  message = jo_client.messages.create(
    body = 'Wanna escape Cogo Labs? Check out zam.monster or callmezaddyjo.vip for your next career milestone.',
    from_ = '+15403182210',
    to = nub
  )
  print(message.sid)


