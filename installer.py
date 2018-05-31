#!/usr/bin/env python3

"""
Program: Install software for Manjaro Linux.
Programmer: Chevelle
Date created: 06-03-2017
Date Updated: 05-29-2018
Version: 1.0.1  (major.minor.fixes)
Tested: Manjaro Linux 17.0.1 = worked
Purpose: Fast way to install/configure new installed Manjaro distro.
Description: Install software, configure wine on game side.
Notes:
"""

import os

pacman = "sudo pacman -S --needed"
yaourt = "yaourt -S --needed"


class List():

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
        choice = str(input('Do you want to install just the apps or full setup'
                           '[y=full/N=apps]: '))
        if choice in ('y', 'ye', 'yes'):
            List.install('{0} dosbox wine winetricks q4wine playonlinux mono \
                        smplayer gimp lib32-libldap lib32-gnutls lib32-lcms2 \
                        && {1} ttf-ms-fonts gstreamer0.10-bad \
                        gstreamer0.10-bad-plugins gstreamer0.10-good \
                        gstreamer0.10-good-plugins gstreamer0.10-ugly \
                        gstreamer0.10-ugly-plugins gstreamer0.10-base \
                        gstreamer0.10-base-plugins \
                        '.format(pacman, yaourt), 'Game-full')
            os.system('winetricks corefonts hosts winhttp wininet vcrun2015')
        else:
            List.install('{0} dosbox wine winetricks q4wine playonlinux mono \
                        smplayer gimp lib32-libldap lib32-gnutls lib32-lcms2 \
                        && {1} ttf-ms-fonts'.format(pacman, yaourt), 'Game')

    Menu_list = {0: Exit,
                 1: Development,
                 2: Internet,
                 3: Media,
                 4: Game
                 }


def menu():
    """Display dictionary 'Menu_list' in List class as a menu."""
    os.system('clear')
    Selection = 1
    print('Installtion Menu: \n')
    for k, v in List.Menu_list.items():
        print(k, '=', v.__name__)

    try:
        Selection = int(input("\nSelect a Number: "))
        if Selection >= 0:
            List.Menu_list[Selection]()
    except Exception as e:
        print("Not a selection \nTry again: \n")
        input('Press Enter to continue....')
        menu()


def update():
    """Ranking mirrors, Optimize, and Sync database."""
    os.system('clear')
    choice = input('Would you like to Improve download speed [y/N]: ')
    if choice in ('y', 'ye', 'yes'):
        os.system('sudo pacman-mirrors --fasttrack && sudo pacman -Syy \
                && sudo pacman-optimize && sync')
        input('Press Enter to continue....')
        menu()
    else:
        menu()


def main():
    update()


if __name__ == "__main__":
    main()
