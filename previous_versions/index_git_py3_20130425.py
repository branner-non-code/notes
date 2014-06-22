# index_git_notes_01.py
'''Creates simple index of .md file-names and headers within those files, in a
Git repository.'''

import os
import hashlib
import re
import pprint
import json

top_dir_path = os.path.join('..', 'notes')
list_of_dirs = []
list_of_files = []
list_of_lines = []
hash_start_ptrn = re.compile('^#+')
hash_all_ptrn = re.compile('^#+$')
hash_end_prtn = re.compile('#+$')
equals_all_ptrn = re.compile('^=+$')
hyphens_all_ptrn = re.compile('^-+$')
word_dividers_ptrn = re.compile('''-|/''')
# Do not strip back-ticks until word has been accepted.
to_be_stripped = re.compile(''''|"|,''')
not_unwanted_words = [
        'Set-up', 'set-up', 'key-bindings',
        ]
unwanted_words = [
        'a', 'I',
        'on', 'in', 'an', 'of', 'to', 'at', 'my', 'My', 'up', 
        'the', 'one', 'for', 'new', 'has', 'how', 'and', 'use', 'set', 
        'with', 'than', 'from',
        'within', 'without', 'useful',
        ]

def add_f_to_list(top_dir_path = top_dir_path):
    for f in os.listdir(top_dir_path):
        if f[0] == '.':
            continue
        the_path = os.path.join(top_dir_path, f)
        if os.path.isdir(the_path):
            list_of_dirs.append(the_path)
            add_f_to_list(the_path)
        else:
            list_of_files.append(the_path)
#            print(os.path.isdir(the_path), the_path)
    return list_of_files, list_of_dirs

def make_dirname_into_string(dirname):
    dirname = os.path.split(dirname)[-1]
#    dirname = dirname.replace('_', ' ').strip()
    return dirname

def make_filename_into_string(filename):
    filename = os.path.split(filename)[-1]
    filename_parts = filename.split('.')
    filename, extension = filename_parts[0], filename_parts[-1]
    if not extension:
        return
    return filename.replace('_', ' ').strip()

def list_all_words(the_string):
    words = the_string.split()
    words_to_divide = []
    words_not_to_divide = []
    words_to_report = []
    for word in words:
        # strip 's
        word = word.replace("'s", '')
        if (not word):
            continue
        if (word[0] == '`' == word[-1]) or (word in not_unwanted_words):
            word.replace('`', '')
            words_not_to_divide.append(word)
        elif (word in unwanted_words):
            continue
        else:
            words_to_divide.append(word)
    # delete unwanted words
    for word in words_to_divide:
        word = re.sub(to_be_stripped, '', word)
        if re.search(word_dividers_ptrn, word):
            words_to_report.extend(re.split(word_dividers_ptrn, word))
        else:
            words_to_report.append(word)
    for word in words_not_to_divide:
        words_to_report.append(word)
    return words_to_report

def list_lines(path):
    with open(path) as f:
        return f.read().split('\n')

def find_headers(list_of_lines):
    header_lines = []
    # distinguish setext (underlined) and atx (#s at line-start) formats
    for line, next_line in zip(list_of_lines, list_of_lines[1:]):
        # First find atx headers
        # Lines that have no other content than # are ignored in MD but must 
        # be eliminated here.
        if (re.search(hash_start_ptrn, line) and not 
                re.search(hash_all_ptrn, line)):
            # Strip any initial or final hashes
            line = re.sub(hash_start_ptrn, '', line)
            line = re.sub(hash_end_prtn, '', line)
            header_lines.append(line)
        # Next find setext headers
        elif (re.search(equals_all_ptrn, next_line) or 
                re.search(hyphens_all_ptrn, next_line)):
            header_lines.append(line)
    return header_lines

def add_tuple_to_dict(dictionary, the_tuple):
    dictionary[the_tuple.__hash__()] = the_tuple
    return dictionary

def main():
    index_entries = []
    string_lookup = {}
    list_of_files, list_of_dirs = add_f_to_list()
    for the_dir in list_of_dirs:
        # Process directory name
        the_string = make_dirname_into_string(the_dir)
        dir_tuple = (the_string, 'dir', the_dir)
        string_lookup = add_tuple_to_dict(string_lookup, dir_tuple)
        words = list_all_words(the_string)
        # Index words and path
        for word in words:
            index_entries.append((word, dir_tuple.__hash__()))
    for the_file in list_of_files:
        # Process file name
        the_string = make_filename_into_string(the_file)
        if the_string:
            file_tuple = (the_string, 'file', the_file)
            string_lookup = add_tuple_to_dict(string_lookup, file_tuple)
            words = list_all_words(the_string)
            # index words and path
            for word in words:
                index_entries.append((word, file_tuple.__hash__()))
        # Process headers
        header_lines = find_headers(list_lines(the_file))
        for line in header_lines:
            string_lookup = add_tuple_to_dict(string_lookup, line)
            header_tuple = (the_string, 'header', line)
            words = list_all_words(line)
            # index words and path and line
            for word in words:
                index_entries.append((word, header_tuple.__hash__()))
    index_entries = list(set(index_entries))
    index_entries.sort()
    pprint.pprint(index_entries)
