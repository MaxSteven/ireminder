#! /usr/bin/env python
# This free software incorporates by reference the text of the WTFPL, Version 2

"""
This is a simple reminder system. Once it is ran, a window will show up
that user can specify a time and message to reminder

.. module:: `reminder`
   :platform: Unix, Windows
   :synopsis: reminder system.

.. module_author:: Ali Jafargholi <ali.jafargholi@gmail.com>
"""

# IMPORT STANDARD MODULES
import sys
import time

# IMPORT LOCAL MODULES
from ui import main_UI, message_UI
from PyQt4 import QtCore, QtGui


class ReminderSystem(QtGui.QWidget, main_UI.Ui_mian_window, message_UI.Ui_Form):
    """
    Setting up the main UI
    """
    def __init__(self, parent=None):
        """
        """
        super(ReminderSystem, self).__init__(parent)
        self.setupUi(self)
        # Set the time display on the window to the current time
        self.due_time.setTime(QtCore.QTime.currentTime())
        # making an instance of message window
        self.message_window = MessageWindow()
        # Setting up the Signals
        self._setup_signals()
    # --> End __init__

    def _setup_signals(self):
        """
        Connecting the signals of the UI to the their use
        """

        self.ok_button.clicked.connect(self._ok_button_clicked)
        self.cancel_button.clicked.connect(self._cancel_button_clicked)
    # --> End _setup_signals

    def _cancel_button_clicked(self):
        """
        Closing the main window after cancel button was clicked
        """
        # Close the app
        self.close()
    # --> End _cancel_button_clicked

    def _ok_button_clicked(self):
        """
        Set up the reminder system once the OK button was clicked
        """

        # Collecting the info from the window
        close_reminder = self.close_after.checkState()
        reminder_message = self.messgae_value.text()
        reminder_due_time = self.due_time.text()

        # Converting the time to QTime type
        hours = int(reminder_due_time.split(":")[0])
        minutes = int(reminder_due_time.split(":")[1].split(" ")[0])
        am_pm = reminder_due_time.split(":")[1].split(" ")[1]
        # Converting the time to 24 the
        if am_pm == "PM":
            hours += 12
        reminder_due_time = QtCore.QTime(hours, minutes)

        # Closing the main window
        self.close()

        # Sending the data to the reminder window
        self._reminder(reminder_message, close_reminder, reminder_due_time)
    # --> _ok_button_clicked

    def _reminder(self, msg, close_it, due):
        """
        Based on the input value, it'll remind the user via
        splash screen, and then it'll shows the a message

        :arg msg: (optional) Message to be shown when alarm goes off
        :type msg: str
        :arg close_it: Boolean value that causes whether the message \
        window to be closed after 10 sec
        :type close_it; boolean
        :arg due: Time to remind the user, example --> 10:30, or, 17:43
        :type due: str
        :returns: returns the message in a QWidget
        :rtype: QWidget
        """

        # If user didn't specify a message, assign something to message,
        # otherwise use the message that user asked
        if not msg:
            msg = "It is time"

        # While we haven't reached the due time, put the script to sleep
        # for 20 seconds
        while due > QtCore.QTime.currentTime():
            time.sleep(20)

        self.message_window.message_result.setText("<font color='red'\
         size=3> " + msg + " </font>")
        self.message_window.show()

        # If the close itself is on, close the window after 10 sec
        if close_it:
            QtCore.QTimer.singleShot(10000, self.message_window.close)
# -->  End ReminderSystem


class MessageWindow(QtGui.QWidget, message_UI.Ui_Form):
    """
    The Message window
    """

    def __init__(self, parent=None):
        """
        Constructing the message window
        """

        super(MessageWindow, self).__init__(parent)
        self.setupUi(self)
        # setting up the signals
        self._setup_signals()
    # --> End __init__

    def _setup_signals(self):
        """
        Setting up the signals of the message window buttons
        """

        self.close_result_window.clicked.connect(self._close_message_window)
    # --> End _setup_signals

    def _close_message_window(self):
        """
        Closing the message window
        """

        self.close()
    # --> End _close_message_window
#---> End MessageWindow


def main():
    """
    Main function the setup the application and run the main window.
    """

    app = QtGui.QApplication(sys.argv)
    win = ReminderSystem()
    win.show()
    app.exec_()
# --> End main

if __name__ == '__main__':
    main()

