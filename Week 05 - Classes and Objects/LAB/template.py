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

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.


class Record:
    def __init__(self, label, value, limit):
        """Store the server's details."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the server's storage status."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"



# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.


def load_records(path):
    """Load server records from a file."""
    records = []

    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(
                Record(label, float(value), float(limit))
            )

    return records


records = load_records("servers.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)




over_limit_count = 0

for record in records:
    result = record.status()

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"Hostname: {record.label}")
    print(f"GB Used:  {record.value}")
    print(f"GB Total: {record.limit}")
    print(f"Status:   {result}")

    print("=" * 34)

    if result == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"{over_limit_count} of {len(records)} servers are OVER LIMIT")





# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring

# Check that two objects are independent

r1 = Record("srv-01", 87, 120)
r2 = Record("srv-02", 120, 100)

r1.value = 95

print("Independence check:")
print(r1.label, r1.value)
print(r2.label, r2.value)
