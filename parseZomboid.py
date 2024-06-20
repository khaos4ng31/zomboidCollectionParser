import json

def parseJson(file):
    try:
        with open(file, 'r') as f:
            jsonObj = json.load(f)
        return jsonObj
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON from '{file}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    f = 'zomboid.json.bak'
    response = parseJson(f)['response']
    workshop_items= response['collectiondetails'][0]['children']
    workshop_id_list = "WorkshopItems="
    count = 0

    for mod in workshop_items:
        count+=1
        workshop_id_list = workshop_id_list + mod['publishedfileid'] + ";\n"


with open('modlist.txt', 'w') as f:
    f.write(workshop_id_list)

f.close()

print("mod count is: " + str(count))
print(workshop_id_list[:-1])
