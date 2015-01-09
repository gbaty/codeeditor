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

from pyqode.python.widgets import PyCodeEdit


class PyCodeEditor(PyCodeEdit):

    def __init__(self, parent=None):
        PyCodeEdit.__init__(self, parent=parent)

    def set_text(self, txt):
        self.setPlainText(txt)

    def get_text(self, start='sof', end='eof'):
        """
        Return a part of the text.

        :param start: is the begining of what you want to get
        :param end: is the end of what you want to get
        :return: text which is contained in the editor between 'start' and 'end'
        """
        txt = self.toPlainText()
        if txt is None:
            txt = ""
        return unicode(txt).replace(u'\u2029', u'\n')  # replace paragraph separators by new lines
