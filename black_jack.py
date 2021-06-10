import random
import logo
print(logo.logo)
deck=[11,2,3,4,5,6,7,8,9,10,10,10]
start= input('Do you want to play black_jack?Yes/No:\n').lower()
if start=='yes':
    pass
else:
    quit()

def black_jack():
    #user deck made here
    user_card=[]
    user_card.append(random.choice(deck))
    user_card.append(random.choice(deck))
    print(f'User deck is {user_card}')
    # computer deck made here
    computer_cards=[]
    computer_cards.append(random.choice(deck))
    print(f'Computer deck is {computer_cards}')
    # Game continues
    game_continue=True
    while game_continue==True:
        play_more=(input('Do you want to continue? yes or no')).lower()

        if play_more=='yes':
            user_card.append(random.choice(deck))
        else:
            computer_cards.append(random.choice(deck))
            game_continue=False    
    sum1=0
    sum2=0
    for i in user_card:
        sum1+=i
    for i in computer_cards:
        sum2+=i
    if 11 in (user_card or computer_cards) and (sum1 or sum2) > 21:
        if 11 in user_card:
            user_card.pop(11)
            user_card.append(1)
        elif 11 in computer_cards:
            computer_cards.append(11)
            computer_cards.pop(1)
            

    if sum1==21 and len(user_card)==2:
        print('You got blackjack you win!!')


    elif (sum1>sum2) and (sum1<21):

        print(f'Your cards are {user_card} and computer cards are {computer_cards}')
        print('You win')
    elif (sum2>sum1 and sum2<21) or (sum1>21):
        print(f'Your cards are {user_card} and computer cards are {computer_cards}')
        print('You lose')  
               
    elif sum1==sum2:
        print('Your cards are {user_card} and computer cards are {computer_cards}')
        print('Its a draw')
# Calling the function
black_jack()
#Do you want to play again.
play_again=('Do you want to play again? Yes or no \n').lower()
if play_again=='yes':
    black_jack()
else:
    quit()    
