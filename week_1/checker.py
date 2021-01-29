import bus_fare_challenge as solution
import datetime
import unittest


class TestBusFareChallenge(unittest.TestCase):
    def setUp(self):
        self.date = datetime.datetime.now().date()
        self.day = self.date.strftime("%a")
        self.charts = {
            "Mon": 100,
            "Tue": 100,
            "Wed": 100,
            "Thu": 100,
            "Fri": 100,
            "Sat": 60,
            "Sun": 80,
        }

    def test_date(self):
        """
        Tests whether the date returned by the program is correct.
        """
        actual = self.date
        given = solution.date
        self.assertEqual(actual, given, "Todays date is given wrong by {}-{}".format(given, actual))

    def test_day(self):
        """
        Tests whether the day returned by the program is correct.
        """
        actual = self.day
        given = solution.day
        self.assertEqual(
            actual, given, "Today is wrong, expexted {} but got {}".format(actual, given)
        )

    def test_fare(self):
        """
        Tests whether the fare returned by the program is correct.
        """
        actual = self.charts[self.day]
        given = solution.fare
        self.assertEqual(
            actual, given, "Fare is wrong, expected {} but got {}!".format(actual, given)
        )


if __name__ == "__main__":
    print("=========================================================================")
    print("=========================================================================")
    print("===== Start: Checking Return Values For Today's  Date, Day and Fare =====")
    unittest.main(exit=False)
    print("===== End: Checking Return Values For Today's  Date, Day and Fare =======")
    print("=========================================================================")
