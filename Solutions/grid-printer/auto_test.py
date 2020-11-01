import grid_printer


expected_grid1 = \
    """+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""
assert grid_printer.print_grid1() == expected_grid1


expected_grid2 = \
    """+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
"""
assert grid_printer.print_grid2(3) == expected_grid2


expected_grid3 = \
    """+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
"""
assert grid_printer.print_grid3(3, 4) == expected_grid3
