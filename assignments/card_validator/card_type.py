from enum import Enum


class CardType(Enum):
    VISA_CARD = 4
    MASTER_CARD = 5
    AMERICAN_EXPRESS = 37
    DISCOVERY_CARD = 6

    number: int

