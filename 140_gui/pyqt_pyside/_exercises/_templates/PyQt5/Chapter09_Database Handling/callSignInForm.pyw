_____ _3, ___
____ ?.?W.. _____ ?D.., ?A..
____ _3 _____ E..

____ demoSignInForm _____ *

c_ MyForm(?D..

    ___  -
        s__. -
        ui _ ?
        ?.sU..
        ?.pushButtonSearch.c___.c..(SearchRows)
        s..

    ___ SearchRows
        sqlStatement_"SELECT EmailAddress, Password FROM Users where EmailAddress like '"+?.lineEditEmailAddress.t..+"' and Password like '"+ ?.lineEditPassword.t..+"'"
        ___
            conn _ _3.c..("ECommerce.db")
            cur _ conn.c..
            cur.e..(sqlStatement)
            row _ cur.f..
            __ row__None:
                ?.lR___.sT..("Sorry, Incorrect email address or password ")
            ____
                ?.lR___.sT..("You are welcome ")
        _____ E.. __ e:
            ?.lR___.sT..("Error in accessing row")
        f..
            conn.c..

__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e.. ?.e
