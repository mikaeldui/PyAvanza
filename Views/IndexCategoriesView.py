__author__ = 'mikbol0113'

from AvanzaApi import AvanzaApi
from Helpers.UiHelpers import UiHelpers

UiHelpers.ClearScreen()

print("")
print("================ INDEXKATEGORIER ====================")

categories = AvanzaApi.API.Instruments.IndexCategories()

for category in categories:
    print(category)