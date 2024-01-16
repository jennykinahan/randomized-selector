import argparse
import random

import errors

def process_list(filename: str, count: int) -> list[str]:
    list_from_file: list[str] = []
    try:
        with open(filename) as file:
            while line := file.readline():
                list_from_file.append(line.rstrip())
    except:
        raise errors.ListProcessingError

    if count > len(list_from_file):
        raise errors.CountOutOfBounds
    
    return list_from_file

def output_selected(elements: list[str], count: int) -> list[str]:
    results: list[str] = []
    random.shuffle(elements)
    for i in range(0, count):
        selected_element: str = random.choice(elements)
        results.append(f"{i+1}. {selected_element}")
        elements.remove(selected_element)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This application takes a newline-delimited \n'
                                     'file and will generate a randomized result based on the \n'
                                     'number of outcomes results desired.')
    parser.add_argument('--filename', help='The location of the newline-delimited file to process',
                        required=True)
    parser.add_argument('--count', default=1, type=int, help='The number of results requsted.  This \n'
                        'number must be greater than or equal to 1 and less than the length of \n'
                        'the originating list.  The count can only be an integer. \n'
                        'This defaults to 1.')
    args: argparse.Namespace = parser.parse_args()

    list_from_file: list[str] = process_list(args.filename, args.count)
    results: list[str] = output_selected(list_from_file, args.count)

    print('Results:')
    print('\n'.join(results))
