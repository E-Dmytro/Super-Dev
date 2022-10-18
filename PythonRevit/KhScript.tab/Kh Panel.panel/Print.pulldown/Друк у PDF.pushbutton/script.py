# -*- coding: UTF-8 -*-
from ctypes.wintypes import RGB
from pyrevit import forms
import clr
import pyrevit
from pyrevit.forms import WPFWindow
import math
import System


# Import ToDSType(bool) extension method
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

version_r = pyrevit._HostApplication().version

#app = uiapp.Application
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import Autodesk.Revit.DB as RVT
RS = RVT.Structure
curview = uidoc.ActiveGraphicalView
from operator import itemgetter

import random
from system import *
__doc__='Print PDF'
__author__ = 'DmytroKhom'

sheets_list= forms.select_sheets(title='Choose Layout', button_name='Select', width=500, multiple=True,filterfunc=None, doc=None)
class ModelessForm(WPFWindow):
    """
    Simple modeless form sample
    """
    def __init__(self, xaml_file_name):
        WPFWindow.__init__(self, xaml_file_name)
        #self.simple_text.Text = "Hello World"
        self.out_list = 5
        self.show_dialog()
    def ok_click(self, sender, e):
		self.out_list=1
		self.Close()
    def no_click(self, sender, e):
		self.out_list=0
		self.Close()
# Let's launch our beautiful and useful form !
modeless_form = ModelessForm("ModelessForm.xaml")
result = modeless_form.out_list
#sel = [ doc.GetElement( elId ) for elId in uidoc.Selection.GetElementIds() ]

#for sel in selection:
#	sheets_list.append(sel)
num=random.randint(0, 10000000)
activeView = doc.ActiveView
pRange = Autodesk.Revit.DB.PrintRange.Select
filepath='C:\\'#forms.pick_folder(title=None)
filetom='КБ1'
#view=doc.ActiveView
set = FilteredElementCollector(doc).WhereElementIsNotElementType().OfClass(ViewSheetSet).ToElements()
p_m = doc.PrintManager
#view = p_m.ViewSheetSetting
newNames = []


