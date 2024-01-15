# randomized-selector
A selector which takes a new line delimited file, and randomly chooses n-number of elements from the list.  Written in Python

The application works by taking a new-line delimited file, and can be provided a `count` that determines the number of results desired.

## Examples
With the file `example.txt` provided within the repository there are 6 fruits and vegetables in the file.

### You can randomly select one of the elements within the file by running the following:
```
python randomized_selector.py --filename=example.txt
```

And the output should resemble something like this:
```
Results:
1. orange
```

### You may also select multiple results from the list, but the count cannot be larger than the list size itself:
```
python randomized_selector.py --filename=example.txt --count=3
```

And the output should resemble something like this:
```
Results:
1. apple
2. orange
3. watermelon
```
