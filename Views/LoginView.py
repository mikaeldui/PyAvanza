__author__ = 'mikbol0113'

from Helpers.UiHelpers import UiHelpers
from AvanzaApi import AvanzaApi
import getpass

UiHelpers.ClearScreen()

contactInfo = AvanzaApi.API.About.GetContactInfo()

print("== Telefonnummer: " + contactInfo.Phone + (" " * (44 - 2 - 18 - len(contactInfo.Phone))) + "==")
print("============================================")
print("")

username = input("Username: ")
password = getpass.getpass()

AvanzaApi.HELPER.AddCredentials(username, password)

import Views.AccountsView