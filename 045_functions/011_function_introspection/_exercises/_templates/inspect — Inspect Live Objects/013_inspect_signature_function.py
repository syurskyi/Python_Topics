# ______ i....
# ______ example
#
# sig _ i___.s.. e___.module_level_function
# print 'module_level_function||'.f.. sig
#
# print('\nParameter details:')
# ___ name param i_ s__.p____.i__
#     i_ p___.kind __ i___.Parameter.POSITIONAL_ONLY
#         print('  || (positional-only)'.f... n...
#     e____ p___.kind __ i___.Parameter.POSITIONAL_OR_KEYWORD
#         i_ p___.default !_ i___.Parameter.empty:
#             print('  {}_{!r}'.f... n... param.default
#         e____
#             print('  {}'.f... n...
#     e___ p___.kind __ i___.Parameter.VAR_POSITIONAL
#         print('  *||'.f... n...
#     e___ p___.kind __ i___.Parameter.KEYWORD_ONLY:
#         i_ p___.default !_ i___.Parameter.empty:
#             print('  ||_|!r| (keyword-only)'.f...(
#                 n..., param.default
#         e___
#             print('  || (keyword-only)'.f... n...
#     e___ p___.kind __ i___.Parameter.VAR_KEYWORD:
#         print('  **||'.f... n...