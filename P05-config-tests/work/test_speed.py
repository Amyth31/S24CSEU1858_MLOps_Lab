"""My own tests for minutes_per_km."""
import pytest
from orders import minutes_per_km
def test_slow_delivery():
    # 60 minutes over 6 km must give 10.0
    assert minutes_per_km(60, 6) == 10.0
def test_negative_distance_raises():
    # A distance of -3 must raise ValueError
    with pytest.raises(ValueError):
        minutes_per_km(60, -3)
