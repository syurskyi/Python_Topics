Overview
========
The documentation for threading in PyQt seems to have some rusty corners and
the proper method for creating and finishing threads has been obscured by the
scores of examples based on older documentation.  This is an attempt to make
some sort of example code that I would have found very helpful a few days ago.

Purpose
-------
The purpose of these modules is to serve as a proof-of-concept for a common use
case: farming a time-intensive task in a GUI application out to another thread
and updating a progress box or window with the status.  This sort of thing
should be pretty common but surprisingly, I was unable to find many examples
that did it using the method recommended by the more recent documentation.

This is a very simple example of a PyQt ``MainWindow`` application containing a
single push button that opens a ``ProgressDialog`` window that performs some
time-intensive operation in a separate thread and returns control to the main
thread once the operation ends or is canceled.  If your code is still
subclassing ``QThread`` and overloading the ``run()`` method, I hope this
helps.

Requirements
------------
This was hacked together this evening using PyQt 4.11.4 and Python 2.7.10 on
Linux, but it should work just fine on Windows or Mac OS as well.

Future
------
I will probably take some time to make this more appealing, but for now, it
works and demonstrates how to farm time-intensive work out to another thread
and end or cancel it, without generating a ton of ``QThread destroyed while
thread is still running`` errors.

