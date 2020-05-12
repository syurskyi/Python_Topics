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
