#!/usr/bin/env python3

import sys
import subprocess

filename = sys.argv[1]
with open(filename) as file:
    for line in file.readlines():
        row = line.strip()
        print("old_directory => [{}]".format(row))
        new_row = row.replace("jane", "jdoe")
        print("new_directory => [{}]".format(new_row))
        subprocess.run(["mv", row, new_row])


# if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
# if test -e ~/data/jane_contact_07292018.csv; then echo "File exists"; else echo "File doesn't exist"; fi
# jdoe_profile_07272018.doc
# jdoe_contact_07292018.csv