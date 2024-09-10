import gdsfactory as gf
import math
from components.PhC_2D_hex_lattice import PhC_2D_hex_lattice

@gf.cell
def PhC_wvg_hex_lattice(r: float,
                        a: float,
                        angle_resolution: float,
                        n_cols: int,
                        n_rows: int,
                        width: float,
                        wvg_type: str) -> gf.Component:
    
    component = gf.Component()
    phc = PhC_2D_hex_lattice(r, a, angle_resolution, n_cols, n_rows)
    top_half = component.add_ref(phc)

    if wvg_type == 'W1': 
        component.add_ref(phc).dmirror_y(top_half.dy-(a*math.sqrt(3)- 2*r + top_half.dysize)/2)
    elif wvg_type == 'W3':
        component.add_ref(phc).dmirror_y(top_half.dy - (a*2*math.sqrt(3) - 2*r + top_half.dysize)/2)
    else:
        component.add_ref(phc).dmirror_y(top_half.dy - (width + top_half.dysize)/2)

    return component