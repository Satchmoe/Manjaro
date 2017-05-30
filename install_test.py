#!/usr/bin/env python3

import os
import time


class List(object):

    def Exit():
        os.system('clear')
        print('Exit!!! \n')

    def Development():
        print("Installing Development Software...")
        try:
            os.system('sudo pacman -S --needed atom geany git')
        except Exception as e:
            print('Error Installing')
        finally:
            input('\nEnter to continue:')
            menu()

    def I3wm():
        print("I3wm")
        time.sleep(3)
        menu()

    def Atom_Text_Editor():
        print("Atom")
        time.sleep(3)
        menu()

    Menu_list = {0: Exit,
                 1: Development,
                 2: I3wm,
                 3: Atom_Text_Editor
                 }


def menu():
    """Display dictionary 'Menu_list' in List class as a menu"""
    os.system('clear')
    Selection = 1
    print('Installtion Menu: \n')
    for k, v in List.Menu_list.items():
        print(k, '=', v.__name__)

    try:
        Selection = int(input("\nSelect a Number: "))
        if (Selection >= 0):
            List.Menu_list[Selection]()
    except Exception as e:
        print("Not a selection \nTry again: \n")
        input('Press Enter to continue....')
        main()


def main():
    menu()


if __name__ == "__main__":
    main()
