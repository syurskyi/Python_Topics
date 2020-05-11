_____ u__
from datetime _____ datetime

from ..stock _____ Stock
from ..rule _____ PriceRule, AndRule


c_ PriceRuleTest ?.?
    @classmethod
    ___ setUpClass(cls):
        goog = Stock("GOOG")
        goog.update(datetime(2014, 2, 10), 11)
        cls.exchange = {"GOOG": goog}

    ___ test_a_PriceRule_matches_when_it_meets_the_condition
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        assertTrue(rule.matches(exchange))

    ___ test_a_PriceRule_is_False_if_the_condition_is_not_met
        rule = PriceRule("GOOG", lambda stock: stock.price < 10)
        assertFalse(rule.matches(exchange))

    ___ test_a_PriceRule_is_False_if_the_stock_is_not_in_the_exchange
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        assertFalse(rule.matches(exchange))

    ___ test_a_PriceRule_is_False_if_the_stock_hasnt_got_an_update_yet
        exchange["AAPL"] = Stock("AAPL")
        rule = PriceRule("AAPL", lambda stock: stock.price > 10)
        assertFalse(rule.matches(exchange))

    ___ test_a_PriceRule_only_depends_on_its_stock
        rule = PriceRule("MSFT", lambda stock: stock.price > 10)
        assertEqual({"MSFT"}, rule.depends_on())


c_ AndRuleTest ?.?
    @classmethod
    ___ setUpClass(cls):
        goog = Stock("GOOG")
        goog.update(datetime(2014, 2, 10), 8)
        goog.update(datetime(2014, 2, 11), 10)
        goog.update(datetime(2014, 2, 12), 12)
        msft = Stock("MSFT")
        msft.update(datetime(2014, 2, 10), 10)
        msft.update(datetime(2014, 2, 11), 10)
        msft.update(datetime(2014, 2, 12), 12)
        redhat = Stock("RHT")
        redhat.update(datetime(2014, 2, 10), 7)
        cls.exchange = {"GOOG": goog, "MSFT": msft, "RHT": redhat}

    ___ test_an_AndRule_matches_if_all_component_rules_are_true
        rule = AndRule(PriceRule("GOOG", lambda stock: stock.price > 8),
                       PriceRule("MSFT", lambda stock: stock.price > 10))
        assertTrue(rule.matches(exchange))
