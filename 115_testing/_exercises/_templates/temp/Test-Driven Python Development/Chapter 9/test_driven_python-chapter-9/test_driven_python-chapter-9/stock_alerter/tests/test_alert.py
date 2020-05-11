_____ u__
from u__ _____ mock
from datetime _____ datetime

from ..alert _____ Alert
from ..rule _____ PriceRule
from ..stock _____ Stock
from ..event _____ Event


c_ AlertTest ?.?
    ___ test_action_is_executed_when_rule_matches
        goog = mock.MagicMock(spec=Stock)
        goog.updated = Event()
        goog.update.side_effect = lambda date, value: goog.updated.fire(self)
        exchange = {"GOOG": goog}
        rule = mock.MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = mock.MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        exchange["GOOG"].update(datetime(2014, 2, 10), 11)
        action.execute.assert_called_with("sample alert")

    ___ test_action_doesnt_fire_if_rule_doesnt_match
        goog = Stock("GOOG")
        exchange = {"GOOG": goog}
        rule = PriceRule("GOOG", lambda stock: stock.price > 10)
        rule_spy = mock.MagicMock(wraps=rule)
        action = mock.MagicMock()
        alert = Alert("sample alert", rule_spy, action)
        alert.connect(exchange)
        alert.check_rule(goog)
        rule_spy.matches.assert_called_with(exchange)
        assertFalse(action.execute.called)

    ___ test_action_fires_when_rule_matches
        goog = Stock("GOOG")
        exchange = {"GOOG": goog}
        main_mock = mock.MagicMock()
        rule = main_mock.rule
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = main_mock.action
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        goog.update(datetime(2014, 5, 14), 11)
        assertEqual([mock.call.rule.depends_on(),
                          mock.call.rule.matches(exchange),
                          mock.call.action.execute("sample alert")],
                         main_mock.mock_calls)
