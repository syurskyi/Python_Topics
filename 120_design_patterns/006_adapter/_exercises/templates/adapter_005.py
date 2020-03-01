# """
# The Adapter pattern is a structural design pattern. It allows a Client to access
# functionalities of a Supplier.
# Without an Adapter the Client can not access such functionalities.
# This pattern can be implemented with an OBJECT approach or a CLASS approach.
# """
#
#
# # Client
#
#
# c_ Smartphone o..
#
#     max_input_voltage _ 5
#
#     ??
#     ___ outcome ___ input_voltage
#         __ input_voltage > ___.max_input_voltage:
#             print("Input voltage: @V -- BURNING!!!".f.. ?
#         ____:
#             print("Input voltage: @V -- Charging...".f.. ?
#
#     ___ charge input_voltage
#         """Charge the phone with the given input voltage."""
#         o... ?
#
#
# # Supplier
#
#
# c_ Socket o..
#     output_voltage _ N..
#
#
# c_ EUSocket Socket
#     output_voltage _ 230
#
#
# c_ USSocket S..
#     output_voltage _ 120
#
#
# ################################################################################
# # Approach A: OBJECT Adapter. The adapter encapsulates client and supplier.
# ################################################################################
#
#
# c_ EUAdapter o..
#     """EUAdapter encapsulates client (Smartphone) and supplier (EUSocket)."""
#     input_voltage _ E...o_v..
#     output_voltage _ Sm___.ma..
#
#
# c_ USAdapter o..
#     """USAdapter encapsulates client (Sm___) and supplier (USSocket)."""
#     input_voltage _ US__.o_v..
#     output_voltage _ Sm___.ma..
#
#
# ################################################################################
# # Approach B: CLASS Adapter. Adapt the Client through multiple inheritance.
# ################################################################################
#
#
# c_ CannotTransformVoltage E..
#     """Exception raised by the SmartphoneAdapter.
#
#     This exception represents the fact that an adapter could not provide the
#     right voltage to the Smartphone __ the voltage of the Socket is wrong."""
#     p..
#
#
# c_ SmartphoneAdapter Sm___ So..
#
#     ??
#     ___ transform_voltage ___ i_v..
#         __ i_v_ __ ___.o_v..:
#             r_ ___.ma..
#
#         ____:
#             r__ CTV..(
#                 "Can\'t transform {0}-{1}V. This adapter transforms {2}-{1}V.".f..(
#                     i_v_ ___.ma.. ___.o_v..
#                 )
#             )
#
#     ??
#     ___ charge ___ i_v_
#         ___
#             voltage _ ___.t_v_ i_v_
#             ___.ou.. ?
#         ______ CTV.. __
#             print ?
#
#
# c_ SmartphoneEUAdapter SA... E..
#     """System (smartphone + adapter) for a European Socket.
#
#     Note: SmartphoneAdapter already inherited from Smartphone and Socket but by
#     re-inheriting from EUSocket we redefine all the stuff inherited from Socket.
#     """
#     p..
#
#
# c_ SmartphoneUSAdapter SA.. US..
#     """System (smartphone + adapter) for an American Socket."""
#     p..
#
#
# ___ main
#
#     print("Smartphone without adapter")
#     smartphone _ Sm___
#     ?.ch.. E...o_v..
#     ?.ch.. US__.o_v..
#
#     print("\nSmartphone with EU adapter (o.. adapter approach)")
#     ?.ch.. EUAd__.o_v..
#     print("\nSmartphone with US adapter (o.. adapter approach)")
#     ?.ch.. US__.o_v..
#
#     print("\nSmartphone with EU adapter (c_ adapter approach)")
#     smarthone_with_eu_adapter _ S_EUAd...
#     ?.ch.. E...o_v..
#     ?.ch.. US__.o_v..
#     print("\nSmartphone with US adapter (c_ adapter approach)")
#     ? _ S_USA..
#     ?.ch.. E...o_v..
#     ?.ch..(US___.o_v..
#
#
# __ ______ __ _______
#     ?
