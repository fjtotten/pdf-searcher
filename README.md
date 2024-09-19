# PdfSearcher

### Description
This library searches pdf files for the largest number present. It considers units of magnitude, such as 100 million.

### Known Weaknesses
- A numeric value is required to start the number. For example: 'one hundred million' will not be considered a number in the search.
- A float value is always returned, regardless of the original numeric type.
- This searches each page in series instead of parralellizing any of the processing.

### Future Improvements
- If the scaling requires it, each page could be searched independently with map-reduce or a similar parallel framework.
  - The mapper will perform single page processing, returning the maximum as well as units of magnitude to start and the running value at the end.
  - The reducer will check for cross page numeric values using the start/end values and compare the maximums seen.
- Fully string numbers can be checked by expanding/improving the unit of magnitude conversion into a full string->number conversion. This was viewed as out of scope for this project.
- The return type can be cleaned up to be the type of the number seen.

### Install the requirements
```
pip install pypdf
```

### Running
A couple test files are included. More can be added. The main method uses `test_files/test_file.pdf`. This can be used as a library as well with any filename being passed into `largest_number_finder/pdf.py`.
