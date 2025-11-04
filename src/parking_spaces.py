import heapq

"""
HW02 — Parking Spaces: Minimum Spots Needed

Implement min_parking_spots(intervals) -> int

Behavior:
- Given a list of (start, end) times, return the minimum number of parking spots
  so that no car waits. If a car leaves at time t and another arrives at time t,
  the same spot can be reused.
"""

def min_parking_spots(intervals):
    # If no cars, no parking spots needed
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap for end times of occupied spots
    heap = []

    max_spots = 0

    for start, end in intervals:
        # Free any spots where the car has already left
        while heap and heap[0] <= start:
            heapq.heappop(heap)

        # Assign this car a spot (push its end time)
        heapq.heappush(heap, end)

        # Track peak number of occupied spots
        max_spots = max(max_spots, len(heap))

    return max_spots


if __name__ == "__main__":
    # Example manual test
    print(min_parking_spots([(1,4),(2,5),(7,9)]))  # Expected: 2
