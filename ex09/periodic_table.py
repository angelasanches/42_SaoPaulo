# Function to read element data from a file and parse the data
def read_element_data_from_file(file_path):
    elements = {}
    with open(file_path, 'r') as file:
        for line in file:
            info = line.strip().split(' = ')
            if len(info) >= 2:
                name = info[0]
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
    element_data_file = "periodic_table.txt"
    elements = read_element_data_from_file(element_data_file)

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

    output_file = "periodic_table.html"
    write_html(html, output_file)
    print(f"HTML file generated: {output_file}")

if __name__ == "__main__":
    main()
