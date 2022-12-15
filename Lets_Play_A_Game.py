class Game:

  import colorama
  from colorama import Fore
  import sys,time,random
  import sys,time
  
def delprint():
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.1)


    
name = input_slow(colorama.Fore.RED + 'What is your name?: '+ colorama.Fore.RESET)

print_slow(Fore.RED + 'Hello '+ name + '!')
print()

answers = input_slow(colorama.Fore.RED + 'Lets play a game: '+ colorama.Fore.RESET)

if answers == 'Yes':
  print_slow(Fore.RED + 'Awesome!')
elif answers == 'No':
    print_slow(Fore.RED + 'Goodbye!')

print()
  
play = input(colorama.Fore.RED + 'Should we play Cards or Hangman ' + colorama.Fore.RESET)
  
print()
  
if play == 'Cards':
  print(Fore.RED + 'Let\'s play Cards!')
