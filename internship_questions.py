def count_intersections(data):
    # List to intersection labels
    intersections = []

    # List to store ending points
    unique_endpoints = []

    pie = 3.14

    for i in range(len(data[0])):
        for j in range(i + 1, len(data[0])):
            # Check if angles are within valid range (0 to 2 * π)
            if data[0][i] < 0 or data[0][i] > (2 * pie) or data[0][j] < 0 or data[0][j] > (2 * pie):
                return "Values should be between 0 to 2 * π"

            # Check if labels indicate starting and ending points of different chords
            if data[1][i][2:] != data[1][j][2:]:
                # If the starting and ending point is already processed, skip
                if data[1][j] in unique_endpoints or data[1][i] in unique_endpoints:
                    pass
                # If the label is already counted as an intersections, remove it
                elif data[1][j][2:] in intersections:
                    intersections.remove(data[1][j][2:])

                # if it is unique, add it to intersections
                else:
                    intersections.append(data[1][j][2:])
            if data[1][i][2:] == data[1][j][2:]:
                # Add the ending point to the list of endpoints
                unique_endpoints.append(data[1][j])

    # Return the count of intersections
    return len(intersections)

data = [(0.9, 1.47, 1.77, 3.92), ("s_1", "s2", "e_1", "e_2")]
print(count_intersections(data))




