Desc = cellDescClass("CLKINVX3")
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "9.979200"
Desc.properties["cell_leakage_power"] = "360.740142"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX3"]=Desc
