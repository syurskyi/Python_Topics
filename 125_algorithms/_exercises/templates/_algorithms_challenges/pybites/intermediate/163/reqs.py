____ packaging _______ version
# old_reqs = """
# certifi==2017.4.17
# chardet==3.0.4
# click==6.7
# Faker==0.7.12
# Flask==0.12.1
# """
# new_reqs = """
# certifi==2016.11.29
# chardet==2.0.4
# click==5.0
# Faker==1.0.2
# Flask==1.0.2
# """

# other_old_reqs = """
# twilio==6.23.1
# urllib3==1.21.1
# Werkzeug==0.12.1
# WTForms==1.19.0
# """
# other_new_reqs = """
# twilio==6.3.0
# urllib3==1.21.1
# Werkzeug==0.14.1
# WTForms==2.1
# """


___ changed_dependencies(old_reqs: s.., new_reqs: s..) __ l..:
   """Compare old vs new requirement multiline strings
      and return a list of dependencies that have been upgraded
      (have a newer version)
   """
   upgraded_reqs    # list
   ___ old, new __ z..(old_reqs.s...s.. , new_reqs.s...s..:
      req, version_old old.s..("==")
      version_new new.s..("==")[1]
      __ version.p..(version_new) > version.p..(version_old
         upgraded_reqs.a..(req)
   r.. upgraded_reqs


# if __name__ == "__main__":
#    changed_dependencies(other_old_reqs, other_new_reqs)