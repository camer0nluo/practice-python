"""
Messing around with garbage collection with circular references
and the gc and sys modules. Sys provides getrefcount()
"""

import gc
import sys


def main():
    a = 4
    b = 5

    c_list = [123, 456]
    # reference cycle
    c_list.append(c_list)
    c_list[2].append(789)

    # foo = ['hi']
    # c_list = foo

    print(c_list)

    print(f"Stats: {gc.get_stats()}")
    print(f"Count: {gc.get_count()}")
    print(f"GC enabled: {gc.isenabled()}")
    print(f"Threshold: {gc.get_threshold()}")
    print(f"c_list is tracked: {gc.is_tracked(c_list)}")

    """
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to getrefcount().
    """
    print(f"Reference count for c_list: {sys.getrefcount(c_list)}")
    del c_list[2]
    print(f"Reference count for c_list: {sys.getrefcount(c_list)}")

    print(f"Collecting: {gc.collect()}")

    print("Done.")


if __name__ == "__main__":
    main()
