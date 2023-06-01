class board: 
    start_board = {x: x for x in range(1, 10)}
    previous_board = {}
    current_board = {x: f"[ {x} ]" for x in range(1, 10)}
    open_locations = {1, 2, 3, 4, 5, 6, 7, 8, 9}