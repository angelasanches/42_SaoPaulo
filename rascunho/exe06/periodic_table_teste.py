# Function to read element data and parse the data
def read_element_data(data):
    elements = {}
    for line in data.split('\n'):
        info = line.split(' = ')
        if len(info) >= 2:  # Verifica se há pelo menos dois elementos em info
            name = info[0].strip()
            properties = info[1].split(', ')
            elements[name] = {
                'position': int(properties[0].split(':')[1]),
                'number': int(properties[1].split(':')[1]),
                'small': properties[2].split(':')[1],
                'molar': float(properties[3].split(':')[1]),
                'electron': properties[4].split(':')[1]
            }
    return elements

# Function to write HTML code to periodic_table.html
def write_html(html, output_file):
    with open(output_file, 'w') as file:
        file.write(html)

# Main function
def main():
    element_data = """
    Hydrogen = position:0, number:1, small: H, molar:1.00794, electron:1
    Helium = position:17, number:2, small: He, molar:4.002602, electron:2
    ...
    Ununoctium = position:17, number:118, small: Uuo, molar:294, electron:2 8 18 32 32 18 8
    """
    elements = read_element_data(element_data)

    html = "<!DOCTYPE html>\n<html>\n<head>\n<title>Periodic Table</title>\n<style>\ntable {\nborder-collapse: collapse;\n}\ntd {\nborder: 1px solid black;\npadding: 10px;\n}\nh4 {\nmargin-top: 0;\n}\n</style>\n</head>\n<body>\n"
    html += "<table>\n"
    for row in range(1, 8):
        html += "<tr>\n"
        for col in range(1, 19):
            element_name = None
            for name, data in elements.items():
                if data['position'] == (col - 1) % 18 and data['number'] == row:
                    element_name = name
                    break
            if element_name:
                element = elements[element_name]
                html += f"<td>\n<h4>{element_name}</h4>\n<ul>\n"
                html += f"<li>No {element['number']}</li>\n"
                html += f"<li>{element['small']}</li>\n"
                html += f"<li>{element['molar']}</li>\n"
                html += f"<li>{element['electron']}</li>\n"
                html += "</ul>\n</td>\n"
            else:
                html += "<td></td>\n"
        html += "</tr>\n"
    html += "</table>\n</body>\n</html>"

    write_html(html, 'periodic_table.html')

if __name__ == "__main__":
    main()
