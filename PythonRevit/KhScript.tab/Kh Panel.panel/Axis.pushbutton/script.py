# -*- coding: UTF-8 -*-
# import Autodesk
# from Autodesk.Revit.DB import *
# from Autodesk.Revit.UI import *
# from pyrevit.forms import WPFWindow
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument


# class ModalForm(WPFWindow):
# 	def __init__(self, xaml_file_name):
# 		WPFWindow.__init__(self, xaml_file_name)
# 		self.ShowDialog()
# 	def select_push_button(self, sender, e):
# 		self.hide()
# 		sel = uidoc.Selection.PickObjects(Selection.ObjectType.Element, 'Choose elements')
# 		self.els = [doc.GetElement( elId ) for elId in sel]
# 		self.ShowDialog()

# 	def ok_button_push(self, sender, e):
# 		par_name = self.text_input.Text
# 		par_value = self.value_input.Text

# 		t = Transaction(doc, 'change parameter')
# 		t.Start()
# 		try:
# 			for i in self.els:
# 				i.LookupParameter(par_name).Set(par_value)
# 		except:
# 			TaskDialog.Show('error', 'error message')
# 		t.Commit()
# 		self.Close()
# 	def cancel_button(self, sender, e):
# 		self.Close()
# form = ModalForm('interface.xaml')

import Autodesk
from Autodesk.Revit.DB import *
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
doc = __revit__.ActiveUIDocument.Document
import itertools
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

p_1 = XYZ(0,0,0)
p_2 = XYZ(0,11000,0)
line_1 = Line.CreateBound(p_1, p_2)

t = Transaction(doc, 'grid')
t.Start()
grid_1 = Grid.Create(doc, line_1)
name = grid_1.get_Parameter(BuiltInParameter.DATUM_TEXT)
name.Set('A322')
t.Commit()