import hashlib
from database import get_top_failing_services

print("=== LogSense AI - Day 1 Real Build ===")

seen_hashes = set()
unique_logs = []

for line in open("logs.txt"):
    line = line.strip()
    if not line or "INFO" in line:
        continue

    # This is your O(1) dedup engine from resume - NOW YOU BUILT IT
    h = hashlib.md5(line.encode()).hexdigest()

    if h not in seen_hashes:
        seen_hashes.add(h)
        unique_logs.append(line)
        print(f"✓ NEW UNIQUE: {line}")
    else:
        print(f"✗ DUPLICATE SKIPPED: {line}")

print(f"\nTotal logs: 8, Unique logs: {len(unique_logs)}")
print("\n=== RANK() - Top Failing Services ===")
ranked = get_top_failing_services(unique_logs)
for rank, (service, count) in enumerate(ranked, 1):
    print(f"Rank {rank}: {service} - {count} failures")

print("\n=== This is REAL LogSense - You can explain every line ===")

from agent import db_agent

print("\n=== GenAI Agent Diagnosis ===")
for log in unique_logs:
    if "DB" in log or "Memory" in log:
        diagnosis = db_agent(log)
        print(f"Log: {log}")
        print(f" -> Agent says: {diagnosis.error_type} | Fix: {diagnosis.fix_action} | Confidence: {diagnosis.confidence}")