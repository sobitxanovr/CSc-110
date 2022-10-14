#
# Author: Rustambek Sobithanov
# Class: CSc 110
# Description: The program determines and prints out the performance-level
#              of a CPU using user inputs gigahertz (given in float)
#              and core count (given in integer).
#

# inputs asking for the gigahertz and core count
gigahertz = float(input("Enter CPU gigahertz:\n"))
core_count = int(input("Enter CPU core count:\n"))
print()

# lines of codes to determine the performance level of a CPU
if gigahertz >= 0 and core_count >= 20:
    print('That is a high-performance CPU.')
elif gigahertz >= 3.2 and core_count >= 8:
    print('That is a high-performance CPU.')
elif gigahertz >= 2.5 and core_count >= 6:
    print('That is a medium-performance CPU.')
elif gigahertz >= 2.0 and core_count >= 2:
    print('That is a low-performance CPU.')
elif gigahertz < 2.0 and core_count >= 0:
    print('That CPU could use an upgrade.')
