__author__ = 'mikbol0113'

from AvanzaApi import AvanzaApi
from Helpers.UiHelpers import UiHelpers


UiHelpers.ClearScreen()


print("")
print("================ KONTON ====================")

overview = AvanzaApi.API.Account.Login(AvanzaApi.HELPER.USERNAME, AvanzaApi.HELPER.USERNAME)

for account in overview.Accounts:
    print("==== " + account.AccountName + ", " + str(account.AccountId) + ", " + str(account.Balance) + " SEK" + " ====")
    for agg in account.PositionAggregations:
        print("")
        print(" Namn              \t", "Inköpspris   \t", "Förändring\t", "Förändring i %\t")
        print("")
        for pos in agg.Positions:
            addToName = ""
            if len(pos.InstrumentName) < 15:
                addToName = " " * 10
            print("", pos.InstrumentName + addToName, "\t", pos.MarketValue, "SEK   \t", pos.Profit, "SEK\t", pos.ProfitPercent, "%")

        print("=" + agg.InstrumentTypeName + "            \t", str(agg.TotalValue) + "SEK \t", "")

input()

import Views.IndexCategoriesView