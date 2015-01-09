# -*- coding: utf-8 -*-
# -*- python -*-
#
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2014 INRIA - CIRAD - INRA
#
#       File author(s): Guillaume Baty <guillaume.baty@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################


from pyqode.python.widgets.code_edit import PyCodeEdit

import sys

from pyqode.core import api
from pyqode.core import modes
from pyqode.core import panels
from openalea.vpltk.qt import QtGui


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # create editor and window
    window = QtGui.QMainWindow()
    editor = PyCodeEdit()
    window.setCentralWidget(editor)

    # start the backend as soon as possible
    editor.backend.start('server.py')

    # append some modes and panels
    editor.modes.append(modes.CodeCompletionMode())
    # editor.modes.append(modes.PygmentsSyntaxHighlighter(editor.document()))
    editor.modes.append(modes.CaretLineHighlighterMode())
    editor.panels.append(panels.SearchAndReplacePanel(),
                         api.Panel.Position.BOTTOM)

    # open a file
    editor.file.open(__file__)

    # run
    window.show()
    app.exec_()
