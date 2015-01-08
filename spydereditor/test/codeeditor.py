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

import traceback

from openalea.vpltk.qt import QtGui, QtCore
from openalea.vpltk.qt.QtCore import Signal

from spyderlib.widgets.sourcecode.codeeditor import CodeEditor
from spyderlib.widgets.sourcecode import syntaxhighlighters
from spyderlib.widgets.editor import FileInfo, ThreadManager
from spyderlib.utils import introspection

css = syntaxhighlighters.COLOR_SCHEME_NAMES[0]


class SpyderCodeEditor(CodeEditor):

    def __init__(self, parent=None):
        CodeEditor.__init__(self, parent=parent)

introspector = introspection.PluginManager(None)
editor = CodeEditor(parent=None)
editor.get_completions.connect(introspector.get_completions)
editor.sig_show_object_info.connect(introspector.show_object_info)
editor.go_to_definition.connect(introspector.go_to_definition)


threadmanager = ThreadManager()

finfo = FileInfo('test', 'utf-8', editor, True, threadmanager, introspector)

#self.add_to_data(finfo, set_current)
# finfo.send_to_inspector.connect(self.send_to_inspector)
#finfo.analysis_results_changed.connect(lambda: self.analysis_results_changed.emit())
#finfo.todo_results_changed.connect(lambda: self.todo_results_changed.emit())
#finfo.edit_goto.connect(lambda fname, lineno, name: self.edit_goto.emit(fname, lineno, name))
#finfo.save_breakpoints.connect(lambda s1, s2: self.save_breakpoints.emit(s1, s2))
# editor.run_selection.connect(self.run_selection)
# editor.run_cell.connect(self.run_cell)
# editor.run_cell_and_advance.connect(self.run_cell_and_advance)
# editor.sig_new_file.connect(self.sig_new_file.emit)
#language = get_file_language(fname, txt)
editor.setup_editor(language='Python')

if __name__ == '__main__':
    instance = QtGui.QApplication.instance()
    if instance is None:
        app = QtGui.QApplication([])

    editor.setup_editor(language='Python')
    editor.set_text("print 'hello'")
    editor.show()

    if instance is None:
        app.exec_()
