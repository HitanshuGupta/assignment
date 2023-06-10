'''Write a program that returns the file type from a file name. The type of the file is determined
from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
png,image) will be input.
The program takes input in the following form:
1. Input extension and type values in the form of a string having the following format:
a. "extension1,type1;extension2,type2;extension3,type3"
b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
"xyz.xls", "text.csv", "123"]'''

def get_file_types(extension_type_list, filenames):
    file_type_mapping = {}
    
    extension_type_pairs = extension_type_list.split(';')
    for pair in extension_type_pairs:
        extension, file_type = pair.split(',')
        file_type_mapping[extension] = file_type
    
    result = {}
    for filename in filenames:
        file_extension = filename.split('.')[-1]
        file_type = file_type_mapping.get(file_extension, 'unknown')
        result[filename] = file_type
    
    return result

# Get extension and type values from the user
extension_type_str = input("Enter extension and type values in the form of 'extension1,type1;extension2,type2': ")

# Get the list of filenames from the user
filenames_str = input("Enter a list of filenames separated by commas: ")
filenames = [filename.strip() for filename in filenames_str.split(',')]

# Get the dictionary of filename: type pairs
file_type_dict = get_file_types(extension_type_str, filenames)

# Print the result
for filename, file_type in file_type_dict.items():
    print(f"{filename}: {file_type}")