sheets_col = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).ToElements()
views_col = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).ToElements()
"""
for i in sheets_col:
	tom = i.LookupParameter('Орг.КомплектКреслень').AsString()
	print_doc=i.LookupParameter('Утвердил').AsString()

        #tom==filetom
	if print_doc=="+":
                sheets_list.append(i)
"""
print('-----------PrintManager v 1.2 (c)D.Serebriian------------')
print_success=[]
print_fail=[]
print_check = a_1
import _winreg
for j in sheets_list:
    """
    reg_connection = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
    pjcKey = _winreg.OpenKey(reg_connection, r"Software\Adobe\Acrobat Distiller\PrinterJobControl", 0, _winreg.KEY_ALL_ACCESS)
    appPath = r"C:\Program Files\Autodesk\Revit " + version_r + r"\Revit.exe"
        #pjcKey.SetValueEx(appPath, '1.pdf')
    _winreg.SetValueEx(pjcKey, "LastPdfPortFolder - Revit.exe",0, _winreg.REG_SZ, 'D:\\')
    _winreg.SetValueEx(pjcKey, appPath,0, _winreg.REG_SZ, 'D:\\1.pdf')
    #pjcKey.SetValueEx("LastPdfPortFolder - Revit.exe", 'C:\\')
    #_winreg.CloseKey(pjcKey)
    """
    sheet_el=[]
    #print(1)
    for e in FilteredElementCollector(doc).OwnedByView(j.Id):
    	sheet_el.append(e)
    t_block_list = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_TitleBlocks).ToElements()

    for v in sheet_el:
    	for a in t_block_list:
    		if v.GetTypeId().IntegerValue == a.Id.IntegerValue and v.Name=='Універсальний':
    			t_block = v
    			t_page = a
    			break
    #print(2)
    t_par1 = t_block.LookupParameter('Формат').AsValueString()
    t_par2 = t_block.LookupParameter('Книжний').AsValueString()
    t_par3 = t_block.LookupParameter('Мультиплікатор_розрахунок').AsValueString()
    try:
    	zm = j.LookupParameter('Орг.Зміна').AsString()
    except:
    	zm = "зм.0"
    s_num = j.get_Parameter(BuiltInParameter.SHEET_NUMBER).AsString()
    s_name = j.get_Parameter(BuiltInParameter.SHEET_NAME).AsString()
    if zm == '' or zm == None:
    	zm='зм.0'
    if t_par2 == 'Да' or t_par2 == 'Yes':
    	form = 'K'
    else:
    	form = 'A'
    #s_tom=j.LookupParameter('Орг.КомплектКреслень').AsString()
    #print(3)
    viewSet = ViewSet()
    viewSet.Insert(j)
    p_m.PrintRange = pRange
    p_m.Apply()
    viewSheetSetting = p_m.ViewSheetSetting
    viewSheetSetting.CurrentViewSheetSet.Views = viewSet
    p_m.SelectNewPrintDriver("Adobe PDF")
    g_l_2 = b_1
    print("10%")
    p_m.Apply()
    p_m.CombinedFile = True
    #print("20%")
    p_m.Apply()
    p_m.PrintToFile = True
    #print("30%")
    p_m.Apply()
    print("40%")
    filename=j.Name
    block_name =['\\','/',':', '*', '?', ' <', '>','|', "'", '"']
    for i in block_name:
    	#print(i)
    	if i in filename:
    		#print('ok')
    		filename = filename.replace(i,' ')
    #if '\' or ''
    #print(filename)
    if str(int(t_par3)) !='1':
        m='x'+str(int(t_par3))
    else:
        m=''
    printSetting = 'A'+str(int(t_par1))+form+m

    p_m.PrintToFileName = str(filepath)+printSetting+"_"+s_num+"_"+filename+"_"+zm+".pdf"
    #print(8)
    p_m.Apply()
    #print("50%")
    #viewSetting=s_tom+:"КБ1: А2А"
    #for e in set:
    #	if e.Name == viewSetting:
    #		view.CurrentViewSheetSet = e
    t = Transaction(doc,'Print')
    t.Start()

    if str(int(t_par3)) !='1':
        m='x'+str(int(t_par3))
    else:
        m=''
    printSetting = 'A'+str(int(t_par1))+form+m
    #print("60%")
    ps = FilteredElementCollector(doc).OfClass(PrintSetting)
    newPrintSetting = False
    for k in ps:
    	#print(k.Name)
    	#print(printSetting)
    	if k.Name == printSetting:
    		newPrintSetting = k
    		break
    if newPrintSetting != False:
    	printSetup = p_m.PrintSetup
    	printSetup.CurrentPrintSetting = newPrintSetting
    	print("70%")
    	p_m.Apply()
    	try:
    		if result==1:
    			#print('+')
    			current_setup = printSetup.CurrentPrintSetting
    			p_params = current_setup.PrintParameters
    			p_params.ColorDepth = ColorDepthType.Color
    			printSetup.Save()
    		else:
    			#print('+')
    			current_setup = printSetup.CurrentPrintSetting
    			p_params = current_setup.PrintParameters
    			p_params.ColorDepth = ColorDepthType.BlackLine
    			printSetup.Save()
    	except:
    		0
    	viewSheetSetting.SaveAs("tempSetName"+str(num))
    	num+=1
    	print("80%")
    	p_m.Apply()
    	try:
    		p_m.SubmitPrint()
    		print("90%")
    		p_m.Apply()
    		viewSheetSetting.Delete()
    		print("100%")
    		print('Аркуш надруковано: ' + s_num+"_"+filename)
    		print_success.append(s_num+"_"+filename)
    	except:
    		print('Помилка при друці ' + s_num+"_"+filename)
    		print_fail.append(s_num+"_"+filename)
    else:
    	print('Некоректне налаштування друку для аркуша ' + s_num+"_"+filename)
    	print_fail.append(s_num+"_"+filename)
    t.Commit()
if len(print_success)>0:
	print(' ')
	print('--------АРКУШІ РОЗДРУКОВАНІ--------:')
	for i in print_success:
		print(i)
	print(' ')
if len(print_fail)>0:
	print('--------НЕ РОЗДРУКОВАНІ АРКУШІ--------:')
	for i in print_fail:
		print(i)
