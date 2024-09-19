import largest_number_finder.pdf as pdf

# Defining main function
def main():
    fileName = 'test_files/test_file.pdf'
    maxNum, numberFound = pdf.find_largest_number(fileName)
    if not numberFound:
        print('No number was found in ', fileName)
    else:
        print('Largest number in ', fileName, ': ', maxNum)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()