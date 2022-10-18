# -*- coding: UTF-8 -*-
from pyrevit import forms
import clr

import math
import System

import Autodesk
from Autodesk.Revit.DB import *
dupopt = Autodesk.Revit.DB.ViewDuplicateOption.Duplicate
#doc = DocumentManager.Instance.CurrentDBDocument
doc = __revit__.ActiveUIDocument.Document
#uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
uidoc = __revit__.ActiveUIDocument
curview = uidoc.ActiveGraphicalView

#uiapp = DocumentManager.Instance.CurrentUIApplication
#app = uiapp.Application

import Autodesk.Revit.DB as RVT
RS = RVT.Structure
curview = uidoc.ActiveGraphicalView
from operator import itemgetter
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random
__doc__='Видалити налаштування друку'
__author__ = 'Дмитро Серебріян'
from system import *
#sheets_list= forms.select_sheets(title='Оберіть аркуші', button_name='Підтвердити', width=500, multiple=True,filterfunc=None, doc=None)

#sel = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

#for sel in selection:
#	sheets_list.append(sel)
start_p = point_1
num=random.randint(0, 10000000)
activeView = doc.ActiveView
pRange = Autodesk.Revit.DB.PrintRange.Select
filepath='C:\\'#forms.pick_folder(title=None)
filetom='КБ1'
#view=doc.ActiveView
set = FilteredElementCollector(doc).WhereElementIsNotElementType().OfClass(ViewSheetSet).ToElements()
p_m = doc.PrintManager
p_m.SelectNewPrintDriver("Adobe PDF")
p_m.Apply()
print_setup = p_m.PrintSetup
current_setup = print_setup.CurrentPrintSetting
print_setup.CurrentPrintSetting = print_setup.InSession
ps = FilteredElementCollector(doc).OfClass(PrintSetting)
print_set_list = []
#for k in ps:
#	print_set_list.append(k.Name)
#	newPrintSetting = k
t= Transaction(doc, 'PrintSettingsDel')
t.Start()
fin_list=[]
for i in ps:
	fin_list.append(i)
for k in fin_list:
	try:
		print_setup.CurrentPrintSetting = print_setup.InSession
		print_setup.CurrentPrintSetting = k
		print_setup.Delete()
		print('ok')
	except:
		print('fail')
print('Finish')
t.Commit()
