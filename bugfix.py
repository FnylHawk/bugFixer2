from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)

def max_bugsfixed(bugseq):
    # Sort the bugs by their escalation limit (the time before they expire)
    bugseq.sort(key=lambda x: x[1])
    
    total_time = 0
    bug_count = 0
    min_heap = []
    
    for difficulty, limit in bugseq:
        if total_time + difficulty <= limit:
            heapq.heappush(min_heap, -difficulty)
            total_time += difficulty
            bug_count += 1
        elif min_heap and -min_heap[0] > difficulty:
            # Replace the largest duration task if it's beneficial
            total_time += difficulty + heapq.heappop(min_heap)
            heapq.heappush(min_heap, -difficulty)

    return bug_count

@app.route('/bugfixer/p2', methods=['POST'])
def bugfixer_p2():
    data = request.json
    results = []
    
    for bug_info in data:
        bugseq = bug_info.get('bugseq', [])
        results.append(max_bugsfixed(bugseq))
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)