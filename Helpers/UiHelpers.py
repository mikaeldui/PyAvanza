__author__ = 'mikbol0113'

import os

class UiHelpers:

    @staticmethod
    def ClearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == 'nt':
            os.system('color F2')

        print("============================================")
        print("==                                        ==")
        print("==              AVANZA BANK               ==")
        print("==                                        ==")
        print("============================================")
