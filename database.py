# For today use in-memory list, tomorrow we add real PostgreSQL
# This is same logic as RANK() OVER(PARTITION BY...)
def get_top_failing_services(logs):
    from collections import Counter
    # Count per service
    counts = Counter()
    for log in logs:
        if "hostel-service" in log: counts["hostel-service"] += 1
        if "mess-service" in log: counts["mess-service"] += 1
        if "library-service" in log: counts["library-service"] += 1
        if "admin-service" in log: counts["admin-service"] += 1

    # RANK() simulation
    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return ranked

# Test it
if __name__ == "__main__":
    print(get_top_failing_services(open("logs.txt").readlines()))