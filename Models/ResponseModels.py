class AccountDetails:
    AccountId = ""
    AccountName = ""
    AdjustedForwardAmount = ""
    Balance = ""
    CreditLimit = ""
    CurrencyAccounts = list()
    """:type : list[CurrencyAccount]"""
    InterestAmount = ""
    LoanAmount = ""
    OwnCapital = ""
    PositionAggregations = list()
    """:type : list[PositionAggregation]"""
    ResAmount = ""
    SecAmount = ""
    SuperInterest = ""
    TotalAccruedInterest = ""
    TotalMarginRequirement = ""
    TotalProfit = ""
    TotalProfitPercent = ""
    TotalValue = ""
    TradingPower = ""
    UnUsedCredit = ""

class AccountNameAndId:
    AccountId = ""
    AccountName = ""
    TradingPower = ""

class AccountOverviewResponse:
    Accounts = list()
    """:type : list[AccountDetails]"""
    TotalOwnCapital = None

class ContactInfo:
    Phone = ""
    PostalAddress = ""
    VisitingAddress = ""

class CurrencyAccount:
    AccountId = None
    Balance = None
    Currency = None

class Deal:
    Amount = ""
    Id = ""
    InstrumentName = ""
    Price = ""
    Reference = ""
    Time = ""
    Type = ""
    Volume = ""

class DeleteOrderResponse:
    Message = ""
    Result = False

class DepotChartData:
    AccountDataList = ""
    IndexDataList = ""
    IndexName = ""

class IndexCategory:
    CategoryName = ""
    OrderbookIds = ""

class IndexCategoryResponse:
    IndexCategories = list()
    """:type :list[IndexCategory]"""

class IndexDetails:
    IndexInfo = ""
    OneYearHighest = ""
    OneYearLowest = ""
    ThreeMonthHighest = ""
    ThreeMonthLowest = ""
    UpdateInfo = ""

class Instrument:
    InstrumentName = ""
    OrderbookId = ""
    Quote = ""

class NewsItem:
    Body = ""
    Id = ""

class NewsListItem:
    Category = ""
    Headline = ""
    Id = ""
    PublishDate = ""
    Source = ""

class Order:
    Amount = ""
    Id = ""
    InstrumentName = ""
    OrderType = ""
    Price = ""
    Reference = ""
    Status = ""
    ValidTo = ""
    Volume = ""

class OrderDepthLevel:
    BuyPrice = ""
    BuyVolume = ""
    BuyWidth = ""
    BuyLevel = ""
    SellPrice = ""
    SellVolume = ""
    SellWidth = ""

class OrderResultResponse:
    Message = ""
    Result = False

class OrdersAndDealsResponse:
    Deals = ""
    Orders = ""

class OrderViewResponse:
    AccountId = ""
    Ask = ""
    Bid = ""
    DefaultValidTo = ""
    InstrumentName = ""
    MaxValidDays = ""
    Message = ""
    Tradeable = False
    TradingPower = ""

class Position:
    AverageAcquiredPrice = ""
    Change = ""
    ExpiryDate = ""
    InstrumentName = ""
    InstrumentType = ""
    MarketValue = ""
    Modified = ""
    OrderbookId = 0
    Price = ""
    Profit = ""
    ProfitPercent = ""
    Tradable = ""
    Volume = ""

class PositionAggregation:
    InstrumentType = 0
    InstrumentTypeName = None
    Positions = list()
    """:type : list[Position]"""
    TotalAverage = None
    TotalChange = None
    TotalProfit = None
    TotalProfitPercent = None
    TotalValue = None

class Quote:
    Ask = ""
    Bid = ""
    Change = ""
    ChangePercent = ""
    HighPrice = ""
    InstrumentName = ""
    LastPrice = ""
    LowPrice = ""
    OrderbookId = ""
    Time = ""
    TotaltQuantityTraded = ""
    Type = ""

class Splash:
    SplashScreenText = ""

class Trade:
    BuyBroker = ""
    Price = ""
    SellBroker = ""
    Time = ""
    Volume = ""

class TradeChartData:
    PrimaryDataList = -1
    SecondaryDataList = -1


