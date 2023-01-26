from assignments.card_validator.card_type import CardType


class CreditCardValidator:
    def __init__(self, card_number: str):
        self.__type: CardType = None
        self.__card_is_Valid: bool = False
        self.__card_number: str = card_number
        self.__total_sum_of_doubled_card_number_second_digit: int = 0
        self.__total_sum_of_digits_in_odd_places: int = 0

    def double_second_digit_of_the_card(self):
        for digit in range(len(self.__card_number) - 2, -1, -2):
            each: int = int(self.__card_number.__getitem__(digit)) * 2
            self.__total_sum_of_doubled_card_number_second_digit += each % 9

    def add_digits_in_odd_places(self):
        for oddDigit in range(len(self.__card_number) - 1, -1, -2):
            self.__total_sum_of_digits_in_odd_places += int(self.__card_number.__getitem__(oddDigit))

    def get_sum_of_doubled_digits(self) -> int:
        return self.__total_sum_of_doubled_card_number_second_digit

    def get_sum_of_odd_digits(self) -> int:
        return self.__total_sum_of_digits_in_odd_places

    def validate_card_number(self):
        if len(self.__card_number) < 13 or len(self.__card_number) > 16:
            raise ValueError("Card number length must be between 13 and 16")

    def set_card_validity(self):
        if (self.get_sum_of_odd_digits() + self.get_sum_of_doubled_digits()) % 10 == 0:
            self.__card_is_Valid = True
        return self.__card_is_Valid

    def set_card_type(self):
        first_digit: int = int(self.__card_number.__getitem__(0))
        if first_digit == 4:
            self.__type = CardType.VISA_CARD
        elif first_digit == 5:
            self.__type = CardType.MASTER_CARD
        elif first_digit == 6:
            self.__type = CardType.DISCOVERY_CARD
        elif first_digit == 3 and int(self.__card_number.__getitem__(1)) == 7:
            self.__type = CardType.AMERICAN_EXPRESS

    def get_card_type(self) -> str:
        return self.__type.name

    def __str__(self) -> str:
        status: str = ""
        if self.__card_is_Valid:
            status = "Valid"
        else:
            status = "Invalid"
        return f"""
        **************************************
        **Credit Card Type: {self.__type.name}
        **Credit Card Number: {self.__card_number}
        **Credit Card Digit Length: {len(self.__card_number)}
        **Credit Card Validity Status: {status}
        **************************************
        """
