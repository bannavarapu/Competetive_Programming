def find_rectangular_overlap(rect1, rect2):

    # print(rect1.get('height'))
    # Calculate the overlap between the two rectangles
   (r1, r2) = (rect1, rect2) \
        if rect1['left_x'] <= rect2['left_x'] else (rect2, rect1)

    if r1['left_x'] + r1['width'] <= r2['left_x']:
        return None  # [r1] [r2] so no intersection

    left_x = max(r1['left_x'], r2['left_x'])
    right_x = min(r1['left_x'] + r1['width'], r2['left_x'] + r2['width'])
    width = right_x - left_x

    # order r1 and r2 bottom to top according to bottom of rect1 and rect2

    (r1, r2) = (rect1, rect2) \
        if rect1['bottom_y'] <= rect2['bottom_y'] else (rect2, rect1)

    if r1['bottom_y'] + r1['height'] <= r2['bottom_y']:
        return None  # r2 is entirely above r1, no intersection

    lower_y = max(r1['bottom_y'], r2['bottom_y'])
    upper_y = min(r1['bottom_y'] + r1['height'], r2['bottom_y'] + r2['height'])
    height = upper_y - lower_y

    intersection = {
        'left_x': left_x,
        'bottom_y': lower_y,
        'width': width,
        'height': height
    }

return intersection
        
