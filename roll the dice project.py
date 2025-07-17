import random

while True:
    choice = input('Roll the dice? (y/n): ').lower() 
    
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print('You rolled...')
        print(f'({die1}, {die2})')
    elif choice == 'n':
         die1 = random.randint(1, 6)
         die2 = random.randint(1, 6)
         print('You rolled...')
         print(f'({die1}, {die2})')
         print('THANKS FOR PLAYING HAVE A GOOD DAY....')
         break
    else:
        print('Invalid choice. Please enter "y" to roll or "n" to quit.')
