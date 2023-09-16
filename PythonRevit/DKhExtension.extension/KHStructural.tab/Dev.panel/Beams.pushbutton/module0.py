# -*- coding: UTF-8 -*-
#from module import *
# -*- coding: UTF-8 -*-
import clr
from operator import itemgetter
import math
import Autodesk
from Autodesk.Revit.DB import *
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
from system import *
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
RS = Autodesk.Revit.DB.Structure
__doc__='Армування колони'
__author__ = 'Дмитро Серебріян'
curview = uidoc.ActiveGraphicalView
from System.Collections.Generic import *
def create_rebar(list_export):
    _values_main = list_export[0]
    _values_1 = list_export[1]
    _values_2 = list_export[2]
    def step_vert(b_rebar_list, b_rebar_count):
        f2=[]
        for i in b_rebar_list:
            if '*' in i:
                k=i.split('*')
                for j in range(int(k[1])):
                    f2.append(k[0])
            else:
                f2.append(i)

        f1 = b_rebar_count
        if len(f2)>f1:
            f2=f2[:f1]

        t_list=[]
        co = 0

        while len(f2)!=f1:
            co+=1
            f2.append(f2[-1])
            if co==50:
                break

        f2.append('45687798')
        count=0
        num=1

        for i in f2:
            if i==f2[count-1] and count!=0:
                num+=1
            elif i != f2[count-1] and count!=0:
                t_list.append(str(f2[count-1])+'*'+str(num))
                num=1
            count+=1
            if count+1 == len(f2):
                t_list.append(str(f2[count-1])+'*'+str(num))
                count+=1
        #print(t_list)
        return t_list
    #------Типи арматури------------------
    all_rebar_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsElementType().ToElements()
    rebar_bar_types = []
    rebar_hook_types = []
    rebar_shapes = []
    for rebar_type in all_rebar_types:
    	name = rebar_type.GetType().Name
    	if name == "RebarBarType":
    		rebar_bar_types.append(rebar_type)
    	elif name == "RebarHookType":
    		rebar_hook_types.append(rebar_type)
    	elif name == "RebarShape":
    		rebar_shapes.append(rebar_type)
    r_orient = RS.RebarHookOrientation()
    #rebar_filter = ElementCategoryFilter(BuiltInCategory.OST_Rebar)
    rebars = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rebar).WhereElementIsNotElementType().ToElements()
    shape_s=None
    for sh in rebar_shapes:
            sh_name=sh.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
            if sh_name == 'M_T1':  # ТУТ ЗВЕРНУТИ УВАГУ
                     shape_s=sh

    hook_s=None
    for hook in rebar_hook_types:
            hook_name=hook.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
            if hook_name == "Stirrup/Tie Seismic - 135 deg.": # ТУТ ЗВЕРНУТИ УВАГУ
                    hook_s=hook

    ##--------------Вхідні дані--------------------
    hook_type_vert=None
    columns = _values_main[0]
    result_1 = _values_1
    result_2 = _values_2

    list_params = ['b', 'h'] # ТУТ ЗВЕРНУТИ УВАГУ
    par_height = list_params[1]
    par_width = list_params[0]
    vert_rebar_1 = result_1[2]
    vert_rebar_2 = result_1[3]
    vert_rebar_3 = result_1[4]
    vert_rebar_4 = result_1[7]
    vert_rebar_5 = result_1[6]
    vert_rebar_6 = result_1[5]
    vert_rebar_7 = result_1[8]
    v_d1 = vert_rebar_1.BarDiameter
    v_d2 = vert_rebar_2.BarDiameter
    v_d3 = vert_rebar_3.BarDiameter
    v_d4 = vert_rebar_4.BarDiameter
    v_d5 = vert_rebar_5.BarDiameter
    v_d6 = vert_rebar_6.BarDiameter
    v_d7 = vert_rebar_7.BarDiameter


    cover_1 = int(result_1[9][3])/304.8
    cover_2 = int(result_1[9][0])/304.8
    cover_3 = int(result_1[9][1])/304.8
    cover_4 = int(result_1[9][2])/304.8

    rebar_lines_step_1 = result_1[11][0]
    rebar_lines_step_2 = result_1[11][1]
    rebar_lines_step_3 = result_1[11][2]
    rebar_lines_step_4 = result_1[11][3]

    rebar_vect_1 = result_1[0]
    rebar_vect_2 = result_1[1]

    b_rebar_1_count = int(result_1[10][0])
    b_rebar_2_count = int(result_1[10][1])
    b_rebar_3_count = int(result_1[10][2])
    b_rebar_4_count = int(result_1[10][5])
    b_rebar_5_count = int(result_1[10][4])
    b_rebar_6_count = int(result_1[10][3])
    b_rebar_7_count = int(result_1[10][6])

    b_rebar_1_step = result_1[12][0]
    #print(b_rebar_1_step)
    b_rebar_1_step = b_rebar_1_step.split(' ')

    b_rebar_2_step = result_1[12][1]
    b_rebar_2_step = b_rebar_2_step.split(' ')
    #print(b_rebar_2_step)

    vert_b_1 = step_vert(b_rebar_1_step, b_rebar_1_count)
    vert_b_2 = step_vert(b_rebar_1_step, b_rebar_2_count)
    vert_b_3 = step_vert(b_rebar_1_step, b_rebar_3_count)
    vert_b_4 = step_vert(b_rebar_2_step, b_rebar_4_count)
    vert_b_5 = step_vert(b_rebar_2_step, b_rebar_5_count)
    vert_b_6 = step_vert(b_rebar_2_step, b_rebar_6_count)
    vert_b_7 = step_vert(b_rebar_1_step, b_rebar_7_count)

    left_offset = result_2[17]
    right_offset = result_2[18]

    gor_rebar_1 =result_2[2]
    gor_rebar_2 =result_2[2]
    gor_rebar_3 =result_2[2]
    gor_rebar_4 =result_2[2]
    gor_rebar_5 =result_2[2]
    g_d1 = gor_rebar_1.BarDiameter
    g_d2 = gor_rebar_2.BarDiameter
    g_d3 = gor_rebar_3.BarDiameter
    g_d4 = gor_rebar_4.BarDiameter
    g_d5 = gor_rebar_5.BarDiameter

    g_left_offset = int(result_2[5])/304.8 + b_1
    g_right_offset = int(result_2[6])/304.8 + b_1
    g_rebar_1_count = int(result_2[8]) + b_1
    g_rebar_1_step = int(result_2[7])/304.8 + b_1

    #g_rebar_2_count = int(result_2[10])
    #g_rebar_2_step = int(result_2[9])/304.8
    g_rebar_3_step = int(result_2[11])/304.8
    #g_rebar_4_count = int(result_2[13])
    #g_rebar_4_step = int(result_2[12])/304.8

    g_rebar_5_count = int(result_2[15])
    g_rebar_5_step = int(result_2[14])/304.8

    #g_rebar_4_count = int(result_2[14])/304.8

    def get_zs(el,parameter):
    	zs_id = el.get_Parameter(parameter).AsElementId()
    	zs_el = doc.GetElement(zs_id)
    	if zs_el is None:
    		zs_id = el.get_Parameter(BuiltInParameter.CLEAR_COVER_OTHER).AsElementId()
    		zs_el = doc.GetElement(zs_id)
    	zs = zs_el.CoverDistance
    	return zs
    def get_pars_column(el):
    	val_hight = el.get_Parameter(BuiltInParameter.INSTANCE_LENGTH_PARAM).AsDouble()
    	type = get_type(el)
    	val_length = type.LookupParameter(par_length).AsDouble()
    	val_width = type.LookupParameter(par_width).AsDouble()
    	return val_hight,val_length,val_width
    def get_type(el):
    	type_id = el.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM).AsElementId()
    	type = doc.GetElement(type_id)
    	return type
    def vert_bar(pt1,h,zs_top,zs_bottom,a):
    	x2 = pt1.X
    	y2 = pt1.Y
    	z2 = pt1.Z+h
    	ln1=[]
        pt1 = XYZ(pt1.X,pt1.Y,pt1.Z)
        if gn_bool:
            pt2 = XYZ(x2,y2,z2-400/304.8)
            pt2_1 = get_new_point(x2,y2,z2-400/304.8, 50/304.8, 0, a)
            pt3 = XYZ(pt2_1.X, pt2_1.Y, pt2_1.Z+100/304.8)
            pt4 = XYZ(pt2_1.X, pt2_1.Y, z2)
            ln1 = [pt1,pt2, pt3, pt4]
        else:
            pt2 = XYZ(x2,y2,z2)
            ln1 = [pt1, pt2]
    	ln=get_lines2(ln1)
    	return ln
    def to4pt(pt1,w,l,a,b,k): #(Центральная точка, Ширина, Длина, Угол поворота, Защитный слой), Переместить все точки по Z
    	x1 = pt1.X
    	y1 = pt1.Y
    	z1 = k
    	pt2 = get_new_point(x1,y1,z1,-w/2+b,-l/2+b,a)
    	pt3 = get_new_point(x1,y1,z1,-w/2+b,l/2-b,a)
    	pt4 = get_new_point(x1,y1,z1,w/2-b,l/2-b,a)
    	pt5 = get_new_point(x1,y1,z1,w/2-b,-l/2+b,a)
    	return pt2,pt3,pt4,pt5
    def get_new_point(x1,y1,z1,fx,fy,a):
    	x2 = x1+(fx)*math.cos(math.radians(a))-(fy)*math.sin(math.radians(a))
    	y2 = y1+(fx)*math.sin(math.radians(a))+(fy)*math.cos(math.radians(a))
    	pt2 = XYZ(x2,y2,z1)
    	return pt2
    def get_angle(a):  #кут між осями документа та вектором
    	x1 = a.X
    	y1 = a.Y
    	angle = a.Normalize().AngleOnPlaneTo(XYZ.BasisX, XYZ.BasisZ)
    	return 90-math.degrees(angle)
    def get_lines(stirrup_pts):
        list=[]
        i=0
        for pt in stirrup_pts:
        	if i==0:
        		pt1=pt
        		pt3=pt
        	else:
        		list.append(Line.CreateBound(pt1,pt))
        		pt1=pt
        	i=i+1
        list.append(Line.CreateBound(pt1,pt3))
        return list
    def get_lines2(stirrup_pts): #створюю лінії між заданими точками отримуючи контур
    	list=[]
    	i=0

    	for pt in stirrup_pts:
    		if i==0:
    			pt1=pt
    			pt3=pt
    		else:
    			list.append(Line.CreateBound(pt1,pt))
    			pt1=pt
    		i=i+1
    	list.append(Line.CreateBound(pt1,pt3))
    	list.pop(-1)
    	return list

    def rebar_delete(el, rebars):
        rebars
        list0=[]
        name = el.GetType().Name
        if name!="Rebar":
            list0.append(el.Id)
        #---Основной код----------------
        list1 = List[ElementId]()
        for rebar in rebars:
            try:
                el_id = rebar.GetHostId()
            except:
                el_id = None
            for id in list0:
                if id==el_id:
        			list1.Add(rebar.Id)
        if len(list1)>=1:
            rebars = uidoc.Selection.SetElementIds(list1)
            for rebar_id in list1:
                doc.Delete(rebar_id)

    def SignedDistanceTo(p, plane):
        v = p - plane.Origin
        return plane.Normal.DotProduct(v)
    def ProjectOnto(plane, p):
        d = SignedDistanceTo(p, plane)
        q = p - d*plane.Normal
        return q
    def new_point_1(point, vect_X, vect_Y, dist_X, dist_Y):
        new_point = point +dist_X*vect_X + dist_Y*vect_Y
        return new_point
    #----ОСНОВНОЙ КОД-----

    for col in columns:

        col_type = doc.GetElement(col.GetTypeId())
        width = col_type.LookupParameter(par_width).AsDouble()
        height = col_type.LookupParameter(par_height).AsDouble()
        curve = col.Location.Curve
        #angle = get_angle(p2-p1)
        bb_box = col.get_BoundingBox(curview)
        bb_cent = (bb_box.Max+bb_box.Min)/2
        normal_X = col.GetTransform().BasisX #знаходжу нормалі балки
        normal_Y =  col.GetTransform().BasisY
        normal_Z = col.GetTransform().BasisZ
        p1 = curve.GetEndPoint(0)+float(left_offset)/304.8*normal_X
        p2 = curve.GetEndPoint(1)-float(right_offset)/304.8*normal_X
        length = p1.DistanceTo(p2)
        #width = col.GetHostGeometry().width
        pp1 = p1+1*normal_Z
        pp2 = p1+1*normal_Y

        pp3 = p2+1*normal_Z
        pp4 = p2+1*normal_Y
        plane = Plane.CreateByThreePoints(p1, pp1, pp2) #площини по кінцям балки
        plane_2 = Plane.CreateByThreePoints(p2, pp3, pp4)
        #print(plane)
        pz0_1 = ProjectOnto(plane, bb_cent)#серединні точки по кінцям балки
        pz0_2 = ProjectOnto(plane_2, bb_cent)
        #print(p0_1)

        p0_1 = new_point_1(pz0_1, normal_Y, normal_Z, -width/2,height/2) #контур початку балки
        p0_2 = new_point_1(pz0_1, normal_Y, normal_Z, width/2,height/2)
        p0_3 = new_point_1(pz0_1, normal_Y, normal_Z, width/2,-height/2)
        p0_4 = new_point_1(pz0_1, normal_Y, normal_Z, -width/2,-height/2)

        p0_5 = new_point_1(pz0_2, normal_Y, normal_Z, -width/2,height/2) #контур кінця балки
        p0_6 = new_point_1(pz0_2, normal_Y, normal_Z, width/2,height/2)
        p0_7 = new_point_1(pz0_2, normal_Y, normal_Z, width/2,-height/2)
        p0_8 = new_point_1(pz0_2, normal_Y, normal_Z, -width/2,-height/2)

        v_r_1 = new_point_1(p0_1, normal_Y, normal_Z, cover_1+v_d1/2, -cover_2 - v_d1/2)
        v_r_2 = new_point_1(p0_2, normal_Y, normal_Z, -cover_3-v_d1/2, -cover_2 - v_d1/2)
        v_r_3 = new_point_1(p0_3, normal_Y, normal_Z, -cover_3-v_d6/2, cover_4 + v_d6/2)
        v_r_4 = new_point_1(p0_4, normal_Y, normal_Z, cover_1+v_d6/2, cover_4 + v_d6/2)

        v_r_5 = v_r_1+length*normal_X
        v_r_6 = v_r_2+length*normal_X
        v_r_7 = v_r_3+length*normal_X
        v_r_8 = v_r_4+length*normal_X
        t=Transaction(doc, 'Arm kolona')
        t.Start()
        rebar_delete(col, rebars)
        rebar_list=[]
        def create_r(pt1, pt2, rebar_type, rebar_step, rebar_count, vert_b):

            if rebar_step[0]=='0' or rebar_vect_1 == 0: #кількість з рівномірним кроком

                m = pt1.DistanceTo(pt2)
                l_step = m/(rebar_count-1)
                vert_b = []
                for h in range(rebar_count):
                    vert_b.append(str(l_step*304.8))
                vert_b = step_vert(vert_b, rebar_count)

            step_next = 0
            for h in vert_b:
                list = h.split('*')
                step = float(list[0])/304.8
                count = float(list[1])
                step_0 = step_next#step+step_next
                step_p = step*count
                step_next += step + step*(count-1)
                pb1_0 = new_point_1(pt1, normal_Y, normal_Z, step_0, 0)
                pb1_1 = pb1_0+length*normal_X#new_point_1(pt1, normal_Y, normal_Z, step_0, 0)
                lines_pts_1 = get_lines2([pb1_0, pb1_1])

                norm_gn1 = normal_Y
                rebar_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, rebar_type, hook_type_vert, hook_type_vert, col , norm_gn1, lines_pts_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)
                rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
                rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(count)
                rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(step)
                rebar_1.GetShapeDrivenAccessor().BarsOnNormalSide = True
                rebar_list.append(rebar_1)
                #plane_m = Plane.CreateByNormalAndOrigin(pt_02-pt_01, col.Location.Point)
                #rebar_2 = ElementTransformUtils.MirrorElement(doc, rebar_1.Id, plane_m)
        r1 = create_r(v_r_1, v_r_2, vert_rebar_1, b_rebar_1_step, b_rebar_1_count,vert_b_1)#перший верхній ряд
        if b_rebar_1_count != 0 or b_rebar_1_count != None: #другий верхній ряд
            if rebar_lines_step_1 != 0 and rebar_lines_step_1 != None:
                v_r_1_2 = new_point_1(p0_1, normal_Y, normal_Z, cover_1+v_d2/2, -cover_2 - v_d2/2) - int(rebar_lines_step_1)/304.8*normal_Z
                v_r_2_2 = new_point_1(p0_2, normal_Y, normal_Z, -cover_3-v_d2/2, -cover_2 - v_d2/2) - int(rebar_lines_step_1)/304.8*normal_Z
                r2 = create_r(v_r_1_2, v_r_2_2, vert_rebar_2, b_rebar_1_step, b_rebar_2_count, vert_b_2)
                if b_rebar_2_count != 0 or b_rebar_2_count != None: #третій верхній ряд
                    v_r_3_2 = new_point_1(p0_1, normal_Y, normal_Z, cover_1+v_d3/2, -cover_2 - v_d3/2) - int(rebar_lines_step_1)/304.8*normal_Z - int(rebar_lines_step_2)/304.8*normal_Z
                    v_r_4_1 = new_point_1(p0_2, normal_Y, normal_Z, -cover_3-v_d3/2, -cover_2 - v_d3/2) - int(rebar_lines_step_1)/304.8*normal_Z - int(rebar_lines_step_2)/304.8*normal_Z
                    r3 = create_r(v_r_3_2, v_r_4_1, vert_rebar_3, b_rebar_1_step, b_rebar_3_count,vert_b_3)

        v_r_1_5 = new_point_1(p0_4, normal_Y, normal_Z, cover_1+v_d4/2, cover_4 + v_d4/2)
        v_r_1_6 = new_point_1(p0_3, normal_Y, normal_Z, -cover_3-v_d4/2, cover_4 + v_d4/2)
        r4 = create_r(v_r_1_5, v_r_1_6, vert_rebar_4, b_rebar_2_step, b_rebar_4_count,vert_b_4) #перший нижній ряд
        if b_rebar_4_count != 0 or b_rebar_4_count != None:
            if rebar_lines_step_4 != 0 and rebar_lines_step_4 != None:
                v_r_1_7 = new_point_1(p0_4, normal_Y, normal_Z, cover_1+v_d5/2, cover_4 + v_d5/2) + int(rebar_lines_step_4)/304.8*normal_Z
                v_r_1_8 = new_point_1(p0_3, normal_Y, normal_Z, -cover_3-v_d5/2, cover_4 + v_d5/2) + int(rebar_lines_step_4)/304.8*normal_Z
                r2 = create_r(v_r_1_7, v_r_1_8, vert_rebar_5, b_rebar_2_step, b_rebar_5_count, vert_b_5)
                if b_rebar_2_count != 0 or b_rebar_2_count != None:
                    v_r_1_8 = new_point_1(p0_4, normal_Y, normal_Z, cover_1+v_d6/2, cover_4 + v_d6/2) + int(rebar_lines_step_4)/304.8*normal_Z + int(rebar_lines_step_3)/304.8*normal_Z
                    v_r_1_9 = new_point_1(p0_3, normal_Y, normal_Z, -cover_3-v_d6/2, cover_4 + v_d6/2) + int(rebar_lines_step_4)/304.8*normal_Z + int(rebar_lines_step_3)/304.8*normal_Z
                    r3 = create_r(v_r_1_8, v_r_1_9, vert_rebar_6, b_rebar_2_step, b_rebar_6_count,vert_b_6)
        #------------------------ХОМУТИ----------------------------------------
        hom_cont_1 = new_point_1(p0_1, normal_Y, normal_Z, cover_1-g_d1, -cover_2+g_d1/2)+g_left_offset*normal_X
        hom_cont_2 = new_point_1(p0_2, normal_Y, normal_Z, -cover_3, -cover_2+g_d1/2)+g_left_offset*normal_X
        hom_cont_3 = new_point_1(p0_3, normal_Y, normal_Z, -cover_3, cover_4-g_d1)+g_left_offset*normal_X
        hom_cont_4 = new_point_1(p0_4, normal_Y, normal_Z, cover_1-g_d1, cover_4-g_d1)+g_left_offset*normal_X
        lines_pts_hom_1 = get_lines([hom_cont_1, hom_cont_2, hom_cont_3, hom_cont_4])

        hom_cont_5 = new_point_1(p0_5, normal_Y, normal_Z, cover_1-g_d1, -cover_2+g_d1/2)-g_right_offset*normal_X
        hom_cont_6 = new_point_1(p0_6, normal_Y, normal_Z, -cover_3, -cover_2+g_d1/2)-g_right_offset*normal_X
        hom_cont_7 =  new_point_1(p0_7, normal_Y, normal_Z, -cover_3, cover_4-g_d1)-g_right_offset*normal_X
        hom_cont_8 = new_point_1(p0_8, normal_Y, normal_Z, cover_1-g_d1, cover_4-g_d1)-g_right_offset*normal_X
        lines_pts_hom_2 = get_lines([hom_cont_5, hom_cont_6, hom_cont_7, hom_cont_8])

        h_m_b = (g_rebar_1_count-1) * g_rebar_1_step
        h_m_t = (g_rebar_5_count-1) * g_rebar_5_step
        h_m_leng = hom_cont_1.DistanceTo(hom_cont_5)- h_m_b - h_m_t
        count = h_m_leng // g_rebar_3_step -1
        if h_m_leng - g_rebar_3_step * count < g_rebar_3_step:
            count-=1
        h_last = (h_m_leng - g_rebar_3_step * count)/2
        hom_m_off = h_m_b + h_last
        hom_m_count = count+1
        #print([hom_m_off*304.8, h_m_b*304, h_m_t*304, h_m_leng*304, count, h_last*304])

        hom_cont_9 = hom_cont_1+hom_m_off*normal_X
        hom_cont_10 = hom_cont_2+hom_m_off*normal_X
        hom_cont_11 = hom_cont_3+hom_m_off*normal_X
        hom_cont_12 = hom_cont_4+hom_m_off*normal_X
        lines_pts_hom_3 = get_lines([hom_cont_9, hom_cont_10, hom_cont_11, hom_cont_12])

        norm2 = normal_X
        #rebar_hom_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, gor_rebar_1, hook_s, hook_s, col ,norm2, lines_pts_hom_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right,True,True)
        #for i in lines_pts_hom_1:
        #    rebar_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, gor_rebar_1, hook_type_vert, hook_type_vert, col , norm2, [i], RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)

        #print(shape_s)
    	rebar_hom_1 = RS.Rebar.CreateFromCurvesAndShape(doc, shape_s, gor_rebar_1, hook_s,hook_s, col, norm2, lines_pts_hom_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right)
        #rebar_list.append(rebar_hom_1)
    	rebar_hom_1.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
    	rebar_hom_1.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(g_rebar_1_count)
    	rebar_hom_1.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(g_rebar_1_step)
    	rebar_hom_1.GetShapeDrivenAccessor().BarsOnNormalSide = True

    	rebar_hom_2 = RS.Rebar.CreateFromCurvesAndShape(doc, shape_s, gor_rebar_5, hook_s,hook_s, col, norm2, lines_pts_hom_2, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right)
        rebar_list.append(rebar_hom_2)
    	rebar_hom_2.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
    	rebar_hom_2.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(g_rebar_5_count)
    	rebar_hom_2.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(g_rebar_5_step)
    	rebar_hom_2.GetShapeDrivenAccessor().BarsOnNormalSide = False

    	rebar_hom_3 = RS.Rebar.CreateFromCurvesAndShape(doc, shape_s, gor_rebar_3, hook_s,hook_s, col, norm2, lines_pts_hom_3, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right)
        rebar_list.append(rebar_hom_3)
    	rebar_hom_3.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
    	rebar_hom_3.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(hom_m_count)
    	rebar_hom_3.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(g_rebar_3_step)
    	rebar_hom_3.GetShapeDrivenAccessor().BarsOnNormalSide = True



        #print(lines_pts_hom_1)
        r = Autodesk.Revit.DB.Structure.RebarHostData.GetRebarHostData(col).GetRebarsInHost()

        ids=[]
        for i in r:
            ids.append(i.Id)
        ids_list = List[ElementId](ids)
        group = doc.Create.NewGroup(ids_list)
        #group.GroupType.Name = 'Б1'
        try:
            for i in r:
                if hasattr(i, "SetSolidInView"):
                    i.SetSolidInView(curview, True)
        except:
            0


        t.Commit()
        """BotLevel = col.get_Parameter(BuiltInParameter.FAMILY_BASE_LEVEL_PARAM)
        base_offset = col.get_Parameter(BuiltInParameter.FAMILY_BASE_LEVEL_OFFSET_PARAM).AsDouble()
        bip = BotLevel.AsElementId()
        bot = doc.GetElement( bip )
        b_value = bot.ProjectElevation
        pars = get_pars_column(col)
        val_hight = pars[0]
        val_length = pars[1]
        val_width = pars[2]
        pt_0 = col.Location.Point
        angle = get_angle(col.HandOrientation)
        #Базові точки по контуру колони--------
        pt_01 = get_new_point(pt_0.X, pt_0.Y, b_value+base_offset, -val_width/2, val_length/2, angle)
        pt_02 = get_new_point(pt_0.X, pt_0.Y, b_value+base_offset, val_width/2, val_length/2, angle)
        pt_03 = get_new_point(pt_0.X, pt_0.Y, b_value+base_offset, val_width/2, -val_length/2, angle)
        pt_04 = get_new_point(pt_0.X, pt_0.Y, b_value+base_offset, -val_width/2, -val_length/2, angle)

        pt_05 =  get_new_point(pt_01.X, pt_01.Y, pt_01.Z+val_hight, 0, 0, angle)
        pt_06 =  get_new_point(pt_02.X, pt_02.Y, pt_02.Z+val_hight, 0, 0, angle)
        pt_07 =  get_new_point(pt_03.X, pt_03.Y, pt_03.Z+val_hight, 0, 0, angle)
        pt_08 =  get_new_point(pt_04.X, pt_04.Y, pt_04.Z+val_hight, 0, 0, angle)
        #----------------------------------
        v_r_1_b = get_new_point(pt_01.X, pt_01.Y, pt_01.Z, cover_4+v_d1/2, -(cover_1+v_d1/2), angle)
        v_r_1_t = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight, 0, 0, angle)
        #print([cover_4*304.8, cover_1*304.8, v_d1*304.8])
        v_r_2_b = get_new_point(pt_02.X, pt_02.Y, pt_02.Z, -(cover_2+v_d2/2), -(cover_1+v_d2/2), angle)
        v_r_2_t = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z+val_hight, 0, 0, angle)
        #print([cover_2*304.8, cover_1*304.8, v_d2*304.8])
        v_r_3_b = get_new_point(pt_03.X, pt_03.Y, pt_03.Z, -(cover_2+v_d3/2), (cover_3+v_d3/2), angle)
        v_r_3_t = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z+val_hight, 0, 0, angle)

        v_r_4_b = get_new_point(pt_04.X, pt_04.Y, pt_04.Z, (cover_4+v_d4/2), (cover_3+v_d4/2), angle)
        v_r_4_t = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z+val_hight, 0, 0, angle)

        if rebar_vect == 0:
            p_offset = gn_5*math.cos(math.radians(45))
            p_offset2 = bot_of_g_1*math.cos(math.radians(45))
            p1_0 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_1, -p_offset2, p_offset2, angle)
            p1_1 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_1, 0, 0, angle)
            p1_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight - gn_2, 0, 0, angle)
            p1_3 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight + gn_1, p_offset, -p_offset, angle)
            p1_4 = get_new_point(p1_3.X, p1_3.Y,  v_r_1_b.Z+val_hight+top_of_1, 0, 0, angle)

            p2_0 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z-bot_of_1, p_offset2, p_offset2, angle)
            p2_1 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z-bot_of_1, 0, 0, angle)
            p2_2 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z+val_hight - gn_2, 0, 0, angle)
            p2_3 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z+val_hight + gn_1, -p_offset, -p_offset, angle)
            p2_4 = get_new_point(p2_3.X, p2_3.Y,  v_r_2_b.Z+val_hight+top_of_1, 0, 0, angle)

            p3_0 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z-bot_of_1, p_offset2, -p_offset2, angle)
            p3_1 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z-bot_of_1, 0, 0, angle)
            p3_2 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z+val_hight - gn_2, 0, 0, angle)
            p3_3 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z+val_hight + gn_1, -p_offset, p_offset, angle)
            p3_4 = get_new_point(p3_3.X, p3_3.Y, v_r_3_b.Z+val_hight+top_of_1, 0, 0, angle)

            p4_0 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z-bot_of_1, -p_offset2, -p_offset2, angle)
            p4_1 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z-bot_of_1, 0, 0, angle)
            p4_2 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z+val_hight - gn_2, 0, 0, angle)
            p4_3 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z+val_hight + gn_1, p_offset, p_offset, angle)
            p4_4 = get_new_point(p4_3.X, p4_3.Y, v_r_4_b.Z+val_hight+top_of_1, 0, 0, angle)





            if bot_of_g_1 != 0 and bot_of_g_1 != None:
                lines_pts_1 = get_lines2([p1_0, p1_1, p1_2, p1_3, p1_4])
                lines_pts_2 = get_lines2([p2_0, p2_1, p2_2, p2_3, p2_4])
                lines_pts_3 = get_lines2([p3_0, p3_1, p3_2, p3_3, p3_4])
                lines_pts_4 = get_lines2([p4_0, p4_1, p4_2, p4_3, p4_4])
            else:
                lines_pts_1 = get_lines2([p1_1, p1_2, p1_3, p1_4])
                lines_pts_2 = get_lines2([p2_1, p2_2, p2_3, p2_4])
                lines_pts_3 = get_lines2([p3_1, p3_2, p3_3, p3_4])
                lines_pts_4 = get_lines2([p4_1, p4_2, p4_3, p4_4])
            norm0 = pt_02-pt_01#col.FacingOrientation#XYZ(0,-1,0)
            norm1 = p1_3-p1_2 #вектор до повернутих
            norm2 = p2_3-p2_2
            norm_gn1 = norm1.CrossProduct(XYZ.BasisZ).Normalize() #нормаль до повернутих
            norm_gn2 = norm2.CrossProduct(XYZ.BasisZ).Normalize()
        elif rebar_vect == 1 or rebar_vect == 2:
            if rebar_vect ==1:
                p_offset_x = bot_of_g_1
                p_offset2_x = top_of_g_1
                p_offset_y = 0
                p_offset2_y = 0
            else:
                p_offset_x = 0
                p_offset2_x = 0
                p_offset_y = bot_of_g_1
                p_offset2_y = top_of_g_1
            p_offset2 = bot_of_g_1
            p1_0 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_1, -p_offset_x, p_offset_y, angle)
            p1_1 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_1, 0, 0, angle)
            p1_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y,  v_r_1_b.Z+val_hight+top_of_1, 0, 0, angle)
            p1_3 = get_new_point(v_r_1_b.X, v_r_1_b.Y,  v_r_1_b.Z+val_hight+top_of_1, -p_offset2_x, p_offset2_y, angle)
            p2_0 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z-bot_of_1, p_offset_x, p_offset_y, angle)
            p2_1 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z-bot_of_1, 0, 0, angle)
            p2_2 = get_new_point(v_r_2_b.X, v_r_2_b.Y,  v_r_2_b.Z+val_hight+top_of_1, 0, 0, angle)
            p2_3 = get_new_point(v_r_2_b.X, v_r_2_b.Y,  v_r_2_b.Z+val_hight+top_of_1, p_offset2_x, p_offset2_y, angle)

            p3_0 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z-bot_of_1, p_offset_x, -p_offset_y, angle)
            p3_1 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z-bot_of_1, 0, 0, angle)
            p3_2 = get_new_point(v_r_3_b.X, v_r_3_b.Y,  v_r_3_b.Z+val_hight+top_of_1, 0, 0, angle)
            p3_3 = get_new_point(v_r_3_b.X, v_r_3_b.Y,  v_r_3_b.Z+val_hight+top_of_1, p_offset2_x, -p_offset2_y, angle)

            p4_0 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z-bot_of_1, -p_offset_x, -p_offset_y, angle)
            p4_1 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z-bot_of_1, 0, 0, angle)
            p4_2 = get_new_point(v_r_4_b.X, v_r_4_b.Y,  v_r_4_b.Z+val_hight+top_of_1, 0, 0, angle)
            p4_3 = get_new_point(v_r_4_b.X, v_r_4_b.Y,  v_r_4_b.Z+val_hight+top_of_1, -p_offset2_x, -p_offset2_y, angle)
            if (bot_of_g_1 == 0 or bot_of_g_1 == None) and top_of_g_1 > 0:
                lines_pts_1 = get_lines2([p1_1, p1_2, p1_3])
                lines_pts_2 = get_lines2([p2_1, p2_2, p2_3])
                lines_pts_3 = get_lines2([p3_1, p3_2, p3_3])
                lines_pts_4 = get_lines2([p4_1, p4_2, p4_3])
            elif (top_of_g_1 == 0 or top_of_g_1 == None) and bot_of_g_1 > 0:
                lines_pts_1 = get_lines2([p1_0, p1_1, p1_2])
                lines_pts_2 = get_lines2([p2_0, p2_1, p2_2])
                lines_pts_3 = get_lines2([p3_0, p3_1, p3_2])
                lines_pts_4 = get_lines2([p4_0, p4_1, p4_2])
            elif top_of_g_1 == 0 and bot_of_g_1 == 0:
                lines_pts_1 = get_lines2([p1_1, p1_2])
                lines_pts_2 = get_lines2([p2_1, p2_2])
                lines_pts_3 = get_lines2([p3_1, p3_2])
                lines_pts_4 = get_lines2([p4_1, p4_2])
            else:
                lines_pts_1 = get_lines2([p1_0, p1_1, p1_2, p1_3])
                lines_pts_2 = get_lines2([p2_0, p2_1, p2_2, p2_3])
                lines_pts_3 = get_lines2([p3_0, p3_1, p3_2, p3_3])
                lines_pts_4 = get_lines2([p4_0, p4_1, p4_2, p4_3])

            if rebar_vect ==2:
                norm_gn1 = col.FacingOrientation #нормаль до повернутих
                norm_gn2 = col.FacingOrientation
            else:
                norm_gn1 = col.HandOrientation #нормаль до повернутих
                norm_gn2 = col.HandOrientation

        hom_cont_1 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+hom_b_off, -v_d1/2-g_d1, v_d1/2+g_d1/2, angle)
        hom_cont_2 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z+hom_b_off, v_d2/2, v_d2/2+g_d1/2, angle)
        hom_cont_3 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z+hom_b_off, v_d3/2, -v_d3/2-g_d1, angle)
        hom_cont_4 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z+hom_b_off, -v_d4/2-g_d1, -v_d4/2-g_d1, angle)
        lines_pts_hom_1 = get_lines([hom_cont_1, hom_cont_2, hom_cont_3, hom_cont_4])

        hom_cont_5 = get_new_point(v_r_1_t.X, v_r_1_t.Y, v_r_1_t.Z-hom_t_off, -v_d1/2-g_d1, v_d1/2+g_d1/2, angle)
        hom_cont_6 = get_new_point(v_r_2_t.X, v_r_2_t.Y, v_r_2_t.Z-hom_t_off, v_d2/2, v_d2/2+g_d1/2, angle)
        hom_cont_7 = get_new_point(v_r_3_t.X, v_r_3_t.Y, v_r_3_t.Z-hom_t_off, v_d3/2, -v_d3/2-g_d1, angle)
        hom_cont_8 = get_new_point(v_r_4_t.X, v_r_4_t.Y, v_r_4_t.Z-hom_t_off, -v_d4/2-g_d1, -v_d4/2-g_d1, angle)
        lines_pts_hom_2 = get_lines([hom_cont_5, hom_cont_6, hom_cont_7, hom_cont_8])

        h_m_b = hom_b_off + (hom_b_count-1) * hom_b_spc
        h_m_t = hom_t_off + (hom_t_count-1) * hom_t_spc
        h_m_leng = val_hight - h_m_b - h_m_t
        count = h_m_leng // hom_m_spc -1
        if h_m_leng - hom_m_spc * count < hom_m_spc:
            count-=1
        h_last = (h_m_leng - hom_m_spc * count)/2
        hom_m_off = h_m_b + h_last
        hom_m_count = count+1
        #print([hom_m_off*304.8, h_m_b*304, h_m_t*304, h_m_leng*304, count, h_last*304])

        hom_cont_9 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+hom_m_off, -v_d1/2-g_d1, v_d1/2+g_d1/2, angle)
        hom_cont_10 = get_new_point(v_r_2_b.X, v_r_2_b.Y, v_r_2_b.Z+hom_m_off, v_d2/2, v_d2/2+g_d1/2, angle)
        hom_cont_11 = get_new_point(v_r_3_b.X, v_r_3_b.Y, v_r_3_b.Z+hom_m_off, v_d3/2, -v_d3/2-g_d1, angle)
        hom_cont_12 = get_new_point(v_r_4_b.X, v_r_4_b.Y, v_r_4_b.Z+hom_m_off, -v_d4/2-g_d1, -v_d4/2-g_d1, angle)
        lines_pts_hom_3 = get_lines([hom_cont_9, hom_cont_10, hom_cont_11, hom_cont_12])
        #print(lines_pts_hom_1)

        t=Transaction(doc, 'Arm kolona')
        t.Start()
        rebar_delete(col, rebars)
        rebar_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, vert_rebar_1, hook_type_vert, hook_type_vert, col ,norm_gn1, lines_pts_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)
        rebar_2 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, vert_rebar_2, hook_type_vert, hook_type_vert, col ,norm_gn2, lines_pts_2, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)
        rebar_3 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, vert_rebar_3, hook_type_vert, hook_type_vert, col ,norm_gn1, lines_pts_3, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)
        rebar_4 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, vert_rebar_4, hook_type_vert, hook_type_vert, col ,norm_gn2, lines_pts_4, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)

        rebar_list = [rebar_1, rebar_2, rebar_3, rebar_4]
        norm2 = XYZ(0,0,1)
        #rebar_hom_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, gor_rebar_1, hook_s, hook_s, col ,norm2, lines_pts_hom_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right,True,True)

    	rebar_hom_1 = RS.Rebar.CreateFromCurvesAndShape(doc, shape_s, gor_rebar_1, hook_s,hook_s, col, norm2, lines_pts_hom_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right)
        rebar_list.append(rebar_hom_1)
    	rebar_hom_1.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
    	rebar_hom_1.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(hom_b_count)
    	rebar_hom_1.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(hom_b_spc)
    	rebar_hom_1.GetShapeDrivenAccessor().BarsOnNormalSide = True

    	rebar_hom_2 = RS.Rebar.CreateFromCurvesAndShape(doc, shape_s, gor_rebar_1, hook_s,hook_s, col, norm2, lines_pts_hom_2, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right)
        rebar_list.append(rebar_hom_2)
    	rebar_hom_2.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
    	rebar_hom_2.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(hom_t_count)
    	rebar_hom_2.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(hom_t_spc)
    	rebar_hom_2.GetShapeDrivenAccessor().BarsOnNormalSide = False

    	rebar_hom_3 = RS.Rebar.CreateFromCurvesAndShape(doc, shape_s, gor_rebar_1, hook_s,hook_s, col, norm2, lines_pts_hom_3, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Right)
        rebar_list.append(rebar_hom_3)
    	rebar_hom_3.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
    	rebar_hom_3.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(hom_m_count)
    	rebar_hom_3.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(hom_m_spc)
    	rebar_hom_3.GetShapeDrivenAccessor().BarsOnNormalSide = True

        p_offset = gn_6
        p_offset2 = bot_of_g_2
        p_offset3 = top_of_g_2
        step_next=0
        #print(rebar_b1_vect)
        #---------------------------БОКОВІ СТРИЖНІ 1--------------------------
        if b_rebar_1_step[0]=='0': #кількість з рівномірним кроком
            m = v_r_1_b.DistanceTo(v_r_4_b)
            l_step = m/(b_rebar_1_count+1)
            vert_b_1 = []
            for h in range(b_rebar_1_count):
                vert_b_1.append(str(l_step*304.8))
            vert_b_1 = step_vert(vert_b_1, b_rebar_1_count)
        elif b_rebar_1_step[0]!='0' and len(b_rebar_1_step)==1 and rebar_b1_vect==0: #рівномрно з кроком
            m = v_r_1_b.DistanceTo(v_r_4_b)
            l_count = m//(int(b_rebar_1_step[0])/304.8)
            l_last = (m - l_count*(int(b_rebar_1_step[0])/304.8))/2
            b_rebar_1_count = int(l_count+1)
            if l_last < (int(b_rebar_1_step[0])/304.8)/2:
                l_last = (m - (l_count-1)*(int(b_rebar_1_step[0])/304.8))/2
                b_rebar_1_count = int(l_count)
            vert_b_1 = []
            vert_b_1.append(str(l_last*304.8))
            for h in range(int(l_count)):
                vert_b_1.append(str(b_rebar_1_step[0]))
            vert_b_1 = step_vert(vert_b_1, b_rebar_1_count)
        for h in vert_b_1:
            list = h.split('*')
            step = float(list[0])/304.8
            count = float(list[1])
            step_0 = step+step_next
            step_p = step*count
            step_next += step + step*(count-1)
            pb1_0 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_2, -p_offset2, -step_0, angle)
            pb1_1 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_2, 0, -step_0, angle)
            pb1_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight - gn_2, 0, -step_0, angle)

            pb1_2_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y,  v_r_1_b.Z+val_hight+top_of_2, 0, -step_0, angle)

            pb1_3 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight + gn_1, p_offset, -step_0, angle)

            pb1_3_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y,  v_r_1_b.Z+val_hight+top_of_2, -p_offset3, -step_0, angle)
            pb1_4 = get_new_point(pb1_3.X, pb1_3.Y,  v_r_1_b.Z+val_hight+top_of_2, 0, 0, angle)

            if rebar_vect == 0:
                if bot_of_g_2 != 0 and bot_of_g_2 != None:
                    lines_pts_1 = get_lines2([pb1_0, pb1_1, pb1_2, pb1_3, pb1_4])

                else:
                    lines_pts_1 = get_lines2([pb1_1, pb1_2, pb1_3, pb1_4])
            else:
                if (bot_of_g_2 == 0 or bot_of_g_2 == None) and top_of_g_2 > 0:
                    lines_pts_1 = get_lines2([pb1_1, pb1_2_2, pb1_3_2])

                elif (top_of_g_2 == 0 or top_of_g_2 == None) and bot_of_g_2 > 0:
                    lines_pts_1 = get_lines2([pb1_0, pb1_1, pb1_2_2])
                elif top_of_g_2 == 0 and bot_of_g_2 == 0:
                    lines_pts_1 = get_lines2([pb1_1, pb1_2_2])
                else:
                    lines_pts_1 = get_lines2([pb1_0, pb1_1, pb1_2_2, pb1_3_2])
            norm_gn1 = col.HandOrientation
            rebar_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, vert_b_rebar_1, hook_type_vert, hook_type_vert, col ,norm_gn1, lines_pts_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)
            rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
            rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(count)
            rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(step)
            rebar_1.GetShapeDrivenAccessor().BarsOnNormalSide = True
            rebar_list.append(rebar_1)
            plane_m = Plane.CreateByNormalAndOrigin(pt_02-pt_01, col.Location.Point)
            rebar_2 = ElementTransformUtils.MirrorElement(doc, rebar_1.Id, plane_m)
        #---------------------------БОКОВІ СТРИЖНІ 1_2--------------------------
        p_offset = gn_6
        p_offset2 = bot_of_g_2
        p_offset3 = top_of_g_2
        step_next=0

        if b_rebar_1_2_step[0]=='0': #кількість з рівномірним кроком
            m = v_r_1_b.DistanceTo(v_r_2_b)
            l_step = m/(b_rebar_1_2_count+1)
            vert_b_1_2 = []
            for h in range(b_rebar_1_2_count):
                vert_b_1_2.append(str(l_step*304.8))
            vert_b_1_2 = step_vert(vert_b_1_2, b_rebar_1_2_count)
        elif b_rebar_1_2_step[0]!='0' and len(b_rebar_1_2_step)==1 and rebar_b2_vect==0: #рівномрно з кроком
            m = v_r_1_b.DistanceTo(v_r_2_b)
            l_count = m//(int(b_rebar_1_2_step[0])/304.8)
            l_last = (m - l_count*(int(b_rebar_1_2_step[0])/304.8))/2
            b_rebar_1_2_count = int(l_count+1)
            if l_last < (int(b_rebar_1_2_step[0])/304.8)/2:
                l_last = (m - (l_count-1)*(int(b_rebar_1_2_step[0])/304.8))/2
                b_rebar_1_2_count = int(l_count)
            vert_b_1_2 = []
            vert_b_1_2.append(str(l_last*304.8))
            for h in range(int(l_count)):
                vert_b_1_2.append(str(b_rebar_1_2_step[0]))
            vert_b_1_2 = step_vert(vert_b_1_2, b_rebar_1_2_count)
        for h in vert_b_1_2:
            list = h.split('*')
            step = float(list[0])/304.8
            count = float(list[1])
            step_0 = step+step_next
            step_p = step*count
            step_next += step + step*(count-1)
            pb1_0 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_2, step_0, p_offset2,  angle)
            pb1_1 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z-bot_of_2, step_0, 0,  angle)
            pb1_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight - gn_2, step_0, 0,  angle)

            pb1_2_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y,  v_r_1_b.Z+val_hight+top_of_2, step_0, 0,  angle)

            pb1_3 = get_new_point(v_r_1_b.X, v_r_1_b.Y, v_r_1_b.Z+val_hight + gn_1, step_0, -p_offset,  angle)

            pb1_3_2 = get_new_point(v_r_1_b.X, v_r_1_b.Y,  v_r_1_b.Z+val_hight+top_of_2, step_0, p_offset3,  angle)
            pb1_4 = get_new_point(pb1_3.X, pb1_3.Y,  v_r_1_b.Z+val_hight+top_of_2, 0, 0, angle)

            if rebar_vect == 0:
                if bot_of_g_2 != 0 and bot_of_g_2 != None:
                    lines_pts_1 = get_lines2([pb1_0, pb1_1, pb1_2, pb1_3, pb1_4])

                else:
                    lines_pts_1 = get_lines2([pb1_1, pb1_2, pb1_3, pb1_4])
            else:
                if (bot_of_g_2 == 0 or bot_of_g_2 == None) and top_of_g_2 > 0:
                    lines_pts_1 = get_lines2([pb1_1, pb1_2_2, pb1_3_2])

                elif (top_of_g_2 == 0 or top_of_g_2 == None) and bot_of_g_2 > 0:
                    lines_pts_1 = get_lines2([pb1_0, pb1_1, pb1_2_2])
                elif top_of_g_2 == 0 and bot_of_g_2 == 0:
                    lines_pts_1 = get_lines2([pb1_1, pb1_2_2])
                else:
                    lines_pts_1 = get_lines2([pb1_0, pb1_1, pb1_2_2, pb1_3_2])
            norm_gn1 = col.FacingOrientation
            rebar_1 = RS.Rebar.CreateFromCurves(doc, RS.RebarStyle.Standard, vert_b_rebar_1, hook_type_vert, hook_type_vert, col ,norm_gn1, lines_pts_1, RS.RebarHookOrientation.Right,RS.RebarHookOrientation.Left,True,True)
            rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_LAYOUT_RULE).Set(3)
            rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_QUANTITY_OF_BARS).Set(count)
            rebar_1.get_Parameter(BuiltInParameter.REBAR_ELEM_BAR_SPACING).Set(step)
            rebar_1.GetShapeDrivenAccessor().BarsOnNormalSide = True
            rebar_list.append(rebar_1)
            plane_m = Plane.CreateByNormalAndOrigin(pt_04-pt_01, col.Location.Point)
            rebar_2 = ElementTransformUtils.MirrorElement(doc, rebar_1.Id, plane_m)



        r = Autodesk.Revit.DB.Structure.RebarHostData.GetRebarHostData(col).GetRebarsInHost()


        try:
            for i in r:
                if hasattr(i, "SetSolidInView"):
                    i.SetSolidInView(curview, True)
        except:
            0

        t.Commit()"""
