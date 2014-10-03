__author__ = 'mikbol0113'

import Models.ResponseModels
from AvanzaHelper import AvanzaHelper

class AvanzaApi:
    BASE_IP_DEBUG = "betatest.avanza.se"
    BASE_IP_RELEASE = "iphone.avanza.se"
    BASE_URL_PREFIX = "https://"
    BASE_URL_SUFFIX = "/iphone-ws/"
    IS_LIVE = True
    HELPER = AvanzaHelper("")

    API = None

    def __init__(self):
        baseUrl = AvanzaApi.BASE_URL_PREFIX
        if AvanzaApi.IS_LIVE:
            baseUrl += AvanzaApi.BASE_IP_RELEASE
        else:
            baseUrl += AvanzaApi.BASE_IP_DEBUG
        baseUrl += AvanzaApi.BASE_URL_SUFFIX

        AvanzaApi.HELPER = AvanzaHelper(baseUrl)

    @staticmethod
    def Init():
        AvanzaApi.API = AvanzaApi()

    class About:

        @staticmethod
        def GetContactInfo():
            response = AvanzaApi.HELPER.Get(AvanzaApi.HELPER.RelativeUrl("about/contact"))
            contactInfo = Models.ResponseModels.ContactInfo()
            contactInfo.Phone = response["phone"]
            contactInfo.PostalAddress = response["postalAddress"]
            contactInfo.VisitingAddress = response["visitingAddress"]

            return contactInfo

        @staticmethod
        def GetSplash():
            response = AvanzaApi.HELPER.Get(AvanzaApi.HELPER.RelativeUrl("about/splash"))
            splash = Models.ResponseModels.Splash()
            splash.SplashScreenText = response["splashScreenText"]

            return splash

    class Account:

        @staticmethod
        def AccountDetails(i):
            """:type i:int"""

            response = AvanzaApi.HELPER.Get(AvanzaApi.HELPER.RelativeUrl("account/details/" + str(i)))

            acc = Models.ResponseModels.AccountDetails()
            acc.AccountId = response["accountId"]
            acc.AccountName = response["accountName"]
            acc.AdjustedForwardAmount = response["adjustedForwardAmount"]
            acc.Balance = response["balance"]
            acc.CreditLimit = response["creditLimit"]
            acc.InterestAmount = response["interestAmount"]
            acc.LoanAmount = response["loanAmount"]
            acc.UnUsedCredit = response["unUsedCredit"]
            acc.TradingPower = response["tradingPower"]
            acc.TotalValue = response["totalValue"]
            acc.TotalProfitPercent = response["totalProfitPercent"]
            acc.TotalProfit = response["totalProfit"]
            acc.TotalMarginRequirement = response["totalMarginRequirement"]
            acc.TotalAccruedInterest = response["totalAccruedInterest"]
            acc.SuperInterest = response["superInterest"]
            acc.SecAmount = response["secAmount"]

            for cAccount in response["currencyAccounts"]:
                cAcc = Models.ResponseModels.CurrencyAccount()
                cAcc.AccountId = cAccount["accountId"]
                cAcc.Balance = cAccount["balance"]
                cAcc.Currency = cAccount["currency"]
                acc.CurrencyAccounts.append(cAcc)
            for pAggregation in account["positionAggregations"]:
                pAgg = Models.ResponseModels.PositionAggregation()
                pAgg.InstrumentType = int(pAggregation["instrumentType"])
                pAgg.InstrumentTypeName = pAggregation["instrumentTypeName"]
                pAgg.TotalAverage = pAggregation["totalAverage"]
                pAgg.TotalChange = pAggregation["totalChange"]
                pAgg.TotalProfit = pAggregation["totalProfit"]
                pAgg.TotalProfitPercent = pAggregation["totalProfitPercent"]
                pAgg.TotalValue = pAggregation["totalValue"]
                for position in pAggregation["positions"]:
                    pos = Models.ResponseModels.Position()
                    pos.AverageAcquiredPrice = position["averageAcquiredPrice"]
                    pos.Change = position["change"]
                    pos.ExpiryDate = position["expiryDate"]
                    pos.InstrumentType = position["instrumentType"]
                    pos.InstrumentName = position["instrumentName"]
                    pos.MarketValue = position["marketValue"]
                    pos.Modified = position["modified"]
                    pos.OrderbookId = position["orderbookId"]
                    pos.Price = position["price"]
                    pos.Profit = position["profit"]
                    pos.ProfitPercent = position["profitPercent"]
                    pos.Tradable = position["tradable"]
                    pos.Volume = position["volume"]
                    pAgg.Positions.append(pos)
                acc.PositionAggregations.append(pAgg)

            return acc


        @staticmethod
        def AccountOverview():
            response = AvanzaApi.HELPER.Get(AvanzaApi.HELPER.RelativeUrl("account/overview/all"))

            overview = Models.ResponseModels.AccountOverviewResponse()

            # success? Then save the credentials and return a response

            overview.TotalOwnCapital = response["totalOwnCapital"]

            for account in response["accounts"]:
                acc = Models.ResponseModels.AccountDetails()
                acc.AccountId = account["accountId"]
                acc.AccountName = account["accountName"]
                acc.AdjustedForwardAmount = account["adjustedForwardAmount"]
                acc.Balance = account["balance"]
                acc.CreditLimit = account["creditLimit"]
                acc.InterestAmount = account["interestAmount"]
                acc.LoanAmount = account["loanAmount"]
                acc.UnUsedCredit = account["unUsedCredit"]
                acc.TradingPower = account["tradingPower"]
                acc.TotalValue = account["totalValue"]
                acc.TotalProfitPercent = account["totalProfitPercent"]
                acc.TotalProfit = account["totalProfit"]
                acc.TotalMarginRequirement = account["totalMarginRequirement"]
                acc.TotalAccruedInterest = account["totalAccruedInterest"]
                acc.SuperInterest = account["superInterest"]
                acc.SecAmount = account["secAmount"]

                for cAccount in account["currencyAccounts"]:
                    cAcc = Models.ResponseModels.CurrencyAccount()
                    cAcc.AccountId = cAccount["accountId"]
                    cAcc.Balance = cAccount["balance"]
                    cAcc.Currency = cAccount["currency"]
                    acc.CurrencyAccounts.append(cAcc)
                for pAggregation in account["positionAggregations"]:
                    pAgg = Models.ResponseModels.PositionAggregation()
                    pAgg.InstrumentType = int(pAggregation["instrumentType"])
                    pAgg.InstrumentTypeName = pAggregation["instrumentTypeName"]
                    pAgg.TotalAverage = pAggregation["totalAverage"]
                    pAgg.TotalChange = pAggregation["totalChange"]
                    pAgg.TotalProfit = pAggregation["totalProfit"]
                    pAgg.TotalProfitPercent = pAggregation["totalProfitPercent"]
                    pAgg.TotalValue = pAggregation["totalValue"]
                    for position in pAggregation["positions"]:
                        pos = Models.ResponseModels.Position()
                        pos.AverageAcquiredPrice = position["averageAcquiredPrice"]
                        pos.Change = position["change"]
                        pos.ExpiryDate = position["expiryDate"]
                        pos.InstrumentType = position["instrumentType"]
                        pos.InstrumentName = position["instrumentName"]
                        pos.MarketValue = position["marketValue"]
                        pos.Modified = position["modified"]
                        pos.OrderbookId = position["orderbookId"]
                        pos.Price = position["price"]
                        pos.Profit = position["profit"]
                        pos.ProfitPercent = position["profitPercent"]
                        pos.Tradable = position["tradable"]
                        pos.Volume = position["volume"]
                        pAgg.Positions.append(pos)
                    acc.PositionAggregations.append(pAgg)
                overview.Accounts.append(acc)

            return overview

        @staticmethod
        def Login(username, password):
            AvanzaApi.HELPER.AddCredentials(username, password)

            return AvanzaApi.Account.AccountOverview()

    class Instruments:

        @staticmethod
        def IndexCategories():
            response = AvanzaApi.HELPER.Get(AvanzaApi.HELPER.RelativeUrl("instruments/indexCategories"))

            categoriesResponse = Models.ResponseModels.IndexCategoryResponse()

            for category in response:
                cat = Models.ResponseModels.IndexCategory()
                cat.CategoryName = category["categoryName"]
                cat.OrderbookIds = category["orderbookIds"]
                categoriesResponse.IndexCategories.append(cat)

            return categoriesResponse