Desc = cellDescClass("DFFHQX1")
Desc.properties["cell_footprint"] = "dffhq"
Desc.properties["area"] = "53.222400"
Desc.properties["cell_leakage_power"] = "1876.612860"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",53.222400);
Desc.add_pin("D","input")
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
CellLib["DFFHQX1"]=Desc
