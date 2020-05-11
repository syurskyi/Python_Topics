# _____ u__
# ____ d_t_ _____ d_t_
#
# ____ __s.. _____ S..
# ____ __r.. _____ PR.. AR..
#
#
# c_ PriceRuleTest ?.?
#     ??
#     ___ setUpClass ___
#         goog _ ?"GOOG"
#         ?.u.. d_t_(2014, 2, 10), 11
#         ___.ex__ _ "GOOG": ?
#
#     ___ test_a_PriceRule_matches_when_it_meets_the_condition
#         rule _ PR... "GOOG" l___ stock ?.p.. > 10
#         aT.. ?.m.. ex__
#
#     ___ test_a_PriceRule_is_False_if_the_condition_is_not_met
#         rule _ PR.. "GOOG" l___ stock ?.p.. < 10
#         aF.. ?.m.. ex__
#
#     ___ test_a_PriceRule_is_False_if_the_stock_is_not_in_the_exchange
#         rule _ ? "MSFT" l___ stock ?.p.. > 10
#         aF.. ?.m.. ex_
#
#     ___ test_a_PriceRule_is_False_if_the_stock_hasnt_got_an_update_yet
#         ex__["AAPL"] _ S.. "AAPL"
#         rule _ PR.. "AAPL" l___ stock ?.p.. > 10
#         aF.. ?.m.. ex__
#
#     ___ test_a_PriceRule_only_depends_on_its_stock
#         rule _ PR.. "MSFT" l___ stock ?.p.. > 10
#         aE.. "MSFT" ?.d_o.
#
#
# c_ AndRuleTest ?.?
#     ??
#     ___ setUpClass ___
#         goog _ S.. "GOOG"
#         ?.u.. d_t_ 2014, 2, 10), 8
#         ?.u.. d_t_ 2014, 2, 11), 10
#         ?.u.. d_t_ 2014, 2, 12), 12
#         msft _ S.. "MSFT"
#         ?.u.. d_t_ 2014, 2, 10), 10
#         ?.u.. d_t_ 2014, 2, 11), 10
#         ?.u.. d_t_ 2014, 2, 12), 12
#         redhat _ S.. "RHT"
#         ?.u.. d_t_ 2014, 2, 10), 7
#         cls.ex__ _ {"GOOG" ? "MSFT" ? "RHT" ?
#
#     ___ test_an_AndRule_matches_if_all_component_rules_are_true
#         rule _ AR.. PR.. "GOOG" l___ stock ?.p.. > 8
#                        PR.. "MSFT" l___ stock ?.p.. > 10
#         aT.. ?.m.. ex__
