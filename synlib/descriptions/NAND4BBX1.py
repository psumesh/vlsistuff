Desc = cellDescClass("NAND4BBX1")
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["area"] = "26.611200"
Desc.properties["cell_leakage_power"] = "1181.488194"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NAND4BBX1"]=Desc
