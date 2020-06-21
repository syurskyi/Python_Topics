_____ u__
____ d_t_ _____ d_t_

____ ..stock _____ Stock
____ ..rule _____ PriceRule, AndRule


c_ PriceRuleTest ?.?
    ??
    ___ setUpClass ___
        goog = Stock("GOOG")
        goog.u..(d_t_(2014, 2, 10), 11)
        cls.ex__ = {"GOOG": goog}

    ___ test_a_PriceRule_matches_when_it_meets_the_condition
        rule = PriceRule("GOOG", l___ stock: stock.price > 10)
        aT..(rule.m..(ex__))

    ___ test_a_PriceRule_is_False_if_the_condition_is_not_met
        rule = PriceRule("GOOG", l___ stock: stock.price < 10)
        aF..(rule.m..(ex__))

    ___ test_a_PriceRule_is_False_if_the_stock_is_not_in_the_exchange
        rule = PriceRule("MSFT", l___ stock: stock.price > 10)
        aF..(rule.m..(ex__))

    ___ test_a_PriceRule_is_False_if_the_stock_hasnt_got_an_update_yet
        ex__["AAPL"] = Stock("AAPL")
        rule = PriceRule("AAPL", l___ stock: stock.price > 10)
        aF..(rule.m..(ex__))

    ___ test_a_PriceRule_only_depends_on_its_stock
        rule = PriceRule("MSFT", l___ stock: stock.price > 10)
        aE..({"MSFT"}, rule.depends_on())


c_ AndRuleTest ?.?
    ??
    ___ setUpClass ___
        goog = Stock("GOOG")
        goog.u..(d_t_(2014, 2, 10), 8)
        goog.u..(d_t_(2014, 2, 11), 10)
        goog.u..(d_t_(2014, 2, 12), 12)
        msft = Stock("MSFT")
        msft.u..(d_t_(2014, 2, 10), 10)
        msft.u..(d_t_(2014, 2, 11), 10)
        msft.u..(d_t_(2014, 2, 12), 12)
        redhat = Stock("RHT")
        redhat.u..(d_t_(2014, 2, 10), 7)
        cls.ex__ = {"GOOG": goog, "MSFT": msft, "RHT": redhat}

    ___ test_an_AndRule_matches_if_all_component_rules_are_true
        rule = AndRule(PriceRule("GOOG", l___ stock: stock.price > 8),
                       PriceRule("MSFT", l___ stock: stock.price > 10))
        aT..(rule.matches(ex__))
