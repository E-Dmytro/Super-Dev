# -*- coding: UTF-8 -*-
from module0 import *
import clr
import sys
import Autodesk

from Autodesk.Revit.DB import *
from Autodesk.Revit.Exceptions import *

from Autodesk.Revit.UI import *
#from Autodesk.Revit.UI.Selection import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

RS = Autodesk.Revit.DB.Structure
import math
curview = uidoc.ActiveGraphicalView
from operator import itemgetter
__doc__='Армування стін'
__author__ = 'Дмитро Серебріян'


#path=os.path.dirname(os.path.abspath(__file__))

class CustomISelectionFilter(Selection.ISelectionFilter):
	def __init__(self, nom_categorie):
		self.nom_categorie = nom_categorie
	def AllowElement(self, e):
		if e.Category.Name == self.nom_categorie:
			return True
		else:
			return False
	def AllowReference(self, ref, point):
		return true
def filter_sel(filter_name):
    filter=CustomISelectionFilter(filter_name)
    return filter

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing
import System.Windows.Forms
from System.Drawing import *
from System.Windows.Forms import *
import os
path=os.path.dirname(os.path.abspath(__file__))

all_rebar_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsElementType().ToElements()
rebar_bar_types = []
rebar_hook_types = []
rebar_shapes = []
for rebar_type in all_rebar_types:
	name = rebar_type.GetType().Name
	if name == "RebarBarType":
		rebar_bar_types.append(rebar_type)
	if name == "RebarHookType":
		rebar_hook_types.append(rebar_type)
list_r=[]
list_h=[]
for rebar in rebar_bar_types:
	#d = str(int(rebar.BarDiameter*304.8))
	list_r.append(rebar.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString())
for rebar in rebar_hook_types:
	#d = str(int(rebar.BarDiameter*304.8))
	list_h.append(rebar.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString())



import System.Drawing
import System.Windows.Forms

