from flask import request, jsonify
from app import app
import heapq

# Helper function to calculate the max number of bugs fixed
def max_bugsfixed(bugseq):
    bugseq.sort(key=lambda x: x[1])  # Sort by escalation time limit
    total_time = 0
    bug_count = 0
    min_heap = []
    
    for difficulty, limit in bugseq:
        if total_time + difficulty <= limit:
            heapq.heappush(min_heap, -difficulty)  # Using max heap via negative values
            total_time += difficulty
            bug_count += 1
        elif min_heap and -min_heap[0] > difficulty:
            # Replace larger duration bug with current one if it's beneficial
            total_time += difficulty + heapq.heappop(min_heap)
            heapq.heappush(min_heap, -difficulty)

    return bug_count

# Define the /bugfixer/p2 route
@app.route('/bugfixer/p2', methods=['POST'])
def bugfixer_p2():
    data = request.json  # Get the posted JSON data
    results = []
    
    for bug_info in data:
        bugseq = bug_info.get('bugseq', [])
        results.append(max_bugsfixed(bugseq))
    
    return jsonify(results)  # Return the results as JSON