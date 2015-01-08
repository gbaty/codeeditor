# -*- coding: utf-8 -*-
# -*- python -*-
#
#
#
#       Copyright 2014 INRIA
#
#       File author(s): Guillaume Baty <guillaume.baty@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the MIT License.
#       See accompanying file LICENSE.txt
#
###############################################################################

from openalea.vpltk.qt import QtGui, QtCore
from openalea.vpltk.qt.QtCore import Signal

from spyderlib.plugins.editor import Editor
from spyderlib.spyder import MainWindow


class SpyderWin(QtGui.QMainWindow):
    restore_scrollbar_position = Signal()
    all_actions_defined = Signal()
    sig_pythonpath_changed = Signal()
    sig_open_external_file = Signal(str)

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        for menu_name in ('file', 'edit', 'search', 'run', 'debug', 'source'):
            setattr(self, '%s_menu_actions' % menu_name, [])
            setattr(self, '%s_toolbar_actions' % menu_name, [])

    def register_shortcut(self, *args, **kwds):
        pass

    def plugin_focus_changed(self, *args, **kwds):
        pass

    def get_spyder_pythonpath(self):
        pass

if __name__ == '__main__':
    instance = QtGui.QApplication.instance()
    if instance is None:
        app = QtGui.QApplication([])

    win = SpyderWin()
    win.show()

    editor = Editor(parent=win)
    editor.load(['setup.py'])
    editor.show()

    if instance is None:
        app.exec_()
