# ========================================================================================================
# c_ HouseInfo
#     """Listing Information"""
#
#     ___ - area price hasWindow hasBathroom hasKitchen address owner
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#
#     ___ getAddress
#         r_ __a..
#
#     ___ getOwnerName
#         r_ __o__.gN..
#
#     ___ showInfo isShowOwner _ T..
#         print("Area: " + st. __a.. + "square meter"
#               "Price: " + st. __p.. + "yuan"
#               "Window: " + "Yes" __ __hW.. ____ "No"
#               "Bathroom: " + __hB..
#               "Kitchen:" + ("Yes" __ __hK.. ____ "No"
#               "Address:" + __a..
#               "Host:" + gON.. __ iSO... ____ ""
#
#
# c_ HousingAgency
#     """Housing agency"""
#
#     ___ - name
#         __houseInfos _   # list
#         __?  ?
#
#     ___ getName
#         r_ __n..
#
#     ___ addHouseInfo houseInfo
#         __h___.ap.. ?
#
#     ___ removeHouseInfo houseInfo
#         ___ info __ __h..
#             __ |? __ ?
#                 __h__.re.. ?
#
#     ___ getSearchCondition description
#         """Here's a logic that turns user descriptions into search criteria
#          (To save space, r_ to the description as it is)"""
#         r_ ?
#
#     ___ getMatchInfos searchCondition
#         """Find the best match based on the properties of the listing
#          (To save space, the matching process is omitted here, all output)"""
#         print(gN.. "Find the best fit ___ you:")
#         ___ info __ __h..
#             ?.sI.. F...
#         r_  __h..
#
#     ___ signContract houseInfo period
#         """Sign an agreement with the landlord"""
#         print(gN.. "With the host" hI___.gON.. "Sign" hI___.gA..
#               "Lease contract ___ house" p... "year. During the contract" gN.. "Right to use and sublet it!")
#
#     ___ signContracts period
#         ___ info __ __h..
#             sC.. i.. ?
#
#
# c_ HouseOwner
#     """landlord"""
#
#     ___ - name
#         __? ?
#         __houseInfo _ N..
#
#     ___ getName
#         r_ __?
#
#     ___ setHouseInfo self address area price hasWindow bathroom kitchen
#         __houseInfo _ HI.. area price hasWindow bathroom kitchen address ____
#
#     ___ publishHouseInfo agency
#         ?.aHI.. __h..
#         print(gN.. + "__" ?.gN.. "Post Property Rental Information:")
#         __h____.shI..
#
#
# c_ Customer
#     """Users, poor middle peasants renting houses"""
#
#     ___ - name
#         __?  ?
#
#     ___ getName
#         r_ __?
#
#     ___ findHouse description agency
#         print("I am" + gN.. + ", I want to find one\"" + ? + "\"House of")
#         print()
#         r_ ?.gMI.. a____.gSC... d...
#
#     ___ seeHouse houseInfos
#         """Go to the house and choose the most used house
#          (The process of viewing a house is omitted here)"""
#         size _ le. hI..
#         r_ hI...|s..-1
#
#     ___ signContract houseInfo agency period
#         """Sign an agreement with an intermediary"""
#         print(gN.. "Intermediary" a____.gN.. "Sign" hI___.gA..
#               "Lease contract ___ a house" p___ "year. During the contract" __n.. "Right to use it!")
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# c_ InteractiveObject
#     """Objects to interact with"""
#     p..
#
# c_ InteractiveObjectImplA
#     """Implementation c_ A"""
#     p..
#
# c_ InteractiveObjectImplB:
#     """Implementation c_ B"""
#     p..
#
# c_ Meditor
#     """Intermediary"""
#
#     ___ -
#         __interactiveObjA _ InteractiveObjectImplA
#         __interactiveObjB _ InteractiveObjectImplB
#
#     ___ interative
#         """Interactive operation"""
#         # Complete the corresponding interactive operations through self .__ interactiveObjA and self .__ interactiveObjB
#         p..
#
#
# # Framework-based implementation
# #==============================
# ____ a.. ______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
# ____ e.. ______ E..
# # Enum enum syntax is supported after Python 3.4
#
# c_ DeviceType E..
#     "Equipment type"
#     TypeSpeaker _ 1
#     TypeMicrophone _ 2
#     TypeCamera _ 3
#
# c_ DeviceItem
#     """Equipment item"""
#
#     ___ -  id name type isDefault _ F...
#         __?  ?
#         __?  ?
#         __?  ?
#         __?  ?
#
#     ___ -s
#         r_ "type:" + st. __t.. + " id:" + st. __i. \
#                + " name:" + st. __n.. + " isDefault:" + st. __iD..
#
#     ___ getId
#         r_ __?
#
#     ___ getName
#         r_ __?
#
#     ___ getType
#         r_ __?
#
#     ___ isDefault
#         r_ __?
#
#
# c_ DeviceList:
#     """Device List"""
#
#     ___ -
#         __devices _    # list
#
#     ___ add deviceItem
#         __d___.ap.. ?
#
#     ___ getCount
#         r_ le. __d___
#
#     ___ getByIdx  idx
#         __ ? < 0 o. ? >_ gC..
#             r_ N..
#         r_ __d___|?
#
#     ___ getById id
#         ___ item __ __d___
#             __|?.gI.. __ ?
#                 r_ ?
#         r_ N..
#
# c_ DeviceMgr m..
#
#     ??
#     ___ enumerate
#         """Enumerating the device list
#          (When the program is initialized the device list must be re-obtained when there is a device plug-__)"""
#         p..
#
#     ??
#     ___ active deviceId
#         """Select the device you want to use"""
#         p..
#
#     ??
#     ___ getCurDeviceId
#         """Get the design ID currently __ use"""
#         p..
#
#
# c_ SpeakerMgr D..
#     """Speaker device management c_"""
#
#     ___ -
#         __curDeviceId _ N..
#
#     ___ enumerate
#         """Enumerating the device list
#          (The real project should read the device information through the driver, here only the initialization is used to simulate)"""
#         devices _ D..
#         ?.ad. DI.. "369dd760-893b-4fe0-89b1-671eca0f0224" "Realtek High Definition Audio" DT___.TS___
#         ?.ad. DI.. "59357639-6a43-4b79-8184-f79aed9a0dfc" "NVIDIA High Definition Audio" DT___.TS___ T..
#         r_ ?
#
#     ___ active deviceId
#         """Activate the specified device as the current device"""
#         __curDeviceId _ ?
#
#     ___ getCurDeviceId
#         r_ __?
#
#
# c_ DeviceUtil
#     """Equipment tools"""
#
#     ___ -
#         __mgrs _    # dict
#         __?|DT___.TS___ _ SM..
#         # To save space, MicrophoneMgr and CameraMgr are no longer implemented
#         # __microphoneMgr _ MicrophoneMgr()
#         # __cameraMgr _ CameraMgr
#
#     ___ __getDeviceMgr type
#         r_ __m...|?
#
#     ___ getDeviceList type
#         r_ __gM..|? .en..
#
#     ___ active type deviceId
#         __gDM.. ty.. .a.. dI.
#
#     ___ getCurDeviceId type
#         r_ __gDM.. ?. gCDI.
#
#
# # Test
# #=======================================================================================================================
#
# ___ Renting
#     myHome _ HA.. "I love my home"
#     zhangsan _ HO.. "Zhang San"
#     ?.sHI.. "Upper Sicily", 20, 2500, 1, "individual washroom", 0
#     ?.pHI.. m..
#     lisi _ HO.. "Li Si"
#     ?.sHI.. "Contemporary Urban Home", 16, 1800, 1, "Public toilet", 0
#     ?.pHI.. m..
#     wangwu _ HO.. "Wang Wu"
#     ?.sHI..("Golden Beauty Garden", 18, 2600, 1, "individual washroom", 1
#     ?.pHI.. m..
#     print()
#
#     m__.sC.. 3
#     print()
#
#     tony _ C.. "Tony"
#     houseInfos _ ?.fH.. "About 18 square meters, you need to have independent guards and windows. It is best to face south. A kitchen is better! Price around 2000", myHome)
#     print()
#     print("Looking around, looking ___ the most suitable nest ...")
#     print()
#     AppropriateHouse _ t___.sH.. hI..
#     t__.sC... AH.. my.. 1
#
#
# ___ Devices
#     deviceUtil _ D..
#     deviceList _ ?.gDL.. DT___.TS___
#     print("Microphone device list：")
#     __ dL__.gC.. > 0:
#         # Set the first device to be used
#         dU__.a.. DT___.TS___, dL__.gBI.. 0 .gI..
#     ___ idx __ ra.. 0 dL__.gC..
#         device _ dL__.gBI.. ?
#         print ?
#     print("Equipment currently __ use:"
#           + dL__.gBI. dU__.gCDI. DT___.TS___||.gN..
#
#
# # testRenting()
# Devices()
