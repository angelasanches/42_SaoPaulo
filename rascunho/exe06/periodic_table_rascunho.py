# Function to read periodic_table.txt and parse the data
def read_periodic_table(file_path):
    elements = {}
    with open(file_path, 'r') as file:
       # lines = file.readlines()
        for line in file:
            data = line.strip().split(', ')
            attrs = {}
            for item in data:
                key,value = item.split(':')
                attrs[key] = value
                elements = attrs
    return elements

# Function to generate HTML code for the periodic table
def generate_html(elements):
    html = "<!DOCTYPE html>\n<html>\n<head>\n<title>Periodic Table</title>\n"
    html +='<style>'
    html += '<table {border-collapse: collapse; }\n'
    html +='td {padding: 10px;}\n'
    html += 'td[data-value="true"] { border: 1px solid black;}\n'
    html += '</style>'
    html += '</head>\n<body>\n<table>\n'
    
    for element, attrs in elements.items():
        position = int(attrs['position'])
        if position % 18 == 0:
            if position != 0:
                html += "</tr>\n"
            html += "</tr>\n"
            current_position = 0
        while current_position < position:    
               html += "<td></td>\n" 
               current_position += 1
        if position == current_position:            
                html += f"<td data-value='true'>\n"
                html += f"<h4>{element}</h4>\n"
                html += "<ul>\n"
                html += f"<li>No {attrs['number']}</li>\n"
                html += f"<li>{attrs['small']}</li>\n"
                html += f"<li>{attrs['molar']}</li>\n"
                html += f"<li>{attrs['electron']} electrons</li>\n"
                html += "</ul>\n"
                html += "</td>\n"
    html += "</table>\n</body>\n</html>"
    return html

# Function to write HTML code to periodic_table.html
def write_html(output_file):
    with open(periodic_table.html, 'w') as file:
        file.write(output_file)

# Main function
def main():
    file_path = 'periodic_table.txt'  
    elements = read_periodic_table(file_path)
    output_file = generate_html(elements) #Saida do arquivo
    write_html(output_file)  #escrever no arquivo

if __name__ == "__main__":
    main()