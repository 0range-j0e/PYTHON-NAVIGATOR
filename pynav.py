#!/usr/bin/python3

import os
import colorama
import sys
import readline

''' The goal of this program is to simplify the navigation of the Linux filesystem within Terminal. '''
__author__ = "0range-j0e"
__copyright__ = "0range-j0e"
__version__ =  "1.0"


# Initialize color variables from Colorama library for ease of coding.
black, red, white, green, yellow, cyan,  white, magenta, dim, bright, normal, reset = colorama.Fore.BLACK, colorama.Fore.RED, colorama.Fore.WHITE, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.CYAN, colorama.Fore.WHITE, colorama.Fore.MAGENTA, colorama.Style.DIM, colorama.Style.BRIGHT, colorama.Style.NORMAL, colorama.Style.RESET_ALL  

# Define the maximum amount of directories and files to be listed in each column.
column_max = 20  

# If set to False, terminal will not clear with each user command. 
auto_clear = False


def macro(directory, columns_max):
    
    if auto_clear is True:
        os.system('clear')

    print("-----------------------")
    print(f"Directory:", os.getcwd() + "\n")

    # Variables and formulas to send contents of present working directory to columns a, b, and c, defined as ca, cb, and cc below. 
    ca = 0
    cb = (column_max)
    cc = (column_max*2)
    num_string = str(len(directory)/(column_max*3))
    
    for i in range(len(num_string)):
        if '.' in num_string[i]:
            integer, decimal = (int(num_string[:i])), (float(num_string[i:]))
    
    if decimal < .34:
        sub_sequences = ((integer*3)+1)
    elif decimal < .67:
        sub_sequences = ((integer*3)+2)
    else:
        sub_sequences = ((integer*3)+3)
    
    starter_subsequence = sub_sequences


    if decimal != .0:
        sequences = integer + 1

    else:
        sequences = integer

    while True:
    
        if sub_sequences >= 3:

            for i in range(column_max):
                try:
                    sys.stdout.write( white + '{:<5s}'.format('['+str(ca)+']') +   white + bright + reset + '{:<45s}'.format(directory[ca]) +  white + '{:<5s}'.format('['+str(cb)+']') +   white + bright + reset + '{:<45s}'.format(directory[cb]) +  white + '{:<5s}'.format('['+str(cc)+']') +   white + bright + reset + '{:<45s}'.format(directory[cc]) + '\n')
                    sys.stdout.flush()
                    ca += 1 
                    cb += 1
                    cc += 1 
                except:
                    sys.stdout.write( white + '{:<5s}'.format('['+str(ca)+']') +   white + bright + reset + '{:<45s}'.format(directory[ca]) +  white + '{:<5s}'.format('['+str(cb)+']') +   white + bright + reset + '{:<45s}'.format(directory[cb]) + '\n')
                    ca += 1 
                    cb += 1
             
            sub_sequences -= 3

            print("")

            ca += (column_max *2)
            cb += (column_max *2)
            cc += (column_max *2)
        else: 
            break



    while True:
                
        if sub_sequences == 2:

            if starter_subsequence > 3:
            
                for i in range(column_max):
                    try:
                        sys.stdout.write( white + '{:<5s}'.format('['+str(cb)+']') +   white + bright + reset + '{:<45s}'.format(directory[cb]) +  white + '{:<5s}'.format('['+str(cc)+']') +   white + bright + reset + '{:<45s}'.format(directory[cc]) + '\n')
                        ca += 1 
                        cb += 1
                    except:
                        sys.stdout.write( white + '{:<5s}'.format('['+str(ca)+']') +   white + bright + reset + '{:<45s}'.format(directory[ca]) + '\n') 
                        ca += 1

            else:
            
                for i in range(column_max):
                    try:
                        sys.stdout.write( white + '{:<5s}'.format('['+str(ca)+']') +   white + bright + reset + '{:<45s}'.format(directory[ca]) +  white + '{:<5s}'.format('['+str(cb)+']') +   white + bright + reset + '{:<45s}'.format(directory[cb]) + '\n')
                        ca += 1 
                        cb += 1
                    except:
                        sys.stdout.write( white + '{:<5s}'.format('['+str(ca)+']') +   white + bright + reset + '{:<45s}'.format(directory[ca]) + '\n') 
                        ca += 1

            sub_sequences -= 2
            print("")

            ca += (column_max *2)
            cb += (column_max *2)
            cc += (column_max *2)
        

        elif sub_sequences == 1:

            if starter_subsequence > 3:

                for i in range(column_max):
                    try:
                        sys.stdout.write(f'[{str(cc)}] {directory[cc]}' + '\n')
                        cc += 1
                    except Exception as e:
                        pass
                
                sub_sequences -= 1

            else:

                for i in range(column_max):
                    try:
                        sys.stdout.write(f'[{str(ca)}] {directory[ca]}' + '\n')
                        ca += 1
                    except Exception as e:
                        pass
            print("")
            
        break

                

''' The heart of it all, the Python Navigator. Directory listings are placed in a dictionary and assigned a key.
If the key is linked to a directory, the program will navigate to that directory. If the key is linked to a file, the
program will open the file using the xdg-open utility. A user can also type their own commands just as if they were in
a regular terminal. For example, if a user would like to run a python script, they would simply enter python3 <file>.
'''

def Navigator(column_max):
    
    while True:
        
        directory = {}

        for i, j in enumerate(os.listdir()):
            directory[i] = j

        try:
            macro(directory, column_max)
        except:
            pass

        
        # Take user input
        command = input()

        # Checks if the user input is a digit. Will attempt to change to directory first. If digit is not assigned to a directory, program will attempt to run file with xdg-open.
        if command.isdigit() is True:
            for key, content in directory.items():
                if int(command) == key:
                    try:
                        os.chdir(directory[key])
                    except:
                        os.system(f'xdg-open "{directory[key]}"')
                    finally:
                        pass


        # Check if the user input is a string.
        elif type(command) is str:
            
            # If 'cd' is in command, try to run the command as usual, but if there is an error print 'invalid directory'.
            if 'cd' in command:

                try:
                    os.chdir(command[3:])
                except:
                    print('invalid diretory')

            
            # If inputted string matches the name of a file or directory, attempt to open a directory and if that fails, attempt to open file with xdg-open. 
            elif command in os.listdir(): 
                try:
                    os.chdir(command)
                except:
                    os.system(f"xdg-open " + "'{command}'")
                finally:
                    pass

            # Function to find content within columns. Needs to be fixed. 
            elif 'find' in command:
                aggregator = {}
                x = 0 
                string_to_find = command[5:]
                for key, content in directory.items():
                    if string_to_find in content:
                        aggregator[x] = content
                        x += 1

                if len(aggregator) > 0:
                    macro(aggregator, column_max)

            # If user input is 'b', program will move back a directory.
            elif command.lower() in ['b', 'back']:
                os.chdir('..')

            # If none of the above parameters are met, program will run with default system command. 
            else:
                os.system(command)
                 

Navigator(column_max)

