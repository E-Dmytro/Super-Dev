# -*- coding: UTF-8 -*-
from pyrevit import forms
import clr
import math
import System
import sys
from System.Collections.Generic import *

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

pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import random
__doc__='Друк обраних аркушів у PDF'
__author__ = 'Дмитро Серебріян'
from system import *
num=random.randint(0, 10000000)
activeView = doc.ActiveView
pRange = Autodesk.Revit.DB.PrintRange.Select
filepath='C:\\'#forms.pick_folder(title=None)
filetom='КБ1'
#view=doc.ActiveView
set = FilteredElementCollector(doc).WhereElementIsNotElementType().OfClass(ViewSheetSet).ToElements()
p_m = doc.PrintManager
print_setup = p_m.PrintSetup
current_setup = print_setup.CurrentPrintSetting
#print_setup.CurrentPrintSetting = print_setup.InSession
ps = FilteredElementCollector(doc).OfClass(PrintSetting)
print_set_list = []
p_m.SelectNewPrintDriver("Adobe PDF")
p_m.Apply()
sussecc_format=[]
fail_format=[]
form_h = a_1
for k in ps:
	print_set_list.append(k.Name)
def create_print_settings(paper_size, paper_name, page_orientation):
	if paper_name not in print_set_list:
		try:
			p_params = current_setup.PrintParameters
			p_params.PageOrientation = page_orientation
			for i in p_m.PaperSizes:
				if i.Name == paper_size:# or i.Name == 'А2':
					papersize = i
					break
			p_params.PaperSize = papersize
			p_params.PaperPlacement = PaperPlacementType.Margins
			p_params.MarginType = MarginType.NoMargin
			p_params.ZoomType = ZoomType.Zoom
			p_params.Zoom = 100+a_1
			p_params.RasterQuality = RasterQualityType.High
			p_params.ColorDepth = ColorDepthType.BlackLine
			p_params.HiddenLineViews = HiddenLineViewsType.VectorProcessing
			p_params.HideCropBoundaries = True
			p_params.HideReforWorkPlanes = True
			p_params.HideScopeBoxes = True
			p_params.ReplaceHalftoneWithThinLines = False
			p_params.ViewLinksinBlue = False
			p_params.HideUnreferencedViewTags = False
			p_params.MaskCoincidentLines = False
			print_setup.SaveAs(paper_name)
			sussecc_format.append(paper_name)
		except:
			print('Немає налаштувань для '+paper_size)
t= Transaction(doc, 'PrintSettingsAdd')
t.Start()
#print_setup.CurrentPrintSetting = newPrintSetting
#p_m.Apply()
create_print_settings('A0', 'A0A', PageOrientationType.Landscape)
create_print_settings('A0', 'A0K', PageOrientationType.Portrait)
create_print_settings('A1', 'A1A', PageOrientationType.Landscape)
create_print_settings('A1', 'A1K', PageOrientationType.Portrait)
create_print_settings('A2', 'A2A', PageOrientationType.Landscape)
create_print_settings('A2', 'A2K', PageOrientationType.Portrait)
create_print_settings('A3', 'A3A', PageOrientationType.Landscape)
create_print_settings('A3', 'A3K', PageOrientationType.Portrait)
create_print_settings('A4', 'A4A', PageOrientationType.Landscape)
create_print_settings('A4', 'A4K', PageOrientationType.Portrait)

create_print_settings('A0x2', 'A0Ax2', PageOrientationType.Landscape)
create_print_settings('A0x3', 'A0Ax3', PageOrientationType.Landscape)

create_print_settings('A1x3', 'A1Ax3', PageOrientationType.Landscape)
create_print_settings('A1x4', 'A1Ax4', PageOrientationType.Landscape)

create_print_settings('A2x3', 'A2Ax3', PageOrientationType.Landscape)
create_print_settings('A2x4', 'A2Ax4', PageOrientationType.Landscape)
create_print_settings('A2x5', 'A2Ax5', PageOrientationType.Landscape)

create_print_settings('A3x3', 'A3Ax3', PageOrientationType.Landscape)
create_print_settings('A3x4', 'A3Ax4', PageOrientationType.Landscape)
create_print_settings('A3x5', 'A3Ax5', PageOrientationType.Landscape)
create_print_settings('A3x6', 'A3Ax6', PageOrientationType.Landscape)
create_print_settings('A3x7', 'A3Ax7', PageOrientationType.Landscape)

create_print_settings('A4x3', 'A4Ax3', PageOrientationType.Landscape)
create_print_settings('A4x4', 'A4Ax4', PageOrientationType.Landscape)
create_print_settings('A4x5', 'A4Ax5', PageOrientationType.Landscape)
create_print_settings('A4x6', 'A4Ax6', PageOrientationType.Landscape)
create_print_settings('A4x7', 'A4Ax7', PageOrientationType.Landscape)
create_print_settings('A4x8', 'A4Ax8', PageOrientationType.Landscape)


print('Додані формати:')
for i in sussecc_format:
	print(i)
t.Commit()
