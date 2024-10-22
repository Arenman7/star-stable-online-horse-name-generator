def clean_name_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    first_scroll = []
    second_scroll = []
    current_scroll = first_scroll

    for line in lines:
        line = line.strip()
        if line == "The First Scroll Bar:":
            current_scroll = first_scroll
        elif line == "The Second Scroll Bar":
            current_scroll = second_scroll
        elif line and not line[0].isdigit():
            current_scroll.append(line)

    return first_scroll, second_scroll