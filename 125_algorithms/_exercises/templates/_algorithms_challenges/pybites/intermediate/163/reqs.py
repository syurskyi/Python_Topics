# ____ p.. _______ v..
# # old_reqs = """
# # certifi==2017.4.17
# # chardet==3.0.4
# # click==6.7
# # Faker==0.7.12
# # Flask==0.12.1
# # """
# # new_reqs = """
# # certifi==2016.11.29
# # chardet==2.0.4
# # click==5.0
# # Faker==1.0.2
# # Flask==1.0.2
# # """
#
# # other_old_reqs = """
# # twilio==6.23.1
# # urllib3==1.21.1
# # Werkzeug==0.12.1
# # WTForms==1.19.0
# # """
# # other_new_reqs = """
# # twilio==6.3.0
# # urllib3==1.21.1
# # Werkzeug==0.14.1
# # WTForms==2.1
# # """
#
#
# ___ changed_dependencies old_reqs s.. new_reqs s.. __ l..
#    """Compare old vs new requirement multiline strings
#       and return a list of dependencies that have been upgraded
#       (have a newer version)
#    """
#    upgraded_reqs    # list
#    ___ old, new __ z.. o__.s...s..  n__.s...s..
#       req, version_old o__.s.. "=="
#       version_new n__.s.. "==" 1
#       __ v__.p..? > v__.p.. ?
#          u__.a.. r..
#    r.. ?
#
#
# # if __name__ == "__main__":
# #    ? ? ?