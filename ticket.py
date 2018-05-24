TICKET_PRICE = 10
tickets_remaining = 100
service_charge = 2

def calculate_price(number_of_tickets):
  return (number_of_tickets * TICKET_PRICE) + service_charge
  
while tickets_remaining >= 1:
  print('There are {} tickets remaining'.format(tickets_remaining))
  name = input('What is your name?')
  num_tickets = input('How many tickets would you like, {}:'.format(name))
  try:
    num_tickets = int(num_tickets)
    if num_tickets > tickets_remaining:
      raise ValueError('Your demand is too high!')
  except ValueError as err:
    print("Oh no! We ran into issue! {}".format(err))
    print('')
  else:
    amount_due = calculate_price(num_tickets)
    print('The total due is ${}'.format(amount_due))
    should_proceed = input('Do you want to proceed? Y/N ')
    if should_proceed.lower() == 'y':
      print('SOLD!')
      print('Come back next time!')
      print('')
      tickets_remaining -= num_tickets
    else:
      print('Thank You {}'.format(name))

print('There are no tickets left')
