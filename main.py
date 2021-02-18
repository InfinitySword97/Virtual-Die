import random
import time
import turtle
print('D for Dice')
print('T for Turtle in progress')
ChooseTool = input('Please choose the tool you want to use Tool:')

if ChooseTool == 'D':
  ConfirmDice=input('Are you sure you want to roll the dice? Enter y for yes and n for no. ')
if ConfirmDice == 'y': 
    b = int(input('How many sides does your die have? please input a number '))
    while True:
      x = random.randint(1, b)
      print('Your number is...')
      time.sleep(0.1)
      print(x)
      reroll = input('Would you like to reroll? Enter y for yes and n for no. ')
      if reroll == 'y':
          continue
      else:
          ConfirmEndofProgram = input(
              'Are you sure you want to leave? Input y for yes and n for no '
            )
          if ConfirmEndofProgram == 'y':
                print('Bye!')
                time.sleep(1)
                break
          else:
                continue

if ChooseTool == 'T':
  turtle.forward(100)
                  