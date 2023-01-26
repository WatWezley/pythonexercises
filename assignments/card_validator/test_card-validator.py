from unittest import TestCase

from assignments.card_validator.CreditCardValidator import CreditCardValidator


class CardValidatorTest(TestCase):

    def test_second_digit_of_the_card_from_right_to_left_can_be_doubled(self):
        credit_card_number: str = "4388576018402626"
        credit_card: CreditCardValidator = CreditCardValidator(credit_card_number)
        credit_card.double_second_digit_of_the_card()

        self.assertEqual(37, credit_card.get_sum_of_doubled_digits())

    def test_digits_in_the_odd_places_can_be_added(self):
        credit_card_number: str = "4388576018402626"
        credit_card: CreditCardValidator = CreditCardValidator(credit_card_number)
        credit_card.add_digits_in_odd_places()

        self.assertEqual(38, credit_card.get_sum_of_odd_digits())

    def test_card_number_length_lesser_than_13_and_greater_than_16_throws_exception(self):
        credit_card_number: str = "438802626"
        credit_card: CreditCardValidator = CreditCardValidator(credit_card_number)

        with self.assertRaises(ValueError):
            credit_card.validate_card_number()

    def test_card_validity(self):
        credit_card_number: str = "438876756560707"
        credit_card: CreditCardValidator = CreditCardValidator(credit_card_number)
        credit_card.add_digits_in_odd_places()
        credit_card.double_second_digit_of_the_card()

        self.assertTrue(credit_card.set_card_validity)

    def test_card_type_is_determined_by_first_digit_of_the_card_number(self):
        credit_card_number: str = "438876756560707"
        credit_card: CreditCardValidator = CreditCardValidator(credit_card_number)
        credit_card.validate_card_number()
        credit_card.set_card_type()

        self.assertEqual("VISA_CARD", credit_card.get_card_type())

    def test_display_string_representation_of_the_a_card_validity(self):
        credit_card_number: str = "438876756560707"
        credit_card: CreditCardValidator = CreditCardValidator(credit_card_number)
        credit_card.validate_card_number()
        credit_card.double_second_digit_of_the_card()
        credit_card.add_digits_in_odd_places()
        credit_card.set_card_type()
        credit_card.set_card_validity()
        expected: str = """
        **************************************
        **Credit Card Type: VISA_CARD
        **Credit Card Number: 438876756560707
        **Credit Card Digit Length: 15
        **Credit Card Validity Status: Valid
        **************************************
        """

        self.assertEqual(expected, credit_card.__str__())

