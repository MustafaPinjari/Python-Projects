import json

if __name__ == '__main__':
    try:
        # Open and read the input.json file
        with open('C:/Users/pinja/OneDrive/Desktop/SANDIP UNIVERSITY/PROGRAM/PYTHON/Python-Projects/JsonToCsv/input.json', 'r') as f:
            file_content = f.read()
            
            # Check if the file is empty
            if not file_content.strip():
                raise ValueError("Input file is empty.")
            
            data = json.loads(file_content)  # Load JSON data from file content

        # Create CSV header from JSON keys
        output = ','.join([*data[0]])

        # Append each row of data
        for obj in data:
            output += f'\n{obj["Name"]},{obj["Age"]},{obj["Dob"]}'

        # Write the output CSV file
        with open('C:/Users/pinja/OneDrive/Desktop/SANDIP UNIVERSITY/PROGRAM/PYTHON/Python-Projects/JsonToCsv/output.csv', 'w') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')
