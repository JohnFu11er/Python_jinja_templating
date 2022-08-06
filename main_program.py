import jinja2
import json

# Read structured data from file
with open('my_data.json') as file:
    data = json.load(file)


# region Custom Jinja Filters
def ipaddressonly(value):
    ip = value.split("/")[0]
    mask = value.split("/")[1]  # Not currently used in function
    
    return ip
# endregion


# region Environment Assignment
file_loader = jinja2.FileSystemLoader('templates')

env = jinja2.Environment(loader=file_loader)
env.filters["ipaddressonly"] = ipaddressonly

template = env.get_template('main.j2')
# endregion

output = template.render(d = data)

print(output)
