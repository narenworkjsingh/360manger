import json


class Utility():

# this method is written to read the json.data file and extract the value for provided key
  def getjsondata(key, value):
        with open("testdata\\testdata.json", "r") as file:
            #data = json.load(f)
            data = json.loads(file.read())
            return(data[key][value])
        

# this funtion is written to pass data value from UI and update it to json file
  def update_login_credentials(text_value, json_tag, json_key):
    # Load the JSON data from the file
    with open("testdata\\testdata.json", 'r') as file:
        data = json.load(file)
    
    # Update the specified JSON key and value in the specified JSON tag section
    print(json_tag)
    print(json_key)
    data[json_tag][json_key] = text_value

    # Write the updated JSON data back to the file
    with open("testdata\\testdata.json", 'w') as file:
        json.dump(data, file, indent=4)
    

# this method is written to generate customer test name and s3 folder name each time script run and update the value for name data field in json data file

  def generate_customerdata(json_tag, json_key):

    with open("testdata\\testdata.json", 'r') as file:
        data = json.load(file)

    # Get the current name value from the JSON data
    current_name = data[json_tag][json_key]

    # Find the last digit in the name
    last_digit_index = len(current_name)
    while last_digit_index > 0 and current_name[last_digit_index - 1].isdigit():
        last_digit_index -= 1

    # Extract the numeric part of the name, if any
    numeric_part = current_name[last_digit_index:]
    base_name = current_name[:last_digit_index]

    # Increment the numeric part and update the name
    if numeric_part.isdigit():
        new_numeric_part = str(int(numeric_part) + 1)
        updated_name = base_name + new_numeric_part
    else:
        updated_name = current_name + "1"  # If no numeric part found, append "1"

    # Update the name in the JSON data
    data[json_tag][json_key] = updated_name

    # Write the updated JSON data back to the file
    with open("testdata\\testdata.json", 'w') as file:
        json.dump(data, file, indent=4)

    # Return the updated name
    return updated_name


