_____ u__
____ u__ _____ mock
____ d_t_ _____ d_t_

____ ..alert _____ Alert
____ ..rule _____ PriceRule
____ ..stock _____ Stock
____ ..event _____ Event


c_ AlertTest ?.?
    ___ test_action_is_executed_when_rule_matches
        goog = mock.MagicMock(spec=Stock)
        goog.updated = Event()
        goog.u...side_effect = l___ date, value: goog.updated.fire(self)
        ex__ = {"GOOG": goog}
        rule = mock.MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = mock.MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(ex__)
        ex__["GOOG"].u..(d_t_(2014, 2, 10), 11)
        action.execute.a_c_w..("sample alert")

    ___ test_action_doesnt_fire_if_rule_doesnt_match
        goog = Stock("GOOG")
        ex__ = {"GOOG": goog}
        rule = PriceRule("GOOG", l___ stock: stock.price > 10)
        rule_spy = mock.MagicMock(wraps=rule)
        action = mock.MagicMock()
        alert = Alert("sample alert", rule_spy, action)
        alert.connect(ex__)
        alert.check_rule(goog)
        rule_spy.matches.a_c_w..(ex__)
        aF..(action.execute.called)

    ___ test_action_fires_when_rule_matches
        goog = Stock("GOOG")
        ex__ = {"GOOG": goog}
        main_mock = mock.MagicMock()
        rule = main_mock.rule
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = main_mock.action
        alert = Alert("sample alert", rule, action)
        alert.connect(ex__)
        goog.u..(d_t_(2014, 5, 14), 11)
        aE..([mock.call.rule.depends_on(),
                          mock.call.rule.matches(ex__),
                          mock.call.action.execute("sample alert")],
                         main_mock.mock_calls)
