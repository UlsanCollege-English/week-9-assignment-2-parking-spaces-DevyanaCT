"""Compatibility shim for tests.

Tests expect a top-level `parking_spaces.py`. The real implementation lives in
`src/parking_spaces.py` so re-export the function here.
"""
from src.parking_spaces import min_parking_spots

__all__ = ["min_parking_spots"]

if __name__ == "__main__":
    print(min_parking_spots([(1,4),(2,5),(7,9)]))
