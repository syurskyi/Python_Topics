_____ _3, ___
____ ?.?W.. _____ ?D.., ?A..
____ _3 _____ E..

____ demoDeleteUser _____ *

c_ MyForm(?D..

    ___  -  
        s__. -
        ui _ ?
        ?.sU..
        ?.pushButtonDelete.c___.c..(DeleteUser)
        ?.pushButtonYes.c___.c..(ConfirmDelete)
        ?.labelSure.hide
        ?.pushButtonYes.hide
        ?.pushButtonNo.hide
        s..

    ___ DeleteUser 
        selectStatement_"SELECT * FROM Users where EmailAddress like '"+?.lineEditEmailAddress.t..+"' and Password like '"+ ?.lineEditPassword.t..+"'"
        ___
            conn _ _3.c..("ECommerce.db")
            cur _ conn.c..
            cur.e..(selectStatement)
            row _ cur.f..
            __ row__None:
                ?.labelSure.hide
                ?.pushButtonYes.hide
                ?.pushButtonNo.hide
                ?.lR___.sT..("Sorry, Incorrect email address or password ")
            ____
                ?.labelSure.s..
                ?.pushButtonYes.s..
                ?.pushButtonNo.s..
                ?.lR___.sT..("")
        _____ E.. __ e:
            ?.lR___.sT..("Error in accessing user account")
        f..
            conn.c..

    ___ ConfirmDelete 
        deleteStatement_"DELETE FROM Users where EmailAddress like '"+?.lineEditEmailAddress.t..+"' and Password like '"+ ?.lineEditPassword.t..+"'"
        ___
            conn _ _3.c..("ECommerce.db")
            cur _ conn.c..
            w__ conn:
                cur.e..(deleteStatement)
                ?.lR___.sT..("User successfully deleted")
        _____ E.. __ e:
            ?.lR___.sT..("Error in deleting user account")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
