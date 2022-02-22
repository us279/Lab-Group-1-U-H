import datetime
import numpy as np
from numpy import dtype
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import rate_of_increase, water_level,polyfit
from floodsystem.datafetcher import fetch_measure_levels
from scipy.misc import derivative
from sympy import poly


#Test 2G
stations = build_station_list()
station = stations[3]
def test_polyfit():
    dt = 1
    p = 4
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, p)
    assert isinstance(d0, float)
    assert isinstance(poly,np.poly1d)

    
def test_rate_of_increase():
    dt = 1
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    r_o_i = rate_of_increase(dates, levels, 1)
    if r_o_i == None:
        pass
    else:
        assert isinstance(r_o_i, float)
    
def test_water_level():
    low, mid, high= water_level()
    assert isinstance(low, list)
    assert isinstance(mid, list)
    assert isinstance(high, list)
