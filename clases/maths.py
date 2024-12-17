from typing import Union


def value_of_card(card):
    if card == 'K':
      return 10
    elif card == 'J':
      return 10
    elif card == 'Q':
      return 10
    elif card == 'A' :
      return 1
    else:
      return card 

print(value_of_card(''))


def higher_card(card_one : str, card_two : str) -> Union[str,tuple]   :
 As = ['A']
 letter = ['Q','K','J','10']
 
 if value_of_card(card_one) > value_of_card(card_two):
   return card_one
 elif value_of_card(card_one) < value_of_card(card_two):
   return card_two
 else: return card_one,card_two
 
 
print(higher_card('9','10'))

numero = 789
def value_of_ace(card_one, card_two):
  
    
  if card_one == 'A' or card_two == 'A':
    return 1
  elif (int(value_of_card(card_one)) + int(value_of_card(card_two))) <= 10:
    return 11
  else: 
    return 1
  
print(value_of_ace('5','5'))
    
