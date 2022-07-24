captains = {}
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

if "Enterprise" not in captains:
    captains["Enterprise"] = "Unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "Unknown"

del captains["Discovery"]

for ship in captains:
    print(f"The {ship} is captained by {captains[ship]}!")

captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko"),
    ]
)