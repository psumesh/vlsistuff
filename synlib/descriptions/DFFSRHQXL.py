Desc = cellDescClass("DFFSRHQXL")
Desc.properties["cell_footprint"] = "dffsrhq"
Desc.properties["area"] = "79.833600"
Desc.properties["cell_leakage_power"] = "1965.000060"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",79.833600);
Desc.add_pin("D","input")
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
CellLib["DFFSRHQXL"]=Desc
