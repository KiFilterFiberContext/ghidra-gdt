# Exports a Ghidra Data Type (GDT) archive for the current program
# @author 13laze
# @menupath Tools.Data Types.ExportGDT
# @category Data Types

from ghidra.util import Msg
from ghidra.program.model.data import FileDataTypeManager
from ghidra.app.script import GhidraScript
from ghidra.app.cmd.function import CaptureFunctionDataTypesCmd
from docking.widgets.filechooser import GhidraFileChooser
from ghidra.util.task import TaskMonitor

chooser = GhidraFileChooser(None)

chooser.setTitle("Choose GDT Archive Path")
chooser.setApproveButtonText("Save As");
chooser.setMultiSelectionEnabled(False);

f = chooser.getSelectedFile(True)

dtm = FileDataTypeManager.createFileArchive(f)
cmd = CaptureFunctionDataTypesCmd(dtm, currentProgram.getMemory(), None)
cmd.applyTo(currentProgram, TaskMonitor.DUMMY)

dtm.save()
dtm.close()