from System.Drawing import *
#System.Drawing.Drawing2D
from System.Windows.Forms import *
import os
path=os.path.dirname(os.path.abspath(__file__))
MarginWidth = 2
MarginHeight = 2
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
#System.Drawing.Drawing2D
from System.Windows.Forms import *
import os
path=os.path.dirname(os.path.abspath(__file__))
MarginWidth = 2
MarginHeight = 2
class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
		self._values_main = []
	 	self._values_1 = []
		self._values_2 = []
		self._values_3 = []
		self._values_4 = []

	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		#resources = System.Resources.ResourceManager("Form1", System.Reflection.Assembly.GetEntryAssembly())
		self._tabControl1 = System.Windows.Forms.TabControl()
		self._tabPage1 = System.Windows.Forms.TabPage()
		self._tabPage2 = System.Windows.Forms.TabPage()
		self._tabPage3 = System.Windows.Forms.TabPage()
		self._button_Save = System.Windows.Forms.Button()
		self._button_Load = System.Windows.Forms.Button()
		self._button_saveAs = System.Windows.Forms.Button()
		self._textBox_saveAs = System.Windows.Forms.TextBox()
		self._tabPage4 = System.Windows.Forms.TabPage()
		self._button_Ok = System.Windows.Forms.Button()
		self._button_cancel = System.Windows.Forms.Button()
		self._label_M2_2 = System.Windows.Forms.Label()
		self._label_M2_8 = System.Windows.Forms.Label()
		self._label_M2_5 = System.Windows.Forms.Label()
		self._label_M2_7 = System.Windows.Forms.Label()
		self._label_M2_4 = System.Windows.Forms.Label()
		self._label_M2_6 = System.Windows.Forms.Label()
		self._textBox_M2_12 = System.Windows.Forms.TextBox()
		self._label_M2_3 = System.Windows.Forms.Label()
		self._textBox_M2_6 = System.Windows.Forms.TextBox()
		self._textBox_M2_9 = System.Windows.Forms.TextBox()
		self._textBox_M2_11 = System.Windows.Forms.TextBox()
		self._textBox_M2_3 = System.Windows.Forms.TextBox()
		self._textBox_M2_5 = System.Windows.Forms.TextBox()
		self._textBox_M2_8 = System.Windows.Forms.TextBox()
		self._textBox_M2_10 = System.Windows.Forms.TextBox()
		self._textBox_M2_2 = System.Windows.Forms.TextBox()
		self._textBox_M2_4 = System.Windows.Forms.TextBox()
		self._textBox_M2_7 = System.Windows.Forms.TextBox()
		self._textBox_M2_1 = System.Windows.Forms.TextBox()
		self._comboBox_M2_2 = System.Windows.Forms.ComboBox()
		self._comboBox_M2_1 = System.Windows.Forms.ComboBox()
		self._label_M2_1 = System.Windows.Forms.Label()
		self._comboBox_save = System.Windows.Forms.ComboBox()
		self._imageList1 = System.Windows.Forms.ImageList(self._components)
		self._imageList2 = System.Windows.Forms.ImageList(self._components)
		self._comboBox_M2_3 = System.Windows.Forms.ComboBox()
		self._textBox_M2_13 = System.Windows.Forms.TextBox()
		self._textBox_M2_19 = System.Windows.Forms.TextBox()
		self._textBox_M2_16 = System.Windows.Forms.TextBox()
		self._textBox_M2_14 = System.Windows.Forms.TextBox()
		self._textBox_M2_22 = System.Windows.Forms.TextBox()
		self._textBox_M2_20 = System.Windows.Forms.TextBox()
		self._textBox_M2_17 = System.Windows.Forms.TextBox()
		self._textBox_M2_15 = System.Windows.Forms.TextBox()
		self._textBox_M2_23 = System.Windows.Forms.TextBox()
		self._textBox_M2_21 = System.Windows.Forms.TextBox()
		self._textBox_M2_18 = System.Windows.Forms.TextBox()
		self._label_M2_10 = System.Windows.Forms.Label()
		self._textBox_M2_24 = System.Windows.Forms.TextBox()
		self._label_M2_13 = System.Windows.Forms.Label()
		self._label_M2_11 = System.Windows.Forms.Label()
		self._label_M2_14 = System.Windows.Forms.Label()
		self._label_M2_12 = System.Windows.Forms.Label()
		self._label_M2_15 = System.Windows.Forms.Label()
		self._label_M2_16 = System.Windows.Forms.Label()
		self._vertRebar_M1_1 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_3 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_2 = System.Windows.Forms.ComboBox()
		self._vertRebar_M1_4 = System.Windows.Forms.ComboBox()
		self._pictureBox_1_1 = System.Windows.Forms.PictureBox()
		self._textBox_M1_4 = System.Windows.Forms.TextBox()
		self._textBox_M1_3 = System.Windows.Forms.TextBox()
		self._textBox_M1_2 = System.Windows.Forms.TextBox()
		self._textBox_M1_1 = System.Windows.Forms.TextBox()
		self._comboBox_M1_5 = System.Windows.Forms.ComboBox()
		self._comboBox_M1_6 = System.Windows.Forms.ComboBox()
		self._label_M1_1 = System.Windows.Forms.Label()
		self._pictureBox_2_1 = System.Windows.Forms.PictureBox()
		self._pictureBox_2_2 = System.Windows.Forms.PictureBox()
		self._pictureBox_2_3 = System.Windows.Forms.PictureBox()
		self._textBox_M2_25 = System.Windows.Forms.TextBox()
		self._textBox_M2_26 = System.Windows.Forms.TextBox()
		self._textBox_M2_27 = System.Windows.Forms.TextBox()
		self._textBox_M2_28 = System.Windows.Forms.TextBox()
		self._textBox_M2_29 = System.Windows.Forms.TextBox()
		self._textBox_M2_30 = System.Windows.Forms.TextBox()
		self._textBox_M2_31 = System.Windows.Forms.TextBox()
		self._label_M2_18 = System.Windows.Forms.Label()
		self._label_M2_19 = System.Windows.Forms.Label()
		self._label_M2_20 = System.Windows.Forms.Label()
		self._label_M2_17 = System.Windows.Forms.Label()
		self._pictureBox_3_1 = System.Windows.Forms.PictureBox()
		self._textBox_3_5 = System.Windows.Forms.TextBox()
		self._textBox_3_6 = System.Windows.Forms.TextBox()
		self._textBox_3_7 = System.Windows.Forms.TextBox()
		self._textBox_3_8 = System.Windows.Forms.TextBox()
		self._label_3_4 = System.Windows.Forms.Label()
		self._label_3_5 = System.Windows.Forms.Label()
		self._textBox_3_1 = System.Windows.Forms.TextBox()
		self._textBox_3_2 = System.Windows.Forms.TextBox()
		self._label_3_2 = System.Windows.Forms.Label()
		self._textBox_3_3 = System.Windows.Forms.TextBox()
		self._textBox_3_4 = System.Windows.Forms.TextBox()
		self._label_3_9 = System.Windows.Forms.Label()
		self._label_3_1 = System.Windows.Forms.Label()
		self._textBox_3_9 = System.Windows.Forms.TextBox()
		self._textBox_3_10 = System.Windows.Forms.TextBox()
		self._textBox_3_11 = System.Windows.Forms.TextBox()
		self._textBox_3_12 = System.Windows.Forms.TextBox()
		self._label_3_10 = System.Windows.Forms.Label()
		self._label_3_11 = System.Windows.Forms.Label()
		self._textBox_3_13 = System.Windows.Forms.TextBox()
		self._textBox_3_14 = System.Windows.Forms.TextBox()
		self._textBox_3_15 = System.Windows.Forms.TextBox()
		self._textBox_3_16 = System.Windows.Forms.TextBox()
		self._label_3_8 = System.Windows.Forms.Label()
		self._label_3_12 = System.Windows.Forms.Label()
		self._comboBox_3_3 = System.Windows.Forms.ComboBox()
		self._label_3_13 = System.Windows.Forms.Label()
		self._comboBox_3_2 = System.Windows.Forms.ComboBox()
		self._label_3_7 = System.Windows.Forms.Label()
		self._label_3_6 = System.Windows.Forms.Label()
		self._comboBox_3_1 = System.Windows.Forms.ComboBox()
		self._vertRebar_M3_1 = System.Windows.Forms.ComboBox()
		self._vertRebar_M3_2 = System.Windows.Forms.ComboBox()
		self._label_3_15 = System.Windows.Forms.Label()
		self._label_3_16 = System.Windows.Forms.Label()
		self._label_3_14 = System.Windows.Forms.Label()
		self._pictureBox_4_1 = System.Windows.Forms.PictureBox()
		self._textBox_4_1 = System.Windows.Forms.TextBox()
		self._textBox_4_2 = System.Windows.Forms.TextBox()
		self._textBox_4_3 = System.Windows.Forms.TextBox()
		self._textBox_4_5 = System.Windows.Forms.TextBox()
		self._textBox_4_7 = System.Windows.Forms.TextBox()
		self._textBox_4_8 = System.Windows.Forms.TextBox()
		self._textBox_4_10 = System.Windows.Forms.TextBox()
		self._textBox_4_4 = System.Windows.Forms.TextBox()
		self._textBox_4_6 = System.Windows.Forms.TextBox()
		self._textBox_4_9 = System.Windows.Forms.TextBox()
		self._textBox_4_11 = System.Windows.Forms.TextBox()
		self._label_4_1 = System.Windows.Forms.Label()
		self._label_4_2 = System.Windows.Forms.Label()
		self._comboBox_4_2 = System.Windows.Forms.ComboBox()
		self._textBox_4_12 = System.Windows.Forms.TextBox()
		self._gor_arm_4_1 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_2 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_3 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_4 = System.Windows.Forms.ComboBox()
		self._gor_arm_4_5 = System.Windows.Forms.ComboBox()
		self._label_4_5 = System.Windows.Forms.Label()
		self._label_4_6 = System.Windows.Forms.Label()
		self._label_4_7 = System.Windows.Forms.Label()
		self._label_4_8 = System.Windows.Forms.Label()
		self._label_4_9 = System.Windows.Forms.Label()
		self._label_4_4 = System.Windows.Forms.Label()
		self._comboBox_4_1 = System.Windows.Forms.ComboBox()
		self._label_4_3 = System.Windows.Forms.Label()
		self._label_M2_9 = System.Windows.Forms.Label()
		self._button_select = System.Windows.Forms.Button()
		self._tabControl1.SuspendLayout()
		self._tabPage1.SuspendLayout()
		self._tabPage2.SuspendLayout()
		self._tabPage3.SuspendLayout()
		self._tabPage4.SuspendLayout()
		self._pictureBox_1_1.BeginInit()
		self._pictureBox_2_1.BeginInit()
		self._pictureBox_2_2.BeginInit()
		self._pictureBox_2_3.BeginInit()
		self._pictureBox_3_1.BeginInit()
		self._pictureBox_4_1.BeginInit()
		self.SuspendLayout()
		#
		# tabControl1
		#
		self._tabControl1.Controls.Add(self._tabPage1)
		self._tabControl1.Controls.Add(self._tabPage2)
		self._tabControl1.Controls.Add(self._tabPage3)
		self._tabControl1.Controls.Add(self._tabPage4)
		self._tabControl1.Location = System.Drawing.Point(3, 43)
		self._tabControl1.Name = "tabControl1"
		self._tabControl1.SelectedIndex = 0
		self._tabControl1.Size = System.Drawing.Size(987, 493)
		self._tabControl1.TabIndex = 0
		#
		# tabPage1
		#
		self._tabPage1.BackColor = System.Drawing.SystemColors.Control
		self._tabPage1.Controls.Add(self._label_M1_1)
		self._tabPage1.Controls.Add(self._comboBox_M1_6)
		self._tabPage1.Controls.Add(self._textBox_M1_1)
		self._tabPage1.Controls.Add(self._textBox_M1_2)
		self._tabPage1.Controls.Add(self._textBox_M1_3)
		self._tabPage1.Controls.Add(self._textBox_M1_4)
		self._tabPage1.Controls.Add(self._pictureBox_1_1)
		self._tabPage1.Controls.Add(self._vertRebar_M1_4)
		self._tabPage1.Controls.Add(self._comboBox_M1_5)
		self._tabPage1.Controls.Add(self._vertRebar_M1_3)
		self._tabPage1.Controls.Add(self._vertRebar_M1_2)
		self._tabPage1.Controls.Add(self._vertRebar_M1_1)
		self._tabPage1.Location = System.Drawing.Point(4, 22)
		self._tabPage1.Name = "tabPage1"
		self._tabPage1.Padding = System.Windows.Forms.Padding(3)
		self._tabPage1.Size = System.Drawing.Size(979, 467)
		self._tabPage1.TabIndex = 0
		self._tabPage1.Text = "Робочі стрижні"
		#
		# tabPage2
		#
		self._tabPage2.BackColor = System.Drawing.SystemColors.Control
		self._tabPage2.Controls.Add(self._comboBox_M2_3)
		self._tabPage2.Controls.Add(self._pictureBox_2_3)
		self._tabPage2.Controls.Add(self._pictureBox_2_2)
		self._tabPage2.Controls.Add(self._pictureBox_2_1)
		self._tabPage2.Controls.Add(self._label_M2_17)
		self._tabPage2.Controls.Add(self._label_M2_16)
		self._tabPage2.Controls.Add(self._label_M2_2)
		self._tabPage2.Controls.Add(self._label_M2_15)
		self._tabPage2.Controls.Add(self._label_M2_20)
		self._tabPage2.Controls.Add(self._label_M2_9)
		self._tabPage2.Controls.Add(self._label_M2_8)
		self._tabPage2.Controls.Add(self._label_M2_12)
		self._tabPage2.Controls.Add(self._label_M2_5)
		self._tabPage2.Controls.Add(self._label_M2_14)
		self._tabPage2.Controls.Add(self._label_M2_19)
		self._tabPage2.Controls.Add(self._label_M2_7)
		self._tabPage2.Controls.Add(self._label_M2_11)
		self._tabPage2.Controls.Add(self._label_M2_4)
		self._tabPage2.Controls.Add(self._label_M2_13)
		self._tabPage2.Controls.Add(self._label_M2_18)
		self._tabPage2.Controls.Add(self._label_M2_6)
		self._tabPage2.Controls.Add(self._textBox_M2_24)
		self._tabPage2.Controls.Add(self._textBox_M2_12)
		self._tabPage2.Controls.Add(self._label_M2_10)
		self._tabPage2.Controls.Add(self._textBox_M2_18)
		self._tabPage2.Controls.Add(self._label_M2_3)
		self._tabPage2.Controls.Add(self._textBox_M2_31)
		self._tabPage2.Controls.Add(self._textBox_M2_21)
		self._tabPage2.Controls.Add(self._textBox_M2_6)
		self._tabPage2.Controls.Add(self._textBox_M2_23)
		self._tabPage2.Controls.Add(self._textBox_M2_9)
		self._tabPage2.Controls.Add(self._textBox_M2_15)
		self._tabPage2.Controls.Add(self._textBox_M2_11)
		self._tabPage2.Controls.Add(self._textBox_M2_17)
		self._tabPage2.Controls.Add(self._textBox_M2_3)
		self._tabPage2.Controls.Add(self._textBox_M2_30)
		self._tabPage2.Controls.Add(self._textBox_M2_20)
		self._tabPage2.Controls.Add(self._textBox_M2_5)
		self._tabPage2.Controls.Add(self._textBox_M2_22)
		self._tabPage2.Controls.Add(self._textBox_M2_8)
		self._tabPage2.Controls.Add(self._textBox_M2_14)
		self._tabPage2.Controls.Add(self._textBox_M2_10)
		self._tabPage2.Controls.Add(self._textBox_M2_16)
		self._tabPage2.Controls.Add(self._textBox_M2_2)
		self._tabPage2.Controls.Add(self._textBox_M2_27)
		self._tabPage2.Controls.Add(self._textBox_M2_26)
		self._tabPage2.Controls.Add(self._textBox_M2_28)
		self._tabPage2.Controls.Add(self._textBox_M2_25)
		self._tabPage2.Controls.Add(self._textBox_M2_29)
		self._tabPage2.Controls.Add(self._textBox_M2_19)
		self._tabPage2.Controls.Add(self._textBox_M2_4)
		self._tabPage2.Controls.Add(self._textBox_M2_13)
		self._tabPage2.Controls.Add(self._textBox_M2_7)
		self._tabPage2.Controls.Add(self._textBox_M2_1)
		self._tabPage2.Controls.Add(self._comboBox_M2_2)
		self._tabPage2.Controls.Add(self._comboBox_M2_1)
		self._tabPage2.Controls.Add(self._label_M2_1)
		self._tabPage2.Location = System.Drawing.Point(4, 22)
		self._tabPage2.Name = "tabPage2"
		self._tabPage2.Padding = System.Windows.Forms.Padding(3)
		self._tabPage2.Size = System.Drawing.Size(979, 467)
		self._tabPage2.TabIndex = 1
		self._tabPage2.Text = "Кінці стрижня"
		self._tabPage2.Click += self.TabPage2Click
		#
		# tabPage3
		#
		self._tabPage3.BackColor = System.Drawing.SystemColors.Control
		self._tabPage3.Controls.Add(self._comboBox_3_2)
		self._tabPage3.Controls.Add(self._comboBox_3_1)
		self._tabPage3.Controls.Add(self._vertRebar_M3_2)
		self._tabPage3.Controls.Add(self._vertRebar_M3_1)
		self._tabPage3.Controls.Add(self._label_3_13)
		self._tabPage3.Controls.Add(self._comboBox_3_3)
		self._tabPage3.Controls.Add(self._label_3_1)
		self._tabPage3.Controls.Add(self._label_3_12)
		self._tabPage3.Controls.Add(self._label_3_9)
		self._tabPage3.Controls.Add(self._label_3_16)
		self._tabPage3.Controls.Add(self._label_3_11)
		self._tabPage3.Controls.Add(self._label_3_5)
		self._tabPage3.Controls.Add(self._label_3_8)
		self._tabPage3.Controls.Add(self._label_3_6)
		self._tabPage3.Controls.Add(self._textBox_3_16)
		self._tabPage3.Controls.Add(self._label_3_7)
		self._tabPage3.Controls.Add(self._label_3_2)
		self._tabPage3.Controls.Add(self._textBox_3_4)
		self._tabPage3.Controls.Add(self._label_3_14)
		self._tabPage3.Controls.Add(self._label_3_15)
		self._tabPage3.Controls.Add(self._label_3_10)
		self._tabPage3.Controls.Add(self._textBox_3_12)
		self._tabPage3.Controls.Add(self._label_3_4)
		self._tabPage3.Controls.Add(self._textBox_3_15)
		self._tabPage3.Controls.Add(self._textBox_3_8)
		self._tabPage3.Controls.Add(self._textBox_3_3)
		self._tabPage3.Controls.Add(self._textBox_3_14)
		self._tabPage3.Controls.Add(self._textBox_3_11)
		self._tabPage3.Controls.Add(self._textBox_3_2)
		self._tabPage3.Controls.Add(self._textBox_3_7)
		self._tabPage3.Controls.Add(self._textBox_3_13)
		self._tabPage3.Controls.Add(self._textBox_3_10)
		self._tabPage3.Controls.Add(self._textBox_3_1)
		self._tabPage3.Controls.Add(self._textBox_3_9)
		self._tabPage3.Controls.Add(self._textBox_3_6)
		self._tabPage3.Controls.Add(self._textBox_3_5)
		self._tabPage3.Controls.Add(self._pictureBox_3_1)
		self._tabPage3.Location = System.Drawing.Point(4, 22)
		self._tabPage3.Name = "tabPage3"
		self._tabPage3.Padding = System.Windows.Forms.Padding(3)
		self._tabPage3.Size = System.Drawing.Size(979, 467)
		self._tabPage3.TabIndex = 2
		self._tabPage3.Text = "Бокові стрижні"
		#
		# button_Save
		#
		self._button_Save.Location = System.Drawing.Point(12, 12)
		self._button_Save.Name = "button_Save"
		self._button_Save.Size = System.Drawing.Size(75, 23)
		self._button_Save.TabIndex = 1
		self._button_Save.Text = "Зберегти"
		self._button_Save.UseVisualStyleBackColor = True
		self._button_Save.Click += self.Button_SaveClick
		#
		# button_Load
		#
		self._button_Load.Location = System.Drawing.Point(93, 12)
		self._button_Load.Name = "button_Load"
		self._button_Load.Size = System.Drawing.Size(75, 23)
		self._button_Load.TabIndex = 1
		self._button_Load.Text = "Завантажити"
		self._button_Load.UseVisualStyleBackColor = True
		self._button_Load.Click += self.Button_LoadClick
		#
		# button_saveAs
		#
		self._button_saveAs.Location = System.Drawing.Point(427, 12)
		self._button_saveAs.Name = "button_saveAs"
		self._button_saveAs.Size = System.Drawing.Size(88, 23)
		self._button_saveAs.TabIndex = 1
		self._button_saveAs.Text = "Зберегти як"
		self._button_saveAs.UseVisualStyleBackColor = True
		self._button_saveAs.Click += self.Button_saveAsClick
		#
		# textBox_saveAs
		#
		self._textBox_saveAs.Location = System.Drawing.Point(521, 15)
		self._textBox_saveAs.Name = "textBox_saveAs"
		self._textBox_saveAs.Size = System.Drawing.Size(149, 20)
		self._textBox_saveAs.TabIndex = 2
		#
		# tabPage4
		#
		self._tabPage4.BackColor = System.Drawing.SystemColors.Control
		self._tabPage4.Controls.Add(self._comboBox_4_1)
		self._tabPage4.Controls.Add(self._gor_arm_4_5)
		self._tabPage4.Controls.Add(self._gor_arm_4_4)
		self._tabPage4.Controls.Add(self._gor_arm_4_3)
		self._tabPage4.Controls.Add(self._gor_arm_4_2)
		self._tabPage4.Controls.Add(self._gor_arm_4_1)
		self._tabPage4.Controls.Add(self._comboBox_4_2)
		self._tabPage4.Controls.Add(self._label_4_3)
		self._tabPage4.Controls.Add(self._label_4_4)
		self._tabPage4.Controls.Add(self._label_4_2)
		self._tabPage4.Controls.Add(self._label_4_9)
		self._tabPage4.Controls.Add(self._label_4_8)
		self._tabPage4.Controls.Add(self._label_4_7)
		self._tabPage4.Controls.Add(self._label_4_6)
		self._tabPage4.Controls.Add(self._label_4_5)
		self._tabPage4.Controls.Add(self._label_4_1)
		self._tabPage4.Controls.Add(self._textBox_4_11)
		self._tabPage4.Controls.Add(self._textBox_4_10)
		self._tabPage4.Controls.Add(self._textBox_4_9)
		self._tabPage4.Controls.Add(self._textBox_4_8)
		self._tabPage4.Controls.Add(self._textBox_4_12)
		self._tabPage4.Controls.Add(self._textBox_4_7)
		self._tabPage4.Controls.Add(self._textBox_4_6)
		self._tabPage4.Controls.Add(self._textBox_4_4)
		self._tabPage4.Controls.Add(self._textBox_4_5)
		self._tabPage4.Controls.Add(self._textBox_4_3)
		self._tabPage4.Controls.Add(self._textBox_4_2)
		self._tabPage4.Controls.Add(self._textBox_4_1)
		self._tabPage4.Controls.Add(self._pictureBox_4_1)
		self._tabPage4.Location = System.Drawing.Point(4, 22)
		self._tabPage4.Name = "tabPage4"
		self._tabPage4.Padding = System.Windows.Forms.Padding(3)
		self._tabPage4.Size = System.Drawing.Size(979, 467)
		self._tabPage4.TabIndex = 3
		self._tabPage4.Text = "Арматурні хомути"
		#
		# button_Ok
		#
		self._button_Ok.Location = System.Drawing.Point(261, 542)
		self._button_Ok.Name = "button_Ok"
		self._button_Ok.Size = System.Drawing.Size(75, 23)
		self._button_Ok.TabIndex = 1
		self._button_Ok.Text = "Застосувати"
		self._button_Ok.UseVisualStyleBackColor = True
		self._button_Ok.Click += self.Button_OkClick
		#
		# button_cancel
		#
		self._button_cancel.Location = System.Drawing.Point(365, 542)
		self._button_cancel.Name = "button_cancel"
		self._button_cancel.Size = System.Drawing.Size(75, 23)
		self._button_cancel.TabIndex = 1
		self._button_cancel.Text = "Скасувати"
		self._button_cancel.UseVisualStyleBackColor = True
		self._button_cancel.Click += self.Button_cancelClick
		#
		# label_M2_2
		#
		self._label_M2_2.Location = System.Drawing.Point(167, 51)
		self._label_M2_2.Name = "label_M2_2"
		self._label_M2_2.Size = System.Drawing.Size(128, 23)
		self._label_M2_2.TabIndex = 27
		self._label_M2_2.Text = "Вертикальний виліт"
		#
		# label_M2_8
		#
		self._label_M2_8.Location = System.Drawing.Point(18, 273)
		self._label_M2_8.Name = "label_M2_8"
		self._label_M2_8.Size = System.Drawing.Size(99, 23)
		self._label_M2_8.TabIndex = 23
		self._label_M2_8.Text = "Бокові стрижні 2"
		#
		# label_M2_5
		#
		self._label_M2_5.Location = System.Drawing.Point(18, 150)
		self._label_M2_5.Name = "label_M2_5"
		self._label_M2_5.Size = System.Drawing.Size(99, 23)
		self._label_M2_5.TabIndex = 22
		self._label_M2_5.Text = "Бокові стрижні 2"
		#
		# label_M2_7
		#
		self._label_M2_7.Location = System.Drawing.Point(18, 247)
		self._label_M2_7.Name = "label_M2_7"
		self._label_M2_7.Size = System.Drawing.Size(99, 23)
		self._label_M2_7.TabIndex = 21
		self._label_M2_7.Text = "Бокові стрижні 1"
		#
		# label_M2_4
		#
		self._label_M2_4.Location = System.Drawing.Point(18, 127)
		self._label_M2_4.Name = "label_M2_4"
		self._label_M2_4.Size = System.Drawing.Size(99, 23)
		self._label_M2_4.TabIndex = 26
		self._label_M2_4.Text = "Бокові стрижні 1"
		#
		# label_M2_6
		#
		self._label_M2_6.Location = System.Drawing.Point(18, 221)
		self._label_M2_6.Name = "label_M2_6"
		self._label_M2_6.Size = System.Drawing.Size(89, 23)
		self._label_M2_6.TabIndex = 25
		self._label_M2_6.Text = "Кутові стрижні"
		#
		# textBox_M2_12
		#
		self._textBox_M2_12.Enabled = False
		self._textBox_M2_12.Location = System.Drawing.Point(273, 273)
		self._textBox_M2_12.Name = "textBox_M2_12"
		self._textBox_M2_12.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_12.TabIndex = 18
		self._textBox_M2_12.Text = "0"
		#
		# label_M2_3
		#
		self._label_M2_3.Location = System.Drawing.Point(18, 101)
		self._label_M2_3.Name = "label_M2_3"
		self._label_M2_3.Size = System.Drawing.Size(89, 23)
		self._label_M2_3.TabIndex = 24
		self._label_M2_3.Text = "Кутові стрижні"
		#
		# textBox_M2_6
		#
		self._textBox_M2_6.Location = System.Drawing.Point(123, 273)
		self._textBox_M2_6.Name = "textBox_M2_6"
		self._textBox_M2_6.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_6.TabIndex = 17
		self._textBox_M2_6.Text = "0"
		#
		# textBox_M2_9
		#
		self._textBox_M2_9.Enabled = False
		self._textBox_M2_9.Location = System.Drawing.Point(273, 150)
		self._textBox_M2_9.Name = "textBox_M2_9"
		self._textBox_M2_9.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_9.TabIndex = 20
		self._textBox_M2_9.Text = "1000"
		#
		# textBox_M2_11
		#
		self._textBox_M2_11.Enabled = False
		self._textBox_M2_11.Location = System.Drawing.Point(273, 247)
		self._textBox_M2_11.Name = "textBox_M2_11"
		self._textBox_M2_11.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_11.TabIndex = 19
		self._textBox_M2_11.Text = "0"
		#
		# textBox_M2_3
		#
		self._textBox_M2_3.Location = System.Drawing.Point(123, 150)
		self._textBox_M2_3.Name = "textBox_M2_3"
		self._textBox_M2_3.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_3.TabIndex = 11
		self._textBox_M2_3.Text = "1000"
		#
		# textBox_M2_5
		#
		self._textBox_M2_5.Location = System.Drawing.Point(123, 247)
		self._textBox_M2_5.Name = "textBox_M2_5"
		self._textBox_M2_5.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_5.TabIndex = 12
		self._textBox_M2_5.Text = "0"
		#
		# textBox_M2_8
		#
		self._textBox_M2_8.Enabled = False
		self._textBox_M2_8.Location = System.Drawing.Point(273, 124)
		self._textBox_M2_8.Name = "textBox_M2_8"
		self._textBox_M2_8.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_8.TabIndex = 9
		self._textBox_M2_8.Text = "1000"
		#
		# textBox_M2_10
		#
		self._textBox_M2_10.Enabled = False
		self._textBox_M2_10.Location = System.Drawing.Point(273, 221)
		self._textBox_M2_10.Name = "textBox_M2_10"
		self._textBox_M2_10.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_10.TabIndex = 10
		self._textBox_M2_10.Text = "0"
		#
		# textBox_M2_2
		#
		self._textBox_M2_2.Location = System.Drawing.Point(123, 124)
		self._textBox_M2_2.Name = "textBox_M2_2"
		self._textBox_M2_2.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_2.TabIndex = 15
		self._textBox_M2_2.Text = "1000"
		#
		# textBox_M2_4
		#
		self._textBox_M2_4.Location = System.Drawing.Point(123, 221)
		self._textBox_M2_4.Name = "textBox_M2_4"
		self._textBox_M2_4.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_4.TabIndex = 16
		self._textBox_M2_4.Text = "0"
		#
		# textBox_M2_7
		#
		self._textBox_M2_7.Enabled = False
		self._textBox_M2_7.Location = System.Drawing.Point(273, 98)
		self._textBox_M2_7.Name = "textBox_M2_7"
		self._textBox_M2_7.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_7.TabIndex = 13
		self._textBox_M2_7.Text = "1000"
		#
		# textBox_M2_1
		#
		self._textBox_M2_1.Location = System.Drawing.Point(123, 98)
		self._textBox_M2_1.Name = "textBox_M2_1"
		self._textBox_M2_1.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_1.TabIndex = 14
		self._textBox_M2_1.Text = "1000"
		#
		# comboBox_M2_2
		#
		self._comboBox_M2_2.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_M2_2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_M2_2.FormattingEnabled = True
		self._comboBox_M2_2.ItemHeight = 65
		self._comboBox_M2_2.Location = System.Drawing.Point(181, 328)
		self._comboBox_M2_2.Name = "comboBox_M2_2"
		self._comboBox_M2_2.Size = System.Drawing.Size(87, 71)
		self._comboBox_M2_2.TabIndex = 7
		self._comboBox_M2_2.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_M2_2.SelectedIndexChanged += self.ComboBox_M2_1SelectedIndexChanged
		#
		# comboBox_M2_1
		#
		self._comboBox_M2_1.FormattingEnabled = True
		self._comboBox_M2_1.Items.AddRange(System.Array[System.Object](
			["Симетрично",
			"Несиметрично"]))
		self._comboBox_M2_1.Location = System.Drawing.Point(157, 16)
		self._comboBox_M2_1.SelectedIndex = 0
		self._comboBox_M2_1.Name = "comboBox_M2_1"
		self._comboBox_M2_1.Size = System.Drawing.Size(138, 21)
		self._comboBox_M2_1.TabIndex = 8
		self._comboBox_M2_1.SelectedIndexChanged += self.ComboBox_M2_1SelectedIndexChanged
		#
		# label_M2_1
		#
		self._label_M2_1.Location = System.Drawing.Point(18, 16)
		self._label_M2_1.Name = "label_M2_1"
		self._label_M2_1.Size = System.Drawing.Size(143, 23)
		self._label_M2_1.TabIndex = 6
		self._label_M2_1.Text = "Моделювання стрижнів"
		#
		# comboBox_save
		#
		self._comboBox_save.FormattingEnabled = True
		self._comboBox_save.Location = System.Drawing.Point(174, 14)
		self._comboBox_save.Name = "comboBox_save"
		self._comboBox_save.Size = System.Drawing.Size(234, 21)
		self._comboBox_save.TabIndex = 3
		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		location_2 = os.path.realpath(os.path.join(location + '/options/'))
		for f in os.listdir(location_2):
			file_name, file_ext = os.path.splitext(f)
			self._comboBox_save.Items.Add(file_name)
		#
		# imageList1
		#
		#self._imageList1.ColorDepth = System.Windows.Forms.ColorDepth.Depth32Bit
		#self._imageList1.ImageSize = System.Drawing.Size(61, 61)
		#self._imageList1.TransparentColor = System.Drawing.Color.Transparent
		self._imageList2.ColorDepth = System.Windows.Forms.ColorDepth.Depth32Bit
		self._imageList2.ImageSize = System.Drawing.Size(46, 25)
		self._imageList2.Images.Add(Image.FromFile(path+"\img\icon_3_5.PNG"))
		self._imageList2.Images.Add(Image.FromFile(path+"\img\icon_3_6.PNG"))

		self._imageList1.ColorDepth = System.Windows.Forms.ColorDepth.Depth32Bit
		self._imageList1.ImageSize = System.Drawing.Size(61,61)
		#self._imageList1.TransparentColor = System.Drawing.Color.Transparent
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_1_1.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_1_2.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_1_3.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_1_4.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon3.png"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon1.png"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon2.png"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon4.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon5.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_3_1.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_3_2.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_3_3.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_3_4.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_4_1.PNG"))
		self._imageList1.Images.Add(Image.FromFile(path+"\img\icon_4_2.PNG"))
		self._list_1 = [0,1,2,3]
		self._list_2 = [4,5,6]
		self._list_3 = [7,8]
		self._list_4 = [9,10,11,12]
		self._list_5 = [13, 14]
		self._list_6 = [0, 1]
		for idx, val in enumerate(self._imageList1.Images):
			if idx in self._list_1:
				self._comboBox_M1_6.Items.Add(val)
			if idx in self._list_2:
				self._comboBox_M2_2.Items.Add(val)
			if idx in self._list_3:
				self._comboBox_M2_3.Items.Add(val)
			if idx in self._list_4:
				self._comboBox_3_3.Items.Add(val)
			if idx in self._list_5:
				self._comboBox_4_1.Items.Add(val)
		for idx, val in enumerate(self._imageList2.Images):
			if idx in self._list_6:
				self._comboBox_3_1.Items.Add(val)
				self._comboBox_3_2.Items.Add(val)
		self._comboBox_M1_6.SelectedIndex = 0
		self._comboBox_M2_2.SelectedIndex = 0
		self._comboBox_M2_3.SelectedIndex = 1
		self._comboBox_3_3.SelectedIndex = 0
		self._comboBox_4_1.SelectedIndex = 0
		self._comboBox_3_1.SelectedIndex = 1
		self._comboBox_3_2.SelectedIndex = 1
		#
		# comboBox_M2_3
		#
		self._comboBox_M2_3.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_M2_3.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_M2_3.FormattingEnabled = True
		self._comboBox_M2_3.ItemHeight = 65
		self._comboBox_M2_3.Location = System.Drawing.Point(783, 273)
		self._comboBox_M2_3.Name = "comboBox_M2_3"
		self._comboBox_M2_3.Size = System.Drawing.Size(82, 71)
		self._comboBox_M2_3.TabIndex = 7
		self._comboBox_M2_3.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_M2_3.SelectedIndexChanged += self.ComboBox_M2_1SelectedIndexChanged
		#
		# textBox_M2_13
		#
		self._textBox_M2_13.Enabled = False
		self._textBox_M2_13.Location = System.Drawing.Point(485, 98)
		self._textBox_M2_13.Name = "textBox_M2_13"
		self._textBox_M2_13.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_13.TabIndex = 14
		self._textBox_M2_13.Text = "500"
		#
		# textBox_M2_19
		#
		self._textBox_M2_19.Enabled = False
		self._textBox_M2_19.Location = System.Drawing.Point(635, 98)
		self._textBox_M2_19.Name = "textBox_M2_19"
		self._textBox_M2_19.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_19.TabIndex = 13
		self._textBox_M2_19.Text = "500"
		#
		# textBox_M2_16
		#
		self._textBox_M2_16.Location = System.Drawing.Point(485, 221)
		self._textBox_M2_16.Name = "textBox_M2_16"
		self._textBox_M2_16.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_16.TabIndex = 16
		self._textBox_M2_16.Text = "0"
		#
		# textBox_M2_14
		#
		self._textBox_M2_14.Enabled = False
		self._textBox_M2_14.Location = System.Drawing.Point(485, 124)
		self._textBox_M2_14.Name = "textBox_M2_14"
		self._textBox_M2_14.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_14.TabIndex = 15
		self._textBox_M2_14.Text = "500"
		#
		# textBox_M2_22
		#
		self._textBox_M2_22.Enabled = False
		self._textBox_M2_22.Location = System.Drawing.Point(635, 221)
		self._textBox_M2_22.Name = "textBox_M2_22"
		self._textBox_M2_22.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_22.TabIndex = 10
		self._textBox_M2_22.Text = "0"
		#
		# textBox_M2_20
		#
		self._textBox_M2_20.Enabled = False
		self._textBox_M2_20.Location = System.Drawing.Point(635, 124)
		self._textBox_M2_20.Name = "textBox_M2_20"
		self._textBox_M2_20.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_20.TabIndex = 9
		self._textBox_M2_20.Text = "500"
		#
		# textBox_M2_17
		#
		self._textBox_M2_17.Location = System.Drawing.Point(485, 247)
		self._textBox_M2_17.Name = "textBox_M2_17"
		self._textBox_M2_17.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_17.TabIndex = 12
		self._textBox_M2_17.Text = "0"
		#
		# textBox_M2_15
		#
		self._textBox_M2_15.Enabled = False
		self._textBox_M2_15.Location = System.Drawing.Point(485, 150)
		self._textBox_M2_15.Name = "textBox_M2_15"
		self._textBox_M2_15.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_15.TabIndex = 11
		self._textBox_M2_15.Text = "500"
		#
		# textBox_M2_23
		#
		self._textBox_M2_23.Enabled = False
		self._textBox_M2_23.Location = System.Drawing.Point(635, 247)
		self._textBox_M2_23.Name = "textBox_M2_23"
		self._textBox_M2_23.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_23.TabIndex = 19
		self._textBox_M2_23.Text = "0"
		#
		# textBox_M2_21
		#
		self._textBox_M2_21.Enabled = False
		self._textBox_M2_21.Location = System.Drawing.Point(635, 150)
		self._textBox_M2_21.Name = "textBox_M2_21"
		self._textBox_M2_21.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_21.TabIndex = 20
		self._textBox_M2_21.Text = "500"
		#
		# textBox_M2_18
		#
		self._textBox_M2_18.Location = System.Drawing.Point(485, 273)
		self._textBox_M2_18.Name = "textBox_M2_18"
		self._textBox_M2_18.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_18.TabIndex = 17
		self._textBox_M2_18.Text = "0"
		#
		# label_M2_10
		#
		self._label_M2_10.Location = System.Drawing.Point(380, 101)
		self._label_M2_10.Name = "label_M2_10"
		self._label_M2_10.Size = System.Drawing.Size(89, 23)
		self._label_M2_10.TabIndex = 24
		self._label_M2_10.Text = "Кутові стрижні"
		#
		# textBox_M2_24
		#
		self._textBox_M2_24.Enabled = False
		self._textBox_M2_24.Location = System.Drawing.Point(635, 273)
		self._textBox_M2_24.Name = "textBox_M2_24"
		self._textBox_M2_24.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_24.TabIndex = 18
		self._textBox_M2_24.Text = "0"
		#
		# label_M2_13
		#
		self._label_M2_13.Location = System.Drawing.Point(380, 221)
		self._label_M2_13.Name = "label_M2_13"
		self._label_M2_13.Size = System.Drawing.Size(89, 23)
		self._label_M2_13.TabIndex = 25
		self._label_M2_13.Text = "Кутові стрижні"
		#
		# label_M2_11
		#
		self._label_M2_11.Location = System.Drawing.Point(380, 127)
		self._label_M2_11.Name = "label_M2_11"
		self._label_M2_11.Size = System.Drawing.Size(99, 23)
		self._label_M2_11.TabIndex = 26
		self._label_M2_11.Text = "Бокові стрижні 1"
		#
		# label_M2_14
		#
		self._label_M2_14.Location = System.Drawing.Point(380, 247)
		self._label_M2_14.Name = "label_M2_14"
		self._label_M2_14.Size = System.Drawing.Size(99, 23)
		self._label_M2_14.TabIndex = 21
		self._label_M2_14.Text = "Бокові стрижні 1"
		#
		# label_M2_12
		#
		self._label_M2_12.Location = System.Drawing.Point(380, 150)
		self._label_M2_12.Name = "label_M2_12"
		self._label_M2_12.Size = System.Drawing.Size(99, 23)
		self._label_M2_12.TabIndex = 22
		self._label_M2_12.Text = "Бокові стрижні 2"
		#
		# label_M2_15
		#
		self._label_M2_15.Location = System.Drawing.Point(380, 270)
		self._label_M2_15.Name = "label_M2_15"
		self._label_M2_15.Size = System.Drawing.Size(99, 23)
		self._label_M2_15.TabIndex = 23
		self._label_M2_15.Text = "Бокові стрижні 2"
		#
		# label_M2_16
		#
		self._label_M2_16.Location = System.Drawing.Point(529, 51)
		self._label_M2_16.Name = "label_M2_16"
		self._label_M2_16.Size = System.Drawing.Size(122, 23)
		self._label_M2_16.TabIndex = 27
		self._label_M2_16.Text = "Горизонтальний виліт"
		#
		# vertRebar_M1_1
		#
		self._vertRebar_M1_1.FormattingEnabled = True
		self._vertRebar_M1_1.Location = System.Drawing.Point(54, 71)
		self._vertRebar_M1_1.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_1.SelectedIndex = 0
		self._vertRebar_M1_1.Name = "vertRebar_M1_1"
		self._vertRebar_M1_1.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_1.TabIndex = 0
		#
		# vertRebar_M1_3
		#
		self._vertRebar_M1_3.Enabled = False
		self._vertRebar_M1_3.FormattingEnabled = True
		self._vertRebar_M1_3.Location = System.Drawing.Point(269, 71)
		self._vertRebar_M1_3.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_3.SelectedIndex = 0
		self._vertRebar_M1_3.Name = "vertRebar_M1_3"
		self._vertRebar_M1_3.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_3.TabIndex = 0
		#
		# vertRebar_M1_2
		#
		self._vertRebar_M1_2.Enabled = False
		self._vertRebar_M1_2.FormattingEnabled = True
		self._vertRebar_M1_2.Location = System.Drawing.Point(54, 275)
		self._vertRebar_M1_2.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_2.SelectedIndex = 0
		self._vertRebar_M1_2.Name = "vertRebar_M1_2"
		self._vertRebar_M1_2.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_2.TabIndex = 0
		#self._vertRebar_M1_2.SelectedIndexChanged += self.ComboBox7SelectedIndexChanged
		#
		# vertRebar_M1_4
		#
		self._vertRebar_M1_4.Enabled = False
		self._vertRebar_M1_4.FormattingEnabled = True
		self._vertRebar_M1_4.Location = System.Drawing.Point(269, 275)
		self._vertRebar_M1_4.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M1_4.SelectedIndex = 0
		self._vertRebar_M1_4.Name = "vertRebar_M1_4"
		self._vertRebar_M1_4.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M1_4.TabIndex = 0
		#self._vertRebar_M1_4.SelectedIndexChanged += self.ComboBox8SelectedIndexChanged
		#
		# pictureBox_1_1
		#
		self._pictureBox_1_1.Image = Image.FromFile(path+"\img\Main1_1.PNG")
		self._pictureBox_1_1.Location = System.Drawing.Point(152, 98)
		self._pictureBox_1_1.Name = "pictureBox_1_1"
		self._pictureBox_1_1.Size = System.Drawing.Size(148, 171)
		self._pictureBox_1_1.TabIndex = 1
		self._pictureBox_1_1.TabStop = False
		#
		# textBox_M1_4
		#
		self._textBox_M1_4.Location = System.Drawing.Point(306, 239)
		self._textBox_M1_4.Name = "textBox_M1_4"
		self._textBox_M1_4.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_4.TabIndex = 2
		self._textBox_M1_4.Text = "25"
		#
		# textBox_M1_3
		#
		self._textBox_M1_3.Enabled = False
		self._textBox_M1_3.Location = System.Drawing.Point(306, 139)
		self._textBox_M1_3.Name = "textBox_M1_3"
		self._textBox_M1_3.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_3.TabIndex = 2
		self._textBox_M1_3.Text = "25"
		#
		# textBox_M1_2
		#
		self._textBox_M1_2.Enabled = False
		self._textBox_M1_2.Location = System.Drawing.Point(109, 208)
		self._textBox_M1_2.Name = "textBox_M1_2"
		self._textBox_M1_2.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_2.TabIndex = 2
		self._textBox_M1_2.Text = "25"
		#
		# textBox_M1_1
		#
		self._textBox_M1_1.Enabled = False
		self._textBox_M1_1.Location = System.Drawing.Point(109, 107)
		self._textBox_M1_1.Name = "textBox_M1_1"
		self._textBox_M1_1.Size = System.Drawing.Size(52, 20)
		self._textBox_M1_1.TabIndex = 2
		self._textBox_M1_1.Text = "25"
		#
		# comboBox_M1_5
		#
		self._comboBox_M1_5.FormattingEnabled = True
		self._comboBox_M1_5.Items.AddRange(System.Array[System.Object](
			["Однаковий з усіх сторін",
			"Різний з усіх сторін"]))
		self._comboBox_M1_5.Location = System.Drawing.Point(375, 238)
		self._comboBox_M1_5.SelectedIndex = 0
		self._comboBox_M1_5.Name = "comboBox_M1_5"
		self._comboBox_M1_5.Size = System.Drawing.Size(151, 21)
		self._comboBox_M1_5.TabIndex = 0
		self._comboBox_M1_5.SelectedIndexChanged += self.ComboBox_M1_5SelectedIndexChanged
		#
		# comboBox_M1_6
		#
		self._comboBox_M1_6.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_M1_6.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_M1_6.FormattingEnabled = True
		self._comboBox_M1_6.ItemHeight = 65
		self._comboBox_M1_6.Location = System.Drawing.Point(552, 71)
		self._comboBox_M1_6.Name = "comboBox_M1_6"
		self._comboBox_M1_6.Size = System.Drawing.Size(82, 71)
		self._comboBox_M1_6.TabIndex = 8
		self._comboBox_M1_6.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_M1_6.SelectedIndexChanged += self.ComboBox_M1_6SelectedIndexChanged
		#
		# label_M1_1
		#
		self._label_M1_1.Location = System.Drawing.Point(543, 45)
		self._label_M1_1.Name = "label_M1_1"
		self._label_M1_1.Size = System.Drawing.Size(120, 23)
		self._label_M1_1.TabIndex = 9
		self._label_M1_1.Text = "Симетричні умови"
		#
		# pictureBox_2_1
		#
		self._pictureBox_2_1.Image = Image.FromFile(path+"\img\Main2_1.PNG")
		self._pictureBox_2_1.Location = System.Drawing.Point(181, 89)
		self._pictureBox_2_1.Name = "pictureBox_2_1"
		self._pictureBox_2_1.Size = System.Drawing.Size(82, 213)
		self._pictureBox_2_1.TabIndex = 28
		self._pictureBox_2_1.TabStop = False
		#
		# pictureBox_2_2
		#
		self._pictureBox_2_2.Image = Image.FromFile(path+"\img\Main2_2.PNG")
		self._pictureBox_2_2.Location = System.Drawing.Point(543, 89)
		self._pictureBox_2_2.Name = "pictureBox_2_2"
		self._pictureBox_2_2.Size = System.Drawing.Size(82, 213)
		self._pictureBox_2_2.TabIndex = 28
		self._pictureBox_2_2.TabStop = False
		#
		# pictureBox_2_3
		#
		self._pictureBox_2_3.Image = Image.FromFile(path+"\img\Main2_3.PNG")
		self._pictureBox_2_3.Location = System.Drawing.Point(795, 89)
		self._pictureBox_2_3.Name = "pictureBox_2_3"
		self._pictureBox_2_3.Size = System.Drawing.Size(70, 181)
		self._pictureBox_2_3.TabIndex = 28
		self._pictureBox_2_3.TabStop = False
		#
		# textBox_M2_25
		#
		self._textBox_M2_25.Location = System.Drawing.Point(883, 115)
		self._textBox_M2_25.Name = "textBox_M2_25"
		self._textBox_M2_25.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_25.TabIndex = 13
		self._textBox_M2_25.Text = "200"
		#
		# textBox_M2_26
		#
		self._textBox_M2_26.Location = System.Drawing.Point(883, 147)
		self._textBox_M2_26.Name = "textBox_M2_26"
		self._textBox_M2_26.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_26.TabIndex = 13
		self._textBox_M2_26.Text = "40"
		#
		# textBox_M2_27
		#
		self._textBox_M2_27.Enabled = False
		self._textBox_M2_27.Location = System.Drawing.Point(871, 314)
		self._textBox_M2_27.Name = "textBox_M2_27"
		self._textBox_M2_27.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_27.TabIndex = 13
		self._textBox_M2_27.Text = "50"
		#
		# textBox_M2_28
		#
		self._textBox_M2_28.Enabled = False
		self._textBox_M2_28.Location = System.Drawing.Point(813, 350)
		self._textBox_M2_28.Name = "textBox_M2_28"
		self._textBox_M2_28.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_28.TabIndex = 13
		self._textBox_M2_28.Text = "50"
		#
		# textBox_M2_29
		#
		self._textBox_M2_29.Enabled = True
		self._textBox_M2_29.Location = System.Drawing.Point(881, 376)
		self._textBox_M2_29.Name = "textBox_M2_29"
		self._textBox_M2_29.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_29.TabIndex = 16
		self._textBox_M2_29.Text = "50"
		#
		# textBox_M2_30
		#
		self._textBox_M2_30.Enabled = True
		self._textBox_M2_30.Location = System.Drawing.Point(881, 402)
		self._textBox_M2_30.Name = "textBox_M2_30"
		self._textBox_M2_30.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_30.TabIndex = 12
		self._textBox_M2_30.Text = "50"
		#
		# textBox_M2_31
		#
		self._textBox_M2_31.Enabled = True
		self._textBox_M2_31.Location = System.Drawing.Point(881, 428)
		self._textBox_M2_31.Name = "textBox_M2_31"
		self._textBox_M2_31.Size = System.Drawing.Size(52, 20)
		self._textBox_M2_31.TabIndex = 17
		self._textBox_M2_31.Text = "50"
		#
		# label_M2_18
		#
		self._label_M2_18.Location = System.Drawing.Point(776, 376)
		self._label_M2_18.Name = "label_M2_18"
		self._label_M2_18.Size = System.Drawing.Size(89, 23)
		self._label_M2_18.TabIndex = 25
		self._label_M2_18.Text = "Кутові стрижні"
		#
		# label_M2_19
		#
		self._label_M2_19.Location = System.Drawing.Point(776, 402)
		self._label_M2_19.Name = "label_M2_19"
		self._label_M2_19.Size = System.Drawing.Size(99, 23)
		self._label_M2_19.TabIndex = 21
		self._label_M2_19.Text = "Бокові стрижні 1"
		#
		# label_M2_20
		#
		self._label_M2_20.Location = System.Drawing.Point(776, 428)
		self._label_M2_20.Name = "label_M2_20"
		self._label_M2_20.Size = System.Drawing.Size(99, 23)
		self._label_M2_20.TabIndex = 23
		self._label_M2_20.Text = "Бокові стрижні 2"
		#
		# label_M2_17
		#
		self._label_M2_17.Location = System.Drawing.Point(781, 51)
		self._label_M2_17.Name = "label_M2_17"
		self._label_M2_17.Size = System.Drawing.Size(109, 23)
		self._label_M2_17.TabIndex = 27
		self._label_M2_17.Text = "Арматурні вигини"
		#
		# pictureBox_3_1
		#
		self._pictureBox_3_1.Image = Image.FromFile(path+"\img\Main3_1.PNG")
		self._pictureBox_3_1.Location = System.Drawing.Point(158, 145)
		self._pictureBox_3_1.Name = "pictureBox_3_1"
		self._pictureBox_3_1.Size = System.Drawing.Size(145, 188)
		self._pictureBox_3_1.TabIndex = 0
		self._pictureBox_3_1.TabStop = False
		#
		# textBox_3_5
		#
		self._textBox_3_5.Location = System.Drawing.Point(15, 185)
		self._textBox_3_5.Name = "textBox_3_5"
		self._textBox_3_5.Size = System.Drawing.Size(38, 20)
		self._textBox_3_5.TabIndex = 1
		self._textBox_3_5.Text = "2"
		self._textBox_3_5.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_6
		#
		self._textBox_3_6.Location = System.Drawing.Point(15, 211)
		self._textBox_3_6.Name = "textBox_3_6"
		self._textBox_3_6.Size = System.Drawing.Size(136, 20)
		self._textBox_3_6.TabIndex = 1
		self._textBox_3_6.Text = "200"
		self._textBox_3_6.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_7
		#
		self._textBox_3_7.Location = System.Drawing.Point(15, 260)
		self._textBox_3_7.Name = "textBox_3_7"
		self._textBox_3_7.Size = System.Drawing.Size(38, 20)
		self._textBox_3_7.TabIndex = 1
		self._textBox_3_7.Text = "0"
		self._textBox_3_7.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_8
		#
		self._textBox_3_8.Location = System.Drawing.Point(15, 286)
		self._textBox_3_8.Name = "textBox_3_8"
		self._textBox_3_8.Size = System.Drawing.Size(136, 20)
		self._textBox_3_8.TabIndex = 1
		self._textBox_3_8.Text = "0"
		self._textBox_3_8.TextChanged += self.TextBox37TextChanged
		#
		# label_3_4
		#
		self._label_3_4.Location = System.Drawing.Point(15, 159)
		self._label_3_4.Name = "label_3_4"
		self._label_3_4.Size = System.Drawing.Size(100, 23)
		self._label_3_4.TabIndex = 2
		self._label_3_4.Text = "Бокові стрижні 1"
		#
		# label_3_5
		#
		self._label_3_5.Location = System.Drawing.Point(15, 234)
		self._label_3_5.Name = "label_3_5"
		self._label_3_5.Size = System.Drawing.Size(100, 23)
		self._label_3_5.TabIndex = 2
		self._label_3_5.Text = "Бокові стрижні 2"
		#
		# textBox_3_1
		#
		self._textBox_3_1.Location = System.Drawing.Point(167, 67)
		self._textBox_3_1.Name = "textBox_3_1"
		self._textBox_3_1.Size = System.Drawing.Size(38, 20)
		self._textBox_3_1.TabIndex = 1
		self._textBox_3_1.Text = "0"
		self._textBox_3_1.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_2
		#
		self._textBox_3_2.Location = System.Drawing.Point(167, 93)
		self._textBox_3_2.Name = "textBox_3_2"
		self._textBox_3_2.Size = System.Drawing.Size(136, 20)
		self._textBox_3_2.TabIndex = 1
		self._textBox_3_2.Text = "0"
		self._textBox_3_2.TextChanged += self.TextBox37TextChanged
		#
		# label_3_2
		#
		self._label_3_2.Location = System.Drawing.Point(167, 41)
		self._label_3_2.Name = "label_3_2"
		self._label_3_2.Size = System.Drawing.Size(100, 23)
		self._label_3_2.TabIndex = 2
		self._label_3_2.Text = "Бокові стрижні 1"
		#
		# textBox_3_3
		#
		self._textBox_3_3.Location = System.Drawing.Point(322, 67)
		self._textBox_3_3.Name = "textBox_3_3"
		self._textBox_3_3.Size = System.Drawing.Size(38, 20)
		self._textBox_3_3.TabIndex = 1
		self._textBox_3_3.Text = "0"
		self._textBox_3_3.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_4
		#
		self._textBox_3_4.Location = System.Drawing.Point(322, 93)
		self._textBox_3_4.Name = "textBox_3_4"
		self._textBox_3_4.Size = System.Drawing.Size(136, 20)
		self._textBox_3_4.TabIndex = 1
		self._textBox_3_4.Text = "0"
		self._textBox_3_4.TextChanged += self.TextBox37TextChanged
		#
		# label_3_9
		#
		self._label_3_9.Location = System.Drawing.Point(322, 41)
		self._label_3_9.Name = "label_3_9"
		self._label_3_9.Size = System.Drawing.Size(100, 23)
		self._label_3_9.TabIndex = 2
		self._label_3_9.Text = "Бокові стрижні 2"
		#
		# label_3_1
		#
		self._label_3_1.Location = System.Drawing.Point(15, 18)
		self._label_3_1.Name = "label_3_1"
		self._label_3_1.Size = System.Drawing.Size(198, 23)
		self._label_3_1.TabIndex = 3
		self._label_3_1.Text = "Кількість бокових стрижнів / крок"
		#
		# textBox_3_9
		#
		self._textBox_3_9.Enabled = False
		self._textBox_3_9.Location = System.Drawing.Point(322, 185)
		self._textBox_3_9.Name = "textBox_3_9"
		self._textBox_3_9.Size = System.Drawing.Size(38, 20)
		self._textBox_3_9.TabIndex = 1
		self._textBox_3_9.Text = "0"
		self._textBox_3_9.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_10
		#
		self._textBox_3_10.Enabled = False
		self._textBox_3_10.Location = System.Drawing.Point(322, 211)
		self._textBox_3_10.Name = "textBox_3_10"
		self._textBox_3_10.Size = System.Drawing.Size(136, 20)
		self._textBox_3_10.TabIndex = 1
		self._textBox_3_10.Text = "0"
		self._textBox_3_10.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_11
		#
		self._textBox_3_11.Enabled = False
		self._textBox_3_11.Location = System.Drawing.Point(322, 260)
		self._textBox_3_11.Name = "textBox_3_11"
		self._textBox_3_11.Size = System.Drawing.Size(38, 20)
		self._textBox_3_11.TabIndex = 1
		self._textBox_3_11.Text = "0"
		self._textBox_3_11.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_12
		#
		self._textBox_3_12.Enabled = False
		self._textBox_3_12.Location = System.Drawing.Point(322, 286)
		self._textBox_3_12.Name = "textBox_3_12"
		self._textBox_3_12.Size = System.Drawing.Size(136, 20)
		self._textBox_3_12.TabIndex = 1
		self._textBox_3_12.Text = "0"
		self._textBox_3_12.TextChanged += self.TextBox37TextChanged
		#
		# label_3_10
		#
		self._label_3_10.Location = System.Drawing.Point(322, 159)
		self._label_3_10.Name = "label_3_10"
		self._label_3_10.Size = System.Drawing.Size(100, 23)
		self._label_3_10.TabIndex = 2
		self._label_3_10.Text = "Бокові стрижні 2"
		#
		# label_3_11
		#
		self._label_3_11.Location = System.Drawing.Point(322, 234)
		self._label_3_11.Name = "label_3_11"
		self._label_3_11.Size = System.Drawing.Size(100, 23)
		self._label_3_11.TabIndex = 2
		self._label_3_11.Text = "Бокові стрижні 1"
		#
		# textBox_3_13
		#
		self._textBox_3_13.Enabled = False
		self._textBox_3_13.Location = System.Drawing.Point(167, 379)
		self._textBox_3_13.Name = "textBox_3_13"
		self._textBox_3_13.Size = System.Drawing.Size(38, 20)
		self._textBox_3_13.TabIndex = 1
		self._textBox_3_13.Text = "0"
		self._textBox_3_13.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_14
		#
		self._textBox_3_14.Enabled = False
		self._textBox_3_14.Location = System.Drawing.Point(167, 405)
		self._textBox_3_14.Name = "textBox_3_14"
		self._textBox_3_14.Size = System.Drawing.Size(136, 20)
		self._textBox_3_14.TabIndex = 1
		self._textBox_3_14.Text = "0"
		self._textBox_3_14.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_15
		#
		self._textBox_3_15.Enabled = False
		self._textBox_3_15.Location = System.Drawing.Point(322, 379)
		self._textBox_3_15.Name = "textBox_3_15"
		self._textBox_3_15.Size = System.Drawing.Size(38, 20)
		self._textBox_3_15.TabIndex = 1
		self._textBox_3_15.Text = "0"
		self._textBox_3_15.TextChanged += self.TextBox37TextChanged
		#
		# textBox_3_16
		#
		self._textBox_3_16.Enabled = False
		self._textBox_3_16.Location = System.Drawing.Point(322, 405)
		self._textBox_3_16.Name = "textBox_3_16"
		self._textBox_3_16.Size = System.Drawing.Size(136, 20)
		self._textBox_3_16.TabIndex = 1
		self._textBox_3_16.Text = "0"
		self._textBox_3_16.TextChanged += self.TextBox37TextChanged
		#
		# label_3_8
		#
		self._label_3_8.Location = System.Drawing.Point(167, 353)
		self._label_3_8.Name = "label_3_8"
		self._label_3_8.Size = System.Drawing.Size(100, 23)
		self._label_3_8.TabIndex = 2
		self._label_3_8.Text = "Бокові стрижні 1"
		#
		# label_3_12
		#
		self._label_3_12.Location = System.Drawing.Point(322, 353)
		self._label_3_12.Name = "label_3_12"
		self._label_3_12.Size = System.Drawing.Size(100, 23)
		self._label_3_12.TabIndex = 2
		self._label_3_12.Text = "Бокові стрижні 2"
		#
		# comboBox_3_3
		#
		self._comboBox_3_3.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_3_3.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_3_3.FormattingEnabled = True
		self._comboBox_3_3.ItemHeight = 65
		self._comboBox_3_3.Location = System.Drawing.Point(542, 44)
		self._comboBox_3_3.Name = "comboBox_3_3"
		self._comboBox_3_3.Size = System.Drawing.Size(82, 71)
		self._comboBox_3_3.TabIndex = 8
		self._comboBox_3_3.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_3_3.SelectedIndexChanged += self.ComboBox_3_3SelectedIndexChanged
		#
		# label_3_13
		#
		self._label_3_13.Location = System.Drawing.Point(542, 18)
		self._label_3_13.Name = "label_3_13"
		self._label_3_13.Size = System.Drawing.Size(120, 23)
		self._label_3_13.TabIndex = 10
		self._label_3_13.Text = "Симетричні умови"
		#
		# comboBox_3_2
		#
		self._comboBox_3_2.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_3_2.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_3_2.FormattingEnabled = True
		self._comboBox_3_2.ItemHeight = 30
		#self._comboBox_3_2.MeasureItem += self.cboDrawImage_MeasureItem
		self._comboBox_3_2.Location = System.Drawing.Point(322, 119)
		self._comboBox_3_2.Name = "comboBox_3_2"
		self._comboBox_3_2.Size = System.Drawing.Size(82, 36)
		self._comboBox_3_2.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_3_2.TabIndex = 8
		#
		# label_3_7
		#
		self._label_3_7.Location = System.Drawing.Point(235, 122)
		self._label_3_7.Name = "label_3_7"
		self._label_3_7.Size = System.Drawing.Size(100, 23)
		self._label_3_7.TabIndex = 2
		self._label_3_7.Text = "Розміщення"
		#
		# label_3_6
		#
		self._label_3_6.Location = System.Drawing.Point(15, 324)
		self._label_3_6.Name = "label_3_6"
		self._label_3_6.Size = System.Drawing.Size(100, 23)
		self._label_3_6.TabIndex = 2
		self._label_3_6.Text = "Розміщення"
		#
		# comboBox_3_1
		#
		self._comboBox_3_1.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_3_1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_3_1.FormattingEnabled = True
		self._comboBox_3_1.ItemHeight = 30
		self._comboBox_3_1.Location = System.Drawing.Point(15, 350)
		self._comboBox_3_1.Name = "comboBox_3_1"
		self._comboBox_3_1.Size = System.Drawing.Size(82, 36)
		self._comboBox_3_1.DrawItem += self.cboDrawImage_DrawItem
		self._comboBox_3_1.TabIndex = 8
		#
		# vertRebar_M3_1
		#
		self._vertRebar_M3_1.FormattingEnabled = True
		self._vertRebar_M3_1.Location = System.Drawing.Point(542, 236)
		self._vertRebar_M3_1.Name = "vertRebar_M3_1"
		self._vertRebar_M3_1.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M3_1.SelectedIndex = 0
		self._vertRebar_M3_1.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M3_1.TabIndex = 11
		#
		# vertRebar_M3_2
		#
		self._vertRebar_M3_2.FormattingEnabled = True
		self._vertRebar_M3_2.Location = System.Drawing.Point(692, 236)
		self._vertRebar_M3_2.Name = "vertRebar_M3_2"
		self._vertRebar_M3_2.Items.AddRange(System.Array[System.Object](list_r))
		self._vertRebar_M3_2.SelectedIndex = 0
		self._vertRebar_M3_2.Size = System.Drawing.Size(121, 21)
		self._vertRebar_M3_2.TabIndex = 11
		#
		# label_3_15
		#
		self._label_3_15.Location = System.Drawing.Point(563, 208)
		self._label_3_15.Name = "label_3_15"
		self._label_3_15.Size = System.Drawing.Size(100, 23)
		self._label_3_15.TabIndex = 2
		self._label_3_15.Text = "Бокові стрижні 1"
		#
		# label_3_16
		#
		self._label_3_16.Location = System.Drawing.Point(692, 208)
		self._label_3_16.Name = "label_3_16"
		self._label_3_16.Size = System.Drawing.Size(100, 23)
		self._label_3_16.TabIndex = 2
		self._label_3_16.Text = "Бокові стрижні 2"
		#
		# label_3_14
		#
		self._label_3_14.Location = System.Drawing.Point(604, 182)
		self._label_3_14.Name = "label_3_14"
		self._label_3_14.Size = System.Drawing.Size(169, 23)
		self._label_3_14.TabIndex = 2
		self._label_3_14.Text = "Арматура бокових стрижнів"
		#
		# pictureBox_4_1
		#
		self._pictureBox_4_1.Image = Image.FromFile(path+"\img\Main4_1.PNG")
		self._pictureBox_4_1.Location = System.Drawing.Point(18, 42)
		self._pictureBox_4_1.Name = "pictureBox_4_1"
		self._pictureBox_4_1.Size = System.Drawing.Size(119, 249)
		self._pictureBox_4_1.TabIndex = 0
		self._pictureBox_4_1.TabStop = False
		#
		# textBox_4_1
		#
		self._textBox_4_1.Location = System.Drawing.Point(78, 52)
		self._textBox_4_1.Name = "textBox_4_1"
		self._textBox_4_1.Size = System.Drawing.Size(50, 20)
		self._textBox_4_1.TabIndex = 1
		self._textBox_4_1.Text = "50"
		#
		# textBox_4_2
		#
		self._textBox_4_2.Location = System.Drawing.Point(78, 262)
		self._textBox_4_2.Name = "textBox_4_2"
		self._textBox_4_2.Size = System.Drawing.Size(50, 20)
		self._textBox_4_2.TabIndex = 1
		self._textBox_4_2.Text = "50"
		#
		# textBox_4_3
		#
		self._textBox_4_3.Location = System.Drawing.Point(143, 99)
		self._textBox_4_3.Name = "textBox_4_3"
		self._textBox_4_3.Size = System.Drawing.Size(44, 20)
		self._textBox_4_3.TabIndex = 2
		self._textBox_4_3.Text = "100"
		#
		# textBox_4_5
		#
		self._textBox_4_5.Location = System.Drawing.Point(143, 125)
		self._textBox_4_5.Name = "textBox_4_5"
		self._textBox_4_5.Size = System.Drawing.Size(44, 20)
		self._textBox_4_5.TabIndex = 2
		#
		# textBox_4_7
		#
		self._textBox_4_7.Location = System.Drawing.Point(143, 151)
		self._textBox_4_7.Name = "textBox_4_7"
		self._textBox_4_7.Size = System.Drawing.Size(44, 20)
		self._textBox_4_7.TabIndex = 2
		self._textBox_4_7.Text = "200"
		#
		# textBox_4_8
		#
		self._textBox_4_8.Location = System.Drawing.Point(143, 177)
		self._textBox_4_8.Name = "textBox_4_8"
		self._textBox_4_8.Size = System.Drawing.Size(44, 20)
		self._textBox_4_8.TabIndex = 2
		#
		# textBox_4_10
		#
		self._textBox_4_10.Location = System.Drawing.Point(143, 203)
		self._textBox_4_10.Name = "textBox_4_10"
		self._textBox_4_10.Size = System.Drawing.Size(44, 20)
		self._textBox_4_10.TabIndex = 2
		self._textBox_4_10.Text = "100"
		#
		# textBox_4_4
		#
		self._textBox_4_4.Location = System.Drawing.Point(209, 99)
		self._textBox_4_4.Name = "textBox_4_4"
		self._textBox_4_4.Size = System.Drawing.Size(44, 20)
		self._textBox_4_4.TabIndex = 2
		self._textBox_4_4.Text = "10"
		#
		# textBox_4_6
		#
		self._textBox_4_6.Location = System.Drawing.Point(209, 125)
		self._textBox_4_6.Name = "textBox_4_6"
		self._textBox_4_6.Size = System.Drawing.Size(44, 20)
		self._textBox_4_6.TabIndex = 2
		#
		# textBox_4_9
		#
		self._textBox_4_9.Location = System.Drawing.Point(209, 177)
		self._textBox_4_9.Name = "textBox_4_9"
		self._textBox_4_9.Size = System.Drawing.Size(44, 20)
		self._textBox_4_9.TabIndex = 2
		#
		# textBox_4_11
		#
		self._textBox_4_11.Location = System.Drawing.Point(209, 203)
		self._textBox_4_11.Name = "textBox_4_11"
		self._textBox_4_11.Size = System.Drawing.Size(44, 20)
		self._textBox_4_11.TabIndex = 2
		self._textBox_4_11.Text = "10"
		#
		# label_4_1
		#
		self._label_4_1.Location = System.Drawing.Point(153, 73)
		self._label_4_1.Name = "label_4_1"
		self._label_4_1.Size = System.Drawing.Size(34, 23)
		self._label_4_1.TabIndex = 3
		self._label_4_1.Text = "Крок"
		#
		# label_4_2
		#
		self._label_4_2.Location = System.Drawing.Point(209, 73)
		self._label_4_2.Name = "label_4_2"
		self._label_4_2.Size = System.Drawing.Size(56, 23)
		self._label_4_2.TabIndex = 3
		self._label_4_2.Text = "Кількість"
		#
		# comboBox_4_2
		#
		self._comboBox_4_2.FormattingEnabled = True
		self._comboBox_4_2.Items.AddRange(System.Array[System.Object](
			["Точна відстань",
			"Список відстаней"]))
		self._comboBox_4_2.SelectedIndex = 0
		self._comboBox_4_2.Location = System.Drawing.Point(209, 151)
		self._comboBox_4_2.Name = "comboBox_4_2"
		self._comboBox_4_2.Size = System.Drawing.Size(186, 21)
		self._comboBox_4_2.TabIndex = 4
		#
		# textBox_4_12
		#
		self._textBox_4_12.Location = System.Drawing.Point(401, 152)
		self._textBox_4_12.Name = "textBox_4_12"
		self._textBox_4_12.Size = System.Drawing.Size(220, 20)
		self._textBox_4_12.TabIndex = 2
		#
		# gor_arm_4_1
		#
		self._gor_arm_4_1.Enabled = False
		self._gor_arm_4_1.FormattingEnabled = True
		self._gor_arm_4_1.Location = System.Drawing.Point(207, 294)
		self._gor_arm_4_1.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_1.SelectedIndex = 0
		self._gor_arm_4_1.Name = "gor_arm_4_1"
		self._gor_arm_4_1.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_1.TabIndex = 4
		#
		# gor_arm_4_2
		#
		self._gor_arm_4_2.Enabled = False
		self._gor_arm_4_2.FormattingEnabled = True
		self._gor_arm_4_2.Location = System.Drawing.Point(207, 321)
		self._gor_arm_4_2.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_2.SelectedIndex = 0
		self._gor_arm_4_2.Name = "gor_arm_4_2"
		self._gor_arm_4_2.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_2.TabIndex = 4
		#
		# gor_arm_4_3
		#
		self._gor_arm_4_3.FormattingEnabled = True
		self._gor_arm_4_3.Location = System.Drawing.Point(207, 348)
		self._gor_arm_4_3.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_3.SelectedIndex = 0
		self._gor_arm_4_3.Name = "gor_arm_4_3"
		self._gor_arm_4_3.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_3.TabIndex = 4
		#
		# gor_arm_4_4
		#
		self._gor_arm_4_4.Enabled = False
		self._gor_arm_4_4.FormattingEnabled = True
		self._gor_arm_4_4.Location = System.Drawing.Point(207, 375)
		self._gor_arm_4_4.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_4.SelectedIndex = 0
		self._gor_arm_4_4.Name = "gor_arm_4_4"
		self._gor_arm_4_4.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_4.TabIndex = 4
		#
		# gor_arm_4_5
		#
		self._gor_arm_4_5.Enabled = False
		self._gor_arm_4_5.FormattingEnabled = True
		self._gor_arm_4_5.Location = System.Drawing.Point(207, 402)
		self._gor_arm_4_5.Items.AddRange(System.Array[System.Object](list_r))
		self._gor_arm_4_5.SelectedIndex = 0
		self._gor_arm_4_5.Name = "gor_arm_4_5"
		self._gor_arm_4_5.Size = System.Drawing.Size(136, 21)
		self._gor_arm_4_5.TabIndex = 4
		#
		# label_4_5
		#
		self._label_4_5.Location = System.Drawing.Point(177, 294)
		self._label_4_5.Name = "label_4_5"
		self._label_4_5.Size = System.Drawing.Size(22, 23)
		self._label_4_5.TabIndex = 3
		self._label_4_5.Text = "1"
		#
		# label_4_6
		#
		self._label_4_6.Location = System.Drawing.Point(177, 321)
		self._label_4_6.Name = "label_4_6"
		self._label_4_6.Size = System.Drawing.Size(22, 23)
		self._label_4_6.TabIndex = 3
		self._label_4_6.Text = "2"
		#
		# label_4_7
		#
		self._label_4_7.Location = System.Drawing.Point(177, 348)
		self._label_4_7.Name = "label_4_7"
		self._label_4_7.Size = System.Drawing.Size(22, 23)
		self._label_4_7.TabIndex = 3
		self._label_4_7.Text = "3"
		#
		# label_4_8
		#
		self._label_4_8.Location = System.Drawing.Point(177, 375)
		self._label_4_8.Name = "label_4_8"
		self._label_4_8.Size = System.Drawing.Size(22, 23)
		self._label_4_8.TabIndex = 3
		self._label_4_8.Text = "4"
		#
		# label_4_9
		#
		self._label_4_9.Location = System.Drawing.Point(177, 402)
		self._label_4_9.Name = "label_4_9"
		self._label_4_9.Size = System.Drawing.Size(22, 23)
		self._label_4_9.TabIndex = 3
		self._label_4_9.Text = "5"
		#
		# label_4_4
		#
		self._label_4_4.Location = System.Drawing.Point(231, 268)
		self._label_4_4.Name = "label_4_4"
		self._label_4_4.Size = System.Drawing.Size(95, 23)
		self._label_4_4.TabIndex = 3
		self._label_4_4.Text = "Тип арматури"
		#
		# comboBox_4_1
		#
		self._comboBox_4_1.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed
		self._comboBox_4_1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList
		self._comboBox_4_1.FormattingEnabled = True
		self._comboBox_4_1.ItemHeight = 65
		self._comboBox_4_1.Location = System.Drawing.Point(313, 42)
		self._comboBox_4_1.Name = "comboBox_4_1"
		self._comboBox_4_1.Size = System.Drawing.Size(82, 71)
		self._comboBox_4_1.TabIndex = 9
		self._comboBox_4_1.DrawItem += self.cboDrawImage_DrawItem
		#
		# label_4_3
		#
		self._label_4_3.Location = System.Drawing.Point(313, 23)
		self._label_4_3.Name = "label_4_3"
		self._label_4_3.Size = System.Drawing.Size(95, 23)
		self._label_4_3.TabIndex = 3
		self._label_4_3.Text = "Тип розкладки"
		#
		# label_M2_9
		#
		self._label_M2_9.Location = System.Drawing.Point(18, 331)
		self._label_M2_9.Name = "label_M2_9"
		self._label_M2_9.Size = System.Drawing.Size(146, 23)
		self._label_M2_9.TabIndex = 23
		self._label_M2_9.Text = "Напрям кутових стрижнів"
		#
		# button_select
		#
		self._button_select.Location = System.Drawing.Point(21, 542)
		self._button_select.Name = "button_select"
		self._button_select.Size = System.Drawing.Size(175, 23)
		self._button_select.TabIndex = 1
		self._button_select.Text = "Вибрати колони"
		self._button_select.UseVisualStyleBackColor = True
		self._button_select.Click += self.Button_selectClick
		#
		# Form1
		#
		self.AutoScaleMode = System.Windows.Forms.AutoScaleMode.None
		self.ClientSize = System.Drawing.Size(1002, 577)
		self.Controls.Add(self._comboBox_save)
		self.Controls.Add(self._textBox_saveAs)
		self.Controls.Add(self._button_saveAs)
		self.Controls.Add(self._button_Load)
		self.Controls.Add(self._button_select)
		self.Controls.Add(self._button_cancel)
		self.Controls.Add(self._button_Ok)
		self.Controls.Add(self._button_Save)
		self.Controls.Add(self._tabControl1)
		self.ImeMode = System.Windows.Forms.ImeMode.On
		self.KeyPreview = True
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "Form1"
		self.ShowIcon = False
		self.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
		self.Text = "Армування колони"
		self._tabControl1.ResumeLayout(False)
		self._tabPage1.ResumeLayout(False)
		self._tabPage1.PerformLayout()
		self._tabPage2.ResumeLayout(False)
		self._tabPage2.PerformLayout()
		self._tabPage3.ResumeLayout(False)
		self._tabPage3.PerformLayout()
		self._tabPage4.ResumeLayout(False)
		self._tabPage4.PerformLayout()
		self._pictureBox_1_1.EndInit()
		self._pictureBox_2_1.EndInit()
		self._pictureBox_2_2.EndInit()
		self._pictureBox_2_3.EndInit()
		self._pictureBox_3_1.EndInit()
		self._pictureBox_4_1.EndInit()
		self.TopMost = True
		self.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D
		self.ResumeLayout(False)
		self.PerformLayout()

	def cboDrawImage_DrawItem(self, sender, e):
		e.DrawBackground()
		#img = Image.FromFile(path+'\Vupysk.png')
		if e.Index<0:
			return
		img = sender.Items[e.Index]
		hgt = e.Bounds.Height - 2 * MarginHeight
		scale = float(hgt / img.Height)
		#print([e.Bounds.Height, img.Height, hgt, scale, 52/60])
		wid = img.Width * scale
		rect = RectangleF(e.Bounds.X + MarginWidth, e.Bounds.Y + MarginHeight, img.Width, img.Height)#wid, hgt)
		#print([e.Bounds.X + MarginWidth, e.Bounds.Y + MarginHeight, wid, hgt, scale])
		e.Graphics.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBilinear
		e.Graphics.DrawImage(img, rect);
		e.DrawFocusRectangle();
	def cboDrawImage_MeasureItem(self, sender, e):
		if e.Index < 0:
			return
		img = sender.Items[e.Index]
		e.ItemHeight = img.Height + 2 * MarginHeight
		e.ItemWidth = img.Width + 2 * MarginWidth
	def ComboBox1SelectedIndexChanged(self, sender, e):
		pass
	def Label1Click(self, sender, e):
		pass

	def ComboBox2SelectedIndexChanged(self, sender, e):
		if self._comboBox2.SelectedIndex == 0:
			self._textBox7.Enabled = False
			self._textBox8.Enabled = False
			self._textBox9.Enabled = False
			self._textBox11.Enabled = False
			self._textBox13.Enabled = False
			self._textBox15.Enabled = False
			self._textBox3.Enabled = False
			self._textBox19.Enabled = False
			self._textBox23.Enabled = False
			self._textBox18.Enabled = False
			self._textBox22.Enabled = False
			self._textBox25.Enabled = False
		elif self._comboBox2.SelectedIndex == 1:
			self._textBox7.Enabled = True
			self._textBox8.Enabled = True
			self._textBox9.Enabled = True
			self._textBox11.Enabled = True
			self._textBox13.Enabled = True
			self._textBox15.Enabled = True
			self._textBox3.Enabled = True
			self._textBox19.Enabled = True
			self._textBox23.Enabled = True
			self._textBox18.Enabled = True
			self._textBox22.Enabled = True
			self._textBox25.Enabled = True
	def ComboBox_M1_6SelectedIndexChanged(self, sender, e):
		if sender.SelectedIndex == 0:
			self._vertRebar_M1_2.Enabled = False
			self._vertRebar_M1_3.Enabled = False
			self._vertRebar_M1_4.Enabled = False
		elif sender.SelectedIndex == 1:
			self._vertRebar_M1_2.Enabled = False
			self._vertRebar_M1_3.Enabled = True
			self._vertRebar_M1_4.Enabled = False
		elif sender.SelectedIndex == 2:
			self._vertRebar_M1_2.Enabled = True
			self._vertRebar_M1_3.Enabled = False
			self._vertRebar_M1_4.Enabled = False
		elif sender.SelectedIndex == 3:
			self._vertRebar_M1_2.Enabled = True
			self._vertRebar_M1_3.Enabled = True
			self._vertRebar_M1_4.Enabled = True
	def ComboBox_M1_5SelectedIndexChanged(self, sender, e):
		if sender.SelectedIndex == 0:
			self._textBox_M1_1.Enabled = False
			self._textBox_M1_2.Enabled = False
			self._textBox_M1_3.Enabled = False
		if sender.SelectedIndex == 1:
			self._textBox_M1_1.Enabled = True
			self._textBox_M1_2.Enabled = True
			self._textBox_M1_3.Enabled = True
	def ComboBox_M2_1SelectedIndexChanged(self, sender, e):
		if (self._comboBox_M2_1.SelectedIndex) == 0 and (self._comboBox_M2_2.SelectedIndex) == 0:
			self._textBox_M2_7.Enabled = self._textBox_M2_8.Enabled = self._textBox_M2_9.Enabled = self._textBox_M2_10.Enabled = self._textBox_M2_11.Enabled = self._textBox_M2_12.Enabled = False
			self._textBox_M2_13.Enabled = self._textBox_M2_14.Enabled = self._textBox_M2_15.Enabled = self._textBox_M2_19.Enabled = self._textBox_M2_20.Enabled = self._textBox_M2_21.Enabled = False
			self._textBox_M2_22.Enabled = self._textBox_M2_23.Enabled = self._textBox_M2_24.Enabled = False

		elif (self._comboBox_M2_1.SelectedIndex) == 0 and (self._comboBox_M2_2.SelectedIndex == 1 or self._comboBox_M2_2.SelectedIndex == 2):
			self._textBox_M2_7.Enabled = self._textBox_M2_8.Enabled = self._textBox_M2_9.Enabled = self._textBox_M2_10.Enabled = self._textBox_M2_11.Enabled = self._textBox_M2_12.Enabled = False
			self._textBox_M2_13.Enabled = self._textBox_M2_14.Enabled = self._textBox_M2_15.Enabled = True
			self._textBox_M2_19.Enabled = self._textBox_M2_20.Enabled = self._textBox_M2_21.Enabled = self._textBox_M2_22.Enabled = self._textBox_M2_23.Enabled = self._textBox_M2_24.Enabled = False

		elif (self._comboBox_M2_1.SelectedIndex) == 1 and (self._comboBox_M2_2.SelectedIndex == 0):
			self._textBox_M2_7.Enabled = self._textBox_M2_8.Enabled = self._textBox_M2_9.Enabled = self._textBox_M2_10.Enabled = self._textBox_M2_11.Enabled = self._textBox_M2_12.Enabled = True
			self._textBox_M2_13.Enabled = self._textBox_M2_14.Enabled = self._textBox_M2_15.Enabled = self._textBox_M2_19.Enabled = self._textBox_M2_20.Enabled = self._textBox_M2_21.Enabled = False
			self._textBox_M2_22.Enabled = self._textBox_M2_23.Enabled = self._textBox_M2_24.Enabled = True
		elif (self._comboBox_M2_1.SelectedIndex) == 1 and (self._comboBox_M2_2.SelectedIndex == 1 or self._comboBox_M2_2.SelectedIndex == 2):
			self._textBox_M2_7.Enabled = self._textBox_M2_8.Enabled = self._textBox_M2_9.Enabled = self._textBox_M2_10.Enabled = self._textBox_M2_11.Enabled = self._textBox_M2_12.Enabled = True
			self._textBox_M2_13.Enabled = self._textBox_M2_14.Enabled = self._textBox_M2_15.Enabled = self._textBox_M2_22.Enabled = self._textBox_M2_23.Enabled = self._textBox_M2_24.Enabled = True
			self._textBox_M2_19.Enabled = self._textBox_M2_20.Enabled = self._textBox_M2_21.Enabled = self._textBox_M2_22.Enabled = self._textBox_M2_23.Enabled = self._textBox_M2_24.Enabled = True
		if (self._comboBox_M2_2.SelectedIndex == 1 or self._comboBox_M2_2.SelectedIndex == 2):
			self._textBox_M2_25.Enabled	= self._textBox_M2_26.Enabled = False
		#self._textBox_M2_27.Enabled = self._textBox_M2_28.Enabled = self._textBox_M2_29.Enabled = self._textBox_M2_30.Enabled = self._textBox_M2_31.Enabled = False
		elif self._comboBox_M2_2.SelectedIndex == 0:
			self._textBox_M2_25.Enabled	= self._textBox_M2_26.Enabled = True
		if self._comboBox_M2_2.SelectedIndex == 0 and self._comboBox_M2_3.SelectedIndex == 0:
			self._textBox_M2_27.Enabled = self._textBox_M2_28.Enabled = True
			self._textBox_M2_29.Enabled = self._textBox_M2_30.Enabled = self._textBox_M2_31.Enabled = False
		elif self._comboBox_M2_2.SelectedIndex == 0 and self._comboBox_M2_3.SelectedIndex == 1:
			self._textBox_M2_27.Enabled = self._textBox_M2_28.Enabled = False
			self._textBox_M2_29.Enabled = self._textBox_M2_30.Enabled = self._textBox_M2_31.Enabled = True
		elif (self._comboBox_M2_2.SelectedIndex == 1 or self._comboBox_M2_2.SelectedIndex == 2):
			self._textBox_M2_27.Enabled = self._textBox_M2_28.Enabled = False
			self._textBox_M2_29.Enabled = self._textBox_M2_30.Enabled = self._textBox_M2_31.Enabled = False
	def	ComboBox_3_3SelectedIndexChanged(self, sender, e):
		if self._comboBox_3_3.SelectedIndex == 0:
			self._textBox_3_1.Enabled = self._textBox_3_2.Enabled = self._textBox_3_3.Enabled = self._textBox_3_4.Enabled = True
			self._textBox_3_5.Enabled = self._textBox_3_6.Enabled = self._textBox_3_7.Enabled = self._textBox_3_8.Enabled = True
			self._textBox_3_9.Enabled = self._textBox_3_10.Enabled = self._textBox_3_11.Enabled = self._textBox_3_12.Enabled = False
			self._textBox_3_13.Enabled = self._textBox_3_14.Enabled = self._textBox_3_15.Enabled = self._textBox_3_16.Enabled = False
		elif self._comboBox_3_3.SelectedIndex == 1:
			self._textBox_3_1.Enabled = self._textBox_3_2.Enabled = self._textBox_3_3.Enabled = self._textBox_3_4.Enabled = True
			self._textBox_3_5.Enabled = self._textBox_3_6.Enabled = self._textBox_3_7.Enabled = self._textBox_3_8.Enabled = True
			self._textBox_3_9.Enabled = self._textBox_3_10.Enabled = self._textBox_3_11.Enabled = self._textBox_3_12.Enabled = True
			self._textBox_3_13.Enabled = self._textBox_3_14.Enabled = self._textBox_3_15.Enabled = self._textBox_3_16.Enabled = False
		elif self._comboBox_3_3.SelectedIndex == 2:
			self._textBox_3_1.Enabled = self._textBox_3_2.Enabled = self._textBox_3_3.Enabled = self._textBox_3_4.Enabled = True
			self._textBox_3_5.Enabled = self._textBox_3_6.Enabled = self._textBox_3_7.Enabled = self._textBox_3_8.Enabled = True
			self._textBox_3_9.Enabled = self._textBox_3_10.Enabled = self._textBox_3_11.Enabled = self._textBox_3_12.Enabled = False
			self._textBox_3_13.Enabled = self._textBox_3_14.Enabled = self._textBox_3_15.Enabled = self._textBox_3_16.Enabled = True
		elif self._comboBox_3_3.SelectedIndex == 3:
			self._textBox_3_1.Enabled = self._textBox_3_2.Enabled = self._textBox_3_3.Enabled = self._textBox_3_4.Enabled = True
			self._textBox_3_5.Enabled = self._textBox_3_6.Enabled = self._textBox_3_7.Enabled = self._textBox_3_8.Enabled = True
			self._textBox_3_9.Enabled = self._textBox_3_10.Enabled = self._textBox_3_11.Enabled = self._textBox_3_12.Enabled = True
			self._textBox_3_13.Enabled = self._textBox_3_14.Enabled = self._textBox_3_15.Enabled = self._textBox_3_16.Enabled = True

	def TabPage2Click(self, sender, e):
		pass

	def TextBox37TextChanged(self, sender, e):
		pass
	#def label_create(self, tabPage, p1, p2, name, s1, s2, tab, text):
	#	label = System.Windows.Forms.Label()
	#
	#	tabPage.Controls.Add(self._label)
	#	label.Location = System.Drawing.Point(p1, p2)
	#	label.Name = name
	#	label.Size = System.Drawing.Size(s1, s2)
	#	label.TabIndex = tab
	#	label.Text = text

	def Button_selectClick(self, sender, e):
		out_list = []
		try:
			sel = uidoc.Selection.PickObjects(Selection.ObjectType.Element, 'Виберіть елементи у бажаному порядку і натисніть Esc по завершенню')#Несущие колонны filter_sel('Несущие колонны')
			for i in sel:
				selelem = doc.GetElement(i.ElementId)
				out_list.append(selelem)
		except:
			0

		sender.Tag = out_list
		Form1.Focus(self)

	def Button_OkClick(self, sender, e):
		self._values_main=[]
		self._values_1=[]
		self._values_2=[]
		self._values_3=[]
		self._values_4=[]

		self._values_main.append(self._button_select.Tag)#0
		self._values_1.append(self._comboBox_M1_5.SelectedIndex)#0
		self._values_1.append(self._comboBox_M1_6.SelectedIndex)#1
		self._values_1.append(self.arm(self._vertRebar_M1_1))#2
		self._values_1.append(self.arm(self._vertRebar_M1_2))#3
		self._values_1.append(self.arm(self._vertRebar_M1_3))#4
		self._values_1.append(self.arm(self._vertRebar_M1_4))#5
		self._values_1.append(self._textBox_M1_1.Text)#6
		self._values_1.append(self._textBox_M1_2.Text)#7
		self._values_1.append(self._textBox_M1_3.Text)#8
		self._values_1.append(self._textBox_M1_4.Text)#9

		self._values_2.append(self._comboBox_M2_1.SelectedIndex)#0
		self._values_2.append(self._comboBox_M2_2.SelectedIndex)#1
		self._values_2.append(self._comboBox_M2_3.SelectedIndex)#2
		self._values_2.append([self._textBox_M2_1.Text, self._textBox_M2_2.Text, self._textBox_M2_3.Text])#3
		self._values_2.append([self._textBox_M2_4.Text, self._textBox_M2_5.Text, self._textBox_M2_6.Text])#4
		self._values_2.append([self._textBox_M2_7.Text, self._textBox_M2_8.Text, self._textBox_M2_9.Text])#5
		self._values_2.append([self._textBox_M2_10.Text, self._textBox_M2_11.Text, self._textBox_M2_12.Text])#6
		self._values_2.append([self._textBox_M2_13.Text, self._textBox_M2_14.Text, self._textBox_M2_15.Text])#7
		self._values_2.append([self._textBox_M2_16.Text, self._textBox_M2_17.Text, self._textBox_M2_18.Text])#8
		self._values_2.append([self._textBox_M2_19.Text, self._textBox_M2_20.Text, self._textBox_M2_21.Text])#9
		self._values_2.append([self._textBox_M2_22.Text, self._textBox_M2_23.Text, self._textBox_M2_24.Text])#10
		self._values_2.append([self._textBox_M2_25.Text, self._textBox_M2_26.Text, self._textBox_M2_27.Text, self._textBox_M2_28.Text, self._textBox_M2_29.Text, self._textBox_M2_30.Text, self._textBox_M2_31.Text])#11

		self._values_3.append(self._comboBox_3_1.SelectedIndex)#0
		self._values_3.append(self._comboBox_3_2.SelectedIndex)#1
		self._values_3.append(self._comboBox_3_3.SelectedIndex)#2
		self._values_3.append([self._textBox_3_1.Text, self._textBox_3_2.Text, self._textBox_3_3.Text, self._textBox_3_4.Text])#3
		self._values_3.append([self._textBox_3_5.Text, self._textBox_3_6.Text, self._textBox_3_7.Text, self._textBox_3_8.Text])#4
		self._values_3.append([self._textBox_3_9.Text, self._textBox_3_10.Text, self._textBox_3_11.Text, self._textBox_3_12.Text])#5
		self._values_3.append([self._textBox_3_13.Text, self._textBox_3_14.Text, self._textBox_3_15.Text, self._textBox_3_16.Text])#6
		self._values_3.append([self.arm(self._vertRebar_M3_1), self.arm(self._vertRebar_M3_2)])#7


		self._values_4.append(self._comboBox_4_1.SelectedIndex)#0
		self._values_4.append(self._comboBox_4_2.SelectedIndex)#1
		#self._values_4.append(self._comboBox_4_3.SelectedIndex)
		self._values_4.append(self.arm(self._gor_arm_4_1))#2
		self._values_4.append(self.arm(self._gor_arm_4_2))#3
		self._values_4.append(self.arm(self._gor_arm_4_3))#4
		self._values_4.append(self.arm(self._gor_arm_4_4))#5
		self._values_4.append(self.arm(self._gor_arm_4_5))#6
		self._values_4.append([self._textBox_4_1.Text, self._textBox_4_2.Text])#7
		self._values_4.append([self._textBox_4_3.Text, self._textBox_4_4.Text])#8
		self._values_4.append([self._textBox_4_4.Text, self._textBox_4_6.Text])#9
		self._values_4.append([self._textBox_4_7.Text, self._textBox_4_12.Text])#10
		self._values_4.append([self._textBox_4_8.Text, self._textBox_4_9.Text])#11
		self._values_4.append([self._textBox_4_10.Text, self._textBox_4_11.Text])#12
		create_rebar(self._values_main, self._values_1, self._values_2, self._values_3, self._values_4)


		#self.Close()
	def Button_cancelClick(self, sender, e):
		self.Close()

	def Button_SaveClick(self, sender, e):
		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		name = self._comboBox_save.SelectedItem
		if name:
			file = os.path.realpath(os.path.join(location + '/options/'+name+'.txt'))
			location_2 = os.path.realpath(os.path.join(location + '/options/'))
			options_list = [self._vertRebar_M1_1.SelectedIndex, self._vertRebar_M1_2.SelectedIndex, self._vertRebar_M1_3.SelectedIndex, self._vertRebar_M1_4.SelectedIndex, self._textBox_M1_1.Text,
							self._textBox_M1_2.Text,self._textBox_M1_3.Text,self._textBox_M1_4.Text, self._comboBox_M1_5.SelectedIndex, self._comboBox_M1_6.SelectedIndex,
							self._comboBox_M2_1.SelectedIndex, self._comboBox_M2_2.SelectedIndex, self._comboBox_M2_3.SelectedIndex, self._textBox_M2_1.Text, self._textBox_M2_2.Text, self._textBox_M2_3.Text,
							self._textBox_M2_4.Text, self._textBox_M2_5.Text, self._textBox_M2_6.Text, self._textBox_M2_7.Text, self._textBox_M2_8.Text, self._textBox_M2_9.Text, self._textBox_M2_10.Text,
							self._textBox_M2_11.Text, self._textBox_M2_12.Text, self._textBox_M2_13.Text, self._textBox_M2_14.Text, self._textBox_M2_15.Text, self._textBox_M2_16.Text, self._textBox_M2_17.Text,
							self._textBox_M2_18.Text, self._textBox_M2_19.Text, self._textBox_M2_20.Text, self._textBox_M2_21.Text, self._textBox_M2_22.Text, self._textBox_M2_23.Text, self._textBox_M2_24.Text,
							self._textBox_M2_25.Text, self._textBox_M2_26.Text, self._textBox_M2_28.Text, self._textBox_M2_29.Text, self._textBox_M2_30.Text, self._textBox_M2_31.Text,
							self._comboBox_3_1.SelectedIndex, self._comboBox_3_2.SelectedIndex, self._comboBox_3_3.SelectedIndex, self._vertRebar_M3_1.SelectedIndex, self._vertRebar_M3_2.SelectedIndex,
							self._textBox_3_1.Text, self._textBox_3_2.Text, self._textBox_3_3.Text, self._textBox_3_4.Text, self._textBox_3_5.Text, self._textBox_3_6.Text, self._textBox_3_7.Text, self._textBox_3_8.Text,
							self._textBox_3_9.Text, self._textBox_3_10.Text, self._textBox_3_11.Text, self._textBox_3_12.Text, self._textBox_3_13.Text, self._textBox_3_14.Text, self._textBox_3_15.Text, self._textBox_3_16.Text,
							self._comboBox_4_1.SelectedIndex, self._comboBox_4_2.SelectedIndex, self._gor_arm_4_1.SelectedIndex, self._gor_arm_4_2.SelectedIndex, self._gor_arm_4_3.SelectedIndex,self._gor_arm_4_4.SelectedIndex,
							self._gor_arm_4_5.SelectedIndex]
			with open(file, mode='w') as csv_file:
				for i in options_list:
					if isinstance(i, int):
						csv_file.writelines('int ' + str(i)+'\n')
					else:
						csv_file.writelines('str ' + i + '\n')
			self._comboBox_save.Items.Clear()
			for f in os.listdir(location_2):
				file_name, file_ext = os.path.splitext(f)
				self._comboBox_save.Items.Add(file_name)

			for idx, val in enumerate(self._comboBox_save.Items):
				if val == name:
					self._comboBox_save.SelectedIndex = idx
	def Button_LoadClick(self, sender, e):

		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		#print(self._comboBox_save.SelectedItem)
		file = os.path.realpath(os.path.join(location + '/options/'+self._comboBox_save.SelectedItem + '.txt'))
		#print(file)
		with open(file, mode='r') as csv_file:
			line = csv_file.readlines()
		fin_list=[]
		for i in line:
			a = i.replace('\n', '')
			char = a.split(' ')
			if char[0] == 'int':
				fin_list.append(int(char[1]))
			else:
				fin_list.append(char[1])
		self._vertRebar_M1_1.SelectedIndex = fin_list[0]
		self._vertRebar_M1_2.SelectedIndex = fin_list[1]
		self._vertRebar_M1_3.SelectedIndex = fin_list[2]
		self._vertRebar_M1_4.SelectedIndex = fin_list[3]
		self._textBox_M1_1.Text = fin_list[4]
		self._textBox_M1_2.Text = fin_list[5]
		self._textBox_M1_3.Text = fin_list[6]
		self._textBox_M1_4.Text = fin_list[7]
		self._comboBox_M1_5.SelectedIndex = fin_list[8]
		self._comboBox_M1_6.SelectedIndex = fin_list[9]
		self._comboBox_M2_1.SelectedIndex = fin_list[10]
		self._comboBox_M2_2.SelectedIndex = fin_list[11]
		self._comboBox_M2_3.SelectedIndex = fin_list[12]
		self._textBox_M2_1.Text = fin_list[13]
		self._textBox_M2_2.Text = fin_list[14]
		self._textBox_M2_3.Text = fin_list[15]
		self._textBox_M2_4.Text = fin_list[16]
		self._textBox_M2_5.Text = fin_list[17]
		self._textBox_M2_6.Text = fin_list[18]
		self._textBox_M2_7.Text = fin_list[19]
		self._textBox_M2_8.Text = fin_list[20]
		self._textBox_M2_9.Text = fin_list[21]
		self._textBox_M2_10.Text = fin_list[22]
		self._textBox_M2_11.Text = fin_list[23]
		self._textBox_M2_12.Text = fin_list[24]
		self._textBox_M2_13.Text = fin_list[25]
		self._textBox_M2_14.Text = fin_list[26]
		self._textBox_M2_15.Text = fin_list[27]
		self._textBox_M2_16.Text = fin_list[28]
		self._textBox_M2_17.Text = fin_list[29]
		self._textBox_M2_18.Text = fin_list[30]
		self._textBox_M2_19.Text = fin_list[31]
		self._textBox_M2_20.Text = fin_list[32]
		self._textBox_M2_21.Text = fin_list[33]
		self._textBox_M2_22.Text = fin_list[34]
		self._textBox_M2_23.Text = fin_list[35]
		self._textBox_M2_24.Text = fin_list[36]
		self._textBox_M2_25.Text = fin_list[37]
		self._textBox_M2_26.Text = fin_list[38]
		self._textBox_M2_28.Text = fin_list[39]
		self._textBox_M2_29.Text = fin_list[40]
		self._textBox_M2_30.Text = fin_list[41]
		self._textBox_M2_31.Text = fin_list[42]
		self._comboBox_3_1.SelectedIndex = fin_list[43]
		self._comboBox_3_2.SelectedIndex = fin_list[44]
		self._comboBox_3_3.SelectedIndex = fin_list[45]
		self._vertRebar_M3_1.SelectedIndex = fin_list[46]
		self._vertRebar_M3_2.SelectedIndex = fin_list[47]
		self._textBox_3_1.Text = fin_list[48]
		self._textBox_3_2.Text = fin_list[49]
		self._textBox_3_3.Text = fin_list[50]
		self._textBox_3_4.Text = fin_list[51]
		self._textBox_3_5.Text = fin_list[52]
		self._textBox_3_6.Text = fin_list[53]
		self._textBox_3_7.Text = fin_list[54]
		self._textBox_3_8.Text = fin_list[55]
		self._textBox_3_9.Text = fin_list[56]
		self._textBox_3_10.Text = fin_list[57]
		self._textBox_3_11.Text = fin_list[58]
		self._textBox_3_12.Text = fin_list[59]
		self._textBox_3_13.Text = fin_list[60]
		self._textBox_3_14.Text = fin_list[61]
		self._textBox_3_15.Text = fin_list[62]
		self._textBox_3_16.Text = fin_list[63]
		self._comboBox_4_1.SelectedIndex = fin_list[64]
		self._comboBox_4_2.SelectedIndex = fin_list[65]
		self._gor_arm_4_1.SelectedIndex = fin_list[66]
		self._gor_arm_4_2.SelectedIndex = fin_list[67]
		self._gor_arm_4_3.SelectedIndex = fin_list[68]
		self._gor_arm_4_4.SelectedIndex = fin_list[69]
		self._gor_arm_4_5.SelectedIndex = fin_list[70]

	def Button_saveAsClick(self, sender, e):
		name = self._comboBox_save.SelectedItem
		location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
		file = os.path.realpath(os.path.join(location + '/options/'+self._textBox_saveAs.Text+'.txt'))
		location_2 = os.path.realpath(os.path.join(location + '/options/'))
		options_list = [self._vertRebar_M1_1.SelectedIndex, self._vertRebar_M1_2.SelectedIndex, self._vertRebar_M1_3.SelectedIndex, self._vertRebar_M1_4.SelectedIndex, self._textBox_M1_1.Text,
						self._textBox_M1_2.Text,self._textBox_M1_3.Text,self._textBox_M1_4.Text, self._comboBox_M1_5.SelectedIndex, self._comboBox_M1_6.SelectedIndex,
						self._comboBox_M2_1.SelectedIndex, self._comboBox_M2_2.SelectedIndex, self._comboBox_M2_3.SelectedIndex, self._textBox_M2_1.Text, self._textBox_M2_2.Text, self._textBox_M2_3.Text,
						self._textBox_M2_4.Text, self._textBox_M2_5.Text, self._textBox_M2_6.Text, self._textBox_M2_7.Text, self._textBox_M2_8.Text, self._textBox_M2_9.Text, self._textBox_M2_10.Text,
						self._textBox_M2_11.Text, self._textBox_M2_12.Text, self._textBox_M2_13.Text, self._textBox_M2_14.Text, self._textBox_M2_15.Text, self._textBox_M2_16.Text, self._textBox_M2_17.Text,
						self._textBox_M2_18.Text, self._textBox_M2_19.Text, self._textBox_M2_20.Text, self._textBox_M2_21.Text, self._textBox_M2_22.Text, self._textBox_M2_23.Text, self._textBox_M2_24.Text,
						self._textBox_M2_25.Text, self._textBox_M2_26.Text, self._textBox_M2_28.Text, self._textBox_M2_29.Text, self._textBox_M2_30.Text, self._textBox_M2_31.Text,
						self._comboBox_3_1.SelectedIndex, self._comboBox_3_2.SelectedIndex, self._comboBox_3_3.SelectedIndex, self._vertRebar_M3_1.SelectedIndex, self._vertRebar_M3_2.SelectedIndex,
						self._textBox_3_1.Text, self._textBox_3_2.Text, self._textBox_3_3.Text, self._textBox_3_4.Text, self._textBox_3_5.Text, self._textBox_3_6.Text, self._textBox_3_7.Text, self._textBox_3_8.Text,
						self._textBox_3_9.Text, self._textBox_3_10.Text, self._textBox_3_11.Text, self._textBox_3_12.Text, self._textBox_3_13.Text, self._textBox_3_14.Text, self._textBox_3_15.Text, self._textBox_3_16.Text,
						self._comboBox_4_1.SelectedIndex, self._comboBox_4_2.SelectedIndex, self._gor_arm_4_1.SelectedIndex, self._gor_arm_4_2.SelectedIndex, self._gor_arm_4_3.SelectedIndex,self._gor_arm_4_4.SelectedIndex,
						self._gor_arm_4_5.SelectedIndex]
		#print(options_list)
		if self._textBox_saveAs.Text != '':
			with open(file, mode='w') as csv_file:
				for i in options_list:
					if isinstance(i, int):
						csv_file.writelines('int ' + str(i)+'\n')
					else:
						csv_file.writelines('str ' + i + '\n')
			self._comboBox_save.Items.Clear()
			for f in os.listdir(location_2):
				file_name, file_ext = os.path.splitext(f)
				self._comboBox_save.Items.Add(file_name)

			for idx, val in enumerate(self._comboBox_save.Items):
				if val == name:
					self._comboBox_save.SelectedIndex = idx
	def arm(self, e):
		sel_name = e.SelectedItem
		for i in rebar_bar_types:
			name = i.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
			if name == sel_name:
				rebar = i
				break
		return rebar
form = Form1()
try:
	Application.Run(form)
except:
	0
