#Class Library 
import json

#Sample data
data ={
 
    'name': 'John Doe',
    'age': 35,
    'city': 'New York, NY',
    'interests': ['Nintendo','Football','Golf'],
    'is_student': False

}
#Writing data to a JSON file
with open('data.json', 'w') as json_file:

    json.dump(data,json_file, indent=4) 

print('Data has been written to data.json')
# I'm making a change to my file to prove that I just changed something.

#Reading from the JSON file
with open('data.json','r') as json_file:
#load the 
    loaded_data = json.load(json_file)

print('data loaded from data.json')
print(loaded_data)

#Modification is created
loaded_data['age'] = 29
loaded_data['interests'].append('Nintendo')



#Write the mods to the file.
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data to the data.json file')