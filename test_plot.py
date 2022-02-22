from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

stations = build_station_list()
station = stations[3]
#Test 2E
def test_plot_water_level():
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    assert isinstance(dates,list)
    assert isinstance(levels,list)
#Test 2F
def test_plot_water_level_with_fit():
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    typical_low=np.linspace(station.typical_range[0],station.typical_range[0],len(dates))
    typical_high=np.linspace(station.typical_range[1],station.typical_range[1],len(dates))
    print(type(typical_low))
    assert isinstance(dates,list)
    assert isinstance(levels,list)
    assert isinstance(typical_low, np.ndarray )
    assert isinstance(typical_high, np.ndarray)
