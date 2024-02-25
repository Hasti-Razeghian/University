import json
from Course import Course

def write_file(data, file_name):
    json_object = json.dumps(data, indent=4)
 
    # Writing to sample.json
    with open(f"/home/hasti/Documents/py-edu/classhw/data/{file_name}.json", "w") as outfile:
        outfile.write(json_object)


# courses = {'a': 1, 'courses': ['dd', 'dddd'], 'c':3}


# courses = [Course('Algorithm', 1).course_dict(), 
#             Course('Python', 2).course_dict(), 
#             Course('Network', 3).course_dict()]

# write_file(courses[0], 'co')
# write_file(courses[1])