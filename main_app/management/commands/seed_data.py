from enum import StrEnum, auto
from typing import NamedTuple

from main_app.enums import CurrencyKind, TagKind


# Row definitions
class ProfileRow(NamedTuple):
    name: str
    alias: str

class CurrencyRow(NamedTuple):
    name: str
    label: str
    kind: CurrencyKind

class TagRow(NamedTuple):
    name: str
    label: str
    kind: TagKind
    order_index: int

class AccountRow(NamedTuple):
    name: str
    label: str
    owner_key: str
    currency_key: str
    tag_key: str


# Seed keys
class SeedProfile(StrEnum):
    demo = 'demo_user'

class SeedCurrency(StrEnum):
    usd = auto()
    eur = auto()
    mxn = auto()
    pt = auto() # points
    us_tb = auto() # US treasure bonds
    appstk = auto() # Apple stocks
    btc = auto() # Bitcoin
    reit = auto() # Real Estate Investment Trusts

class SeedTag(StrEnum):
    cash = auto()
    debits = auto()
    reserved = auto()
    savings = auto()
    receivables = auto()
    gov_bonds = auto()
    cryptos = auto()
    investments = auto()
    funds = auto()
    credits = auto()
    payables = auto()
    loans = auto()

class SeedAccount(StrEnum):
    cash_usd = auto()
    cash_eur = auto()
    cash_mxn = auto()
    payroll_usd = auto()
    bank1d = auto()
    bank2d = auto()
    bank1r = auto()
    bank2r = auto()
    bank1s = auto()
    bank2s = auto()
    us_treasb = auto()
    apple_stock = auto()
    btc_wallet = auto()
    retirement_fund = auto()
    amex_card = auto()
    visacard = auto()
    mastercard = auto()


# Data functions
def get_profiles() -> list[ProfileRow]:
    return [
        ProfileRow(
            SeedProfile.demo,
            'John Doe',
        ),
    ]

def get_currencies() -> list[CurrencyRow]:
    return [
        CurrencyRow(
            SeedCurrency.usd,
            'USD',
            CurrencyKind.FIAT,
        ),
        CurrencyRow(
            SeedCurrency.eur,
            'EUR',
            CurrencyKind.FIAT,
        ),
        CurrencyRow(
            SeedCurrency.mxn,
            'MXN',
            CurrencyKind.FIAT,
        ),
        CurrencyRow(
            SeedCurrency.pt,
            'Rewards points',
            CurrencyKind.POINT_UNITS,
        ),
        CurrencyRow(
            SeedCurrency.us_tb,
            'US treasure bonds',
            CurrencyKind.BOND_UNITS,
        ),
        CurrencyRow(
            SeedCurrency.appstk,
            'Apple stocks',
            CurrencyKind.EQUITY_UNITS,
        ),
        CurrencyRow(
            SeedCurrency.btc,
            'Bitcoin',
            CurrencyKind.CRYPTO_UNITS,
        ),
        CurrencyRow(
            SeedCurrency.reit,
            'Real state',
            CurrencyKind.COMMODITY_UNITS,
        ),
    ]

def get_tags() -> list[TagRow]:
    return [
        TagRow(
            SeedTag.cash,
            'Cash',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.receivables,
            'Receivables',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.debits,
            'Debits',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.reserved,
            'Reserved',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.savings,
            'Savings',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.gov_bonds,
            'Gov_bonds',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.cryptos,
            'Cryptos',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.investments,
            'Investments',
            TagKind.ASSETS,
            1,
        ),
        TagRow(
            SeedTag.funds,
            'Funds',
            TagKind.PORTAFOLIO_ASSETS,
            1,
        ),
        TagRow(
            SeedTag.credits,
            'Credits',
            TagKind.LIABILITIES,
            1,
        ),
        TagRow(
            SeedTag.payables,
            'Payables',
            TagKind.LIABILITIES,
            1,
        ),
        TagRow(
            SeedTag.loans,
            'Loans',
            TagKind.LIABILITIES,
            1,
        ),
    ]

def get_accounts() -> list[AccountRow]:
    return [
        AccountRow(
            SeedAccount.cash_usd,
            'Cash USD',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.cash,
        ),
        AccountRow(
            SeedAccount.cash_eur,
            'Cash_eur',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.cash,
        ),
        AccountRow(
            SeedAccount.cash_mxn,
            'Cash_mxn',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.cash,
        ),
        AccountRow(
            SeedAccount.payroll_usd,
            'Payroll_usd',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.debits,
        ),
        AccountRow(
            SeedAccount.bank1d,
            'Bank1d',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.debits,
        ),
        AccountRow(
            SeedAccount.bank2d,
            'Bank2d',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.debits,
        ),
        AccountRow(
            SeedAccount.bank1r,
            'Bank1r',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.reserved,
        ),
        AccountRow(
            SeedAccount.bank2r,
            'Bank2r',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.reserved,
        ),
        AccountRow(
            SeedAccount.bank1s,
            'Bank1s',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.savings,
        ),
        AccountRow(
            SeedAccount.bank2s,
            'Bank2s',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.savings,
        ),
        AccountRow(
            SeedAccount.us_treasb,
            'Us_treasb',
            SeedProfile.demo,
            SeedCurrency.us_tb,
            SeedTag.gov_bonds,
        ),
        AccountRow(
            SeedAccount.apple_stock,
            'Apple_stock',
            SeedProfile.demo,
            SeedCurrency.appstk,
            SeedTag.investments,
        ),
        AccountRow(
            SeedAccount.btc_wallet,
            'Btc_wallet',
            SeedProfile.demo,
            SeedCurrency.btc,
            SeedTag.cryptos,
        ),
        AccountRow(
            SeedAccount.retirement_fund,
            'Retirement_fund',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.funds,
        ),
        AccountRow(
            SeedAccount.amex_card,
            'Amex card',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.credits,
        ),
        AccountRow(
            SeedAccount.visacard,
            'Visacard',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.credits,
        ),
        AccountRow(
            SeedAccount.mastercard,
            'Mastercard',
            SeedProfile.demo,
            SeedCurrency.usd,
            SeedTag.credits,
        ),

    ]
