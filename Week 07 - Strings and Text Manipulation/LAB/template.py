"""
RECORD CHECK  -  my version
===========================

Name  :sumaya
Lane  :  IT      
Date  :5/11

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# 
def parse_line(raw_line):
    """Clean a server record and return a dictionary."""
    parts = raw_line.strip().lower().split(",")

    hostname = parts[0].strip()
    used = float(parts[1].split("=")[1].strip())
    total = float(parts[2].split("=")[1].strip())

    return {
        "hostname": hostname,
        "used": used,
        "total": total
    }


def status_of(record):
    """Return the server's storage status."""
    percent = record["used"] / record["total"] * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"



# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.


raw_records = []

with open("servers.txt", "r") as file:
    for line in file:
        raw_records.append(line)



# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.


over_limit_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    result = status_of(record)

    print(record, "Status:", result)

    if result == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"{over_limit_count} of {len(raw_records)} servers are OVER LIMIT")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
