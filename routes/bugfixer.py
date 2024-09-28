from flask import Blueprint, request, jsonify
import heapq

# Create a Blueprint for the bugfixer route
bugfixer = Blueprint('bugfixer', __name__)

# POST route to handle the bug fixing request
@bugfixer.route('/bugfixer/p2', methods=['POST'])
def max_bugsfixed():
    data = request.get_json()
    results = []

    # Loop through each task in the input data
    for task in data:
        bugseq = task["bugseq"]
        # Calculate the maximum number of bugs that can be fixed
        max_bugs = find_max_bugs_fixed(bugseq)
        results.append(max_bugs)
    
    # Return the results as JSON
    return jsonify(results)

def find_max_bugs_fixed(bugseq):
    # Sort the bugs by escalation limit
    bugseq.sort(key=lambda x: x[1])

    current_time = 0
    fixed_bugs = 0
    bug_heap = []  # This will act as a max-heap (negative values to simulate max-heap)

    # Debugging: print the initial sorted bug sequence
    print("Initial state:")
    print(f"Sorted bugseq: {bugseq}")
    print()

    # Loop through the sorted bugs
    for difficulty, limit in bugseq:
        print(f"Considering bug with difficulty: {difficulty} and limit: {limit}")
        # Add the difficulty to the max-heap (store as negative to simulate max-heap)
        heapq.heappush(bug_heap, -difficulty)
        current_time += difficulty

        # If current time exceeds the limit, remove the bug with the highest difficulty (smallest negative number)
        if current_time > limit:
            removed_bug = -heapq.heappop(bug_heap)
            current_time -= removed_bug
            print(f"Current time exceeds limit! Removed bug with difficulty: {removed_bug}")

        print(f"Current time after fixing: {current_time}")
        print(f"Total bugs fixed so far: {len(bug_heap)}")
        print("-" * 40)

    # Debugging: print the final number of bugs fixed
    fixed_bugs = len(bug_heap)
    print(f"Final number of bugs fixed: {fixed_bugs}")
    
    return fixed_bugs
