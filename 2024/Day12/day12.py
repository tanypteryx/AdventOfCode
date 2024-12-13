with open('input.txt') as fid:
    data = fid.read().splitlines()

visited = set()
for ii in range(len(data)):
    for jj in range(len(data[0])):
        visited.add((ii,jj))


def flood_fill(image, x, y):
    region = []
    rows, cols = len(image), len(image[0])
    region_label = image[x][y]

    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop(0)
        if (cx, cy) not in region and image[cx][cy]==region_label:
            region.append((cx,cy))
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                if 0 <= nx < rows and 0 <= ny < cols:
                    queue.append((nx, ny))
    return set(region)

def find_perimeter_length(plot, name, data):
    result = 0
    perimeter = []
    rows, cols = len(data), len(data[0])
    for cx, cy in plot:
        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
            if 0 <= nx < rows and 0 <= ny < cols:
                if data[nx][ny] != name:
                    result += 1
                    perimeter.append((cx,cy))
            else:
                result += 1
                perimeter.append((cx,cy))
    return result, perimeter


# identify the plots via flood fill
plots = {}
while visited:
    start= visited.pop()
    name = data[start[0]][start[1]]
    plot = flood_fill(data, start[0], start[1])
    visited -= plot
    if name not in plots:
        plots[name] = [plot,]
    else:
        plots[name].append(plot)

result = 0
for name, fields in plots.items():
    for field in fields:
        # get perimeter
        plen, tst = find_perimeter_length(field, name, data)
        result += len(field)*plen
print(f'Part 1: {result}')

# Part 2 - ugliest code ever written, needs to be refactored before upload :(
