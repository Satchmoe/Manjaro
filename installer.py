#!/usr/bin/env python3

import os

pacman = "sudo pacman -S --needed"
yaourt = "yaourt -S --needed"


class List(object):

    def install(install, name):
        print("Installing {} Software...".format(name))
        try:
            os.system(install)
        except Exception as e:
            print('Error Installing')
        finally:
            input('\nEnter to continue:')
            menu()

    def Exit():
        os.system('clear')
        print('Exit!!! \n')

    def Development():
        List.install('{0} atom geany git terminator redshift \
                    && {1} redshift-qt'.format(pacman, yaourt), 'Development')

    def Internet():
        List.install('{0} chromium \
                    && {1} chromium-widevine pepper-flash teamviewer skype \
                    '.format(pacman, yaourt), 'Internet')

    def Media():
        List.install('{} mpv mplayer smtube'.format(pacman), 'Media')

    def Game():
        choice = input('Do you want to install just the apps or full setup'
                       ' [y=full/n=apps]')
        if choice != 'y':
            List.install('{0} dosbox wine winetricks q4wine playonlinux mono \
                        smplayer gimp lib32-libldap lib32-gnutls lib32-lcms2 \
                        && {1} ttf-ms-fonts'.format(pacman, yaourt), 'Game')
        else:
            List.install('{0} dosbox wine winetricks q4wine playonlinux mono \
                        smplayer gimp lib32-libldap lib32-gnutls lib32-lcms2 \
                        && {1} ttf-ms-fonts gstreamer0.10-{{bad,good,ugly,base} \
                        {,-plugins},ffmpeg}'.format(pacman, yaourt), 'Game')
            os.system('winetricks corefonts hosts winhttp wininet vcrun2015')

    Menu_list = {0: Exit,
                 1: Development,
                 2: Internet,
                 3: Media,
                 4: Game
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
        menu()


def update():
    """Ranking mirrors, Optimize, and Sync database"""
    os.system('clear')
    choice = input('Would you like to Improve download speed [y/n]: ')
    if choice == 'y':
        os.system('sudo pacman-mirrors -g && sudo pacman -Syy \
                && sudo pacman-optimize && sync')
        input('Press Enter to continue....')
        menu()
    else:
        menu()


def main():
    update()


if __name__ == "__main__":
    main()
