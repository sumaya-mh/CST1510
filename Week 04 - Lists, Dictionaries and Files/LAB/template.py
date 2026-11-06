"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(value, limit):
    """Check if the value is over the limit."""
    if value >= limit:
        return "OVER LIMIT"
    else:
        return "OK"

def print_report(label, status):
    """Print the report for a record."""
    print(f"Record {label}: {status}")

   
# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "10.0.0.5", "value": 12, "limit": 400},
    {"label": "10.0.0.6", "value": 450, "limit": 400},
    {"label": "10.0.0.7", "value": 25, "limit": 400}
]


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
results_file = open("results.txt", "w")
over_limit_count = 0
for record in records:
    status = check_record(record["value"], record["limit"])
    print_report(record["label"], status)
    results_file.write(f'{record["label"]},{status}\n')
    if status == "OVER LIMIT":
        over_limit_count += 1

print_report("Total records over limit", over_limit_count)
results_file.close()
       


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
