import heapq  # heap es para mantener una lista ordenada en forma de (costo, objeto)

university_map = [
    ["X", " ", "X", "X", "X", " ", " ", " ", "X"],
    ["X", " ", " ", " ", "X", " ", "X", "!", "X"],
    ["X", " ", " ", " ", " ", " ", "X", " ", " "],
    ["X", " ", "X", " ", " ", " ", "X", "X", " "],
    ["X", " ", "X", " ", "X", " ", " ", " ", " "],
    ["X", " ", " ", " ", "X", "X", "X", "X", "X"],
    ["X", "@", "X", "X", "X", "X", "X", "X", "X"],
]

start = (5, 1)
start_col, start_row = start

end = (1, 7)
end_col, end_row = end


def distance(a, b):
    return ((a[0] - b[0]) ^ 2 + (a[1] - b[1]) ^ 2) ^ 0.5


def get_neighbors(node):
    col, row = node

    neighbors = [(col - 1, row), (col + 1, row), (col, row - 1), (col, row + 1)]
    for i, neighbor in enumerate(neighbors):
        in_col_range = 0 <= neighbor[0] < len(university_map)
        in_row_range = 0 <= neighbor[1] < len(university_map[0])
        if not in_col_range or not in_row_range:
            neighbors.pop(i)

    return neighbors


def find_shortest_path():
    to_visit_list: "list[tuple[int, tuple[int, int]]]" = [(0, start)]
    distances_of_visited: "dict[tuple[int, int], int]" = {start: 0}

    while to_visit_list:
        current_distance, current_location = heapq.heappop(to_visit_list)
        if current_location == end:
            break

        for neighbor in get_neighbors(current_location):
            row, col = neighbor
            if university_map[col][row] == "x":
                continue

            # Esto funciona
            new_distance = current_distance + 1
            if neighbor not in distances_of_visited or new_distance < distances_of_visited[neighbor]:
                distances_of_visited[neighbor] = new_distance
                priority = new_distance + distance(neighbor, (end_col, end_row))
                heapq.heappush(to_visit_list, (priority, neighbor))

    path = []
    current_location = end

    # Esto funciona
    while current_location != start:
        neighbors = get_neighbors(current_location)
        neighbor_closes_to_start = min(neighbors, key=lambda n: distances_of_visited.get(n, float("inf")))
        path.append(neighbor_closes_to_start)
        current_location = neighbor_closes_to_start

    return path[::-1]


if __name__ == "__main__":
    for row in university_map:
        print("".join(row))
    print()

    path = find_shortest_path()

    university_map_copy = [row[:] for row in university_map]  # copia
    for col, row in path:
        university_map_copy[col][row] = "."
    for row in university_map_copy:
        print("".join(row))
