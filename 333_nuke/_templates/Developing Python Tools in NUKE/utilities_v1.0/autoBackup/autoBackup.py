import nuke
import os
import time
import helper


"""
This module contains functionality to make an automatic backup of your current nuke script whenever you save it.
"""


# autoBackup setting
#############################################################################
#
# backup_dir
# here you can set the root backup directory in which all backups are saved
backup_dir = "{}/nuke_backups".format(os.path.expanduser("~"))

# number_of_backups
# here you can decide how many latest backups to have per script
number_of_backups = 5
#
#############################################################################


def get_script_name():
    """
    get the name of the current nuke script
    :return: String name of the current nuke script
    """

    script = nuke.root().name()
    script_name = os.path.basename(script)
    script_name = os.path.splitext(script_name)[0]

    return script_name


def open_backup_dir():
    """
    open backup directory in explorer
    :return: None
    """

    script_name = get_script_name()
    script_backup_dir = "{}/{}".format(backup_dir, script_name)
    helper.open_folder(script_backup_dir)


def make_backup():
    """
    make backup of script
    :return: None
    """

    script_name = get_script_name()
    script_backup_dir = "{}/{}".format(backup_dir, script_name)
    current_time = time.strftime("%y%m%d-%H%M")

    if not os.path.isdir(script_backup_dir):
        os.makedirs(script_backup_dir)

    try:
        # remove callback, make backup, add callback
        # this is a special case because we do a save operation inside the save callback itself.
        # the callback needs to be removed and added afterwards, otherwise it would end up in an infinite loop
        nuke.removeOnScriptSave(make_backup)
        nuke.scriptSave("{}/bckp_{}_{}.nk".format(script_backup_dir, current_time, script_name))
        nuke.addOnScriptSave(make_backup)
    except:
        nuke.message("Couldn't write a backup file")

    delete_older_backup_versions(script_backup_dir)


def delete_older_backup_versions(path):
    """
    keep only the last backups of a script
    The number of backup scripts to keep is determined by 'number_of_backups'
    :param path: String full path of the script backup directory
    :return: None
    """

    files_list = []
    keep_list = []

    for filename in os.listdir(path):
        if os.path.splitext(filename)[1] == ".nk":
            files_list.append(filename)

    if len(files_list) > number_of_backups:
        keep_list = files_list[-number_of_backups:]

        # sorry, i forgot to indent this code here
        # it *must* be indented so it gets only executed
        # when our if statement above is True
        for filename in files_list:
            if filename not in keep_list:
                file_to_delete = "{}/{}".format(path, filename)
                if os.path.isfile(file_to_delete):
                    os.remove(file_to_delete)
