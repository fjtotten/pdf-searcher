import locale
from pypdf import PdfReader

# find_largest_number will return the float value of the largest number found in the pdf file.
# Note: this does not provide any special error handling in case the file does not exist or
# errors occur while parsing it.
def find_largest_number(fileName):
    # Set the locale to determine how to process '.' and ','
    locale.setlocale(locale.LC_ALL, '')

    # creating a pdf reader object
    reader = PdfReader(fileName)
    print('Searching across ', len(reader.pages), ' pages...')

    max = -1
    numFound = False
    # We use currentSet to understand whether a currentValue was actually seen.
    # It is possible for the current number to be less than 0, meaning a default
    # value for current is not a reliable indicator.
    current = -1
    currentSet = False
    for p in reader.pages:
        # Search each page for the maximum number. 
        # Note: this does not find numbers split across pages.
        n, found, current, currentSet = find_largest_number_in_text(p.extract_text(), current, currentSet)
        if found:
            if n > max or not numFound:
                max = n
            numFound = True
    return max, numFound

# find_largest_number returns the largest number found in the text
def find_largest_number_in_text(text, current, currentSet):
    words = text.split()

    # Like currentSet, we use maxSet to determine if a max value has been set for this page
    # instead of using max == -1 to imply that it is unset.
    max = -1
    maxSet = False
    for word in words:
        try:
            current = locale.atof(word)
            currentSet = True
        except ValueError:
            # If the text does not modify a numeric value, we continue
            if not currentSet:
                continue
            # If the word is a unit of magnitude, convert is to the numeric value
            unit = getUnitOfMagnitude(word)
            if unit == None:
                currentSet = False
                continue
            current = current * unit
        # wWether a new numeric value was seen or the current one was modified with
        # a unit of magnitude, set the max value seen accordingly
        if current > max or not maxSet:
            max = current
            maxSet = True
    return max, maxSet, current, currentSet

# getUnitOfMagnitude checks common units of magnitude up to 1 trillion
def getUnitOfMagnitude(word):
    # Always lower case the word for consistent comparison
    word = word.lower()
    if word == "hundred":
        return 100
    if word == "thousand":
        return 1000
    if word == "million":
        return 1000000
    if word == "billion":
        return 1000000000
    if word == "trillion":
        return 1000000000000