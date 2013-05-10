# index_git.py
# 20130510, works
# David Prager Branner
'''Creates simple index of .md file-names and headers within those files, in a
Git repository. Exports two .js files to be read by JS look-up script.'''

import os
import hashlib
import re
import pprint
import json
import nltk

top_dir_path = os.path.join('', 'CONTENT')
list_of_dirs = []
list_of_paths = []
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
        'set-up', 'key-bindings', 'OS_X'
        ]
unwanted_words = [
        'be', 'go',
        ]
treebank_to_wordnet_dict = {
        'J': nltk.wordnet.wordnet.ADJ, 
        'R' : nltk.wordnet.wordnet.ADV, 
        'N' : nltk.wordnet.wordnet.NOUN, 
        'V' : nltk.wordnet.wordnet.VERB,
        }

def generate_headword(word, treebank_POS, wnl_obj):
    if treebank_POS[0] not in treebank_to_wordnet_dict:
        return ''
    else:
        return wnl_obj.lemmatize(word,
                treebank_to_wordnet_dict[treebank_POS[0]])

def add_f_to_list(top_dir_path = top_dir_path):
    for f in os.listdir(top_dir_path):
        if f[0] == '.':
            continue
        the_path = os.path.join(top_dir_path, f)
        if os.path.isdir(the_path):
            list_of_paths.append(the_path)
            add_f_to_list(the_path)
        else:
            list_of_paths.append(the_path)
    return list_of_paths

def make_filename_into_string(the_path):
    filename = os.path.split(the_path)[-1]
    if filename in not_unwanted_words:
        return filename
    # Directory names are excluded from the following
    if os.path.isfile(the_path):
        filename_parts = filename.split('.')
        filename, extension = filename_parts[0], filename_parts[-1]
        if (not extension) or ('~' in extension):
            return ''
    return filename.replace('_', ' ').strip()

def normalize_words(strings, wnl_obj):
    words_to_report = []
    for the_string in strings:
        words_to_divide = []
        words_not_to_divide = []
        hash_of_whole_string = str(the_string.__hash__())
        the_string = the_string.lower()
        the_string = re.sub('"|^\.', '', the_string)
        tokenized_words = nltk.word_tokenize(the_string)
        tagged_words = nltk.pos_tag(tokenized_words)
        for word, treebank_POS in tagged_words:
            if (word[0] == '`' == word[-1]) or (word in not_unwanted_words):
                word = word.replace('`', '')
                words_not_to_divide.append([word, hash_of_whole_string])
            else:
                words_to_divide.append([word, treebank_POS, 
                    hash_of_whole_string])
        for item in words_to_divide:
            word = item[0]
            treebank_POS = item[1]
            hash_of_whole_string = item[2]
            word = generate_headword(word, treebank_POS, wnl_obj)
            if (not word) or (word in unwanted_words):
                continue
            word = re.sub(to_be_stripped, '', word)
            if re.search(word_dividers_ptrn, word):
                small_list = re.split(word_dividers_ptrn, word)
                for subword in small_list:
                    words_to_report.append([subword, hash_of_whole_string])
            else:
                words_to_report.append([word, hash_of_whole_string])
        for word_and_string_hash in words_not_to_divide:
            words_to_report.append(word_and_string_hash)
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
            header_lines.append(line.strip())
        # Next find setext headers
        elif (re.search(equals_all_ptrn, next_line) or 
                re.search(hyphens_all_ptrn, next_line)):
            header_lines.append(line)
    return header_lines

def prepare_tuple_storage(tuple_storage, all_strings, path_type, the_path, the_string):
    tuple_storage[str(the_string.__hash__())] = (
            path_type, the_path, the_string)
    all_strings.append(the_string)
    return tuple_storage, all_strings

def remove_dups(list_of_lists):
    list_of_lists = tuple(tuple(a_list) for a_list in list_of_lists)
    list_of_lists = list(set(list_of_lists))
    list_of_lists.sort()
    return list_of_lists

def main():
    index_entries = {} 
    all_strings = []
    tuple_storage = {}
    list_of_paths = add_f_to_list()
    wnl_obj = nltk.stem.WordNetLemmatizer()
    # First create hash-based dictionary of string-path tuples; then index the
    # words in the strings of that dictionary. The purpose of the dictionary is
    # to thin the main redundancies - filenames that reappear in one of the
    # headers within them.
    for the_path in list_of_paths:
        # Determine types
        if os.path.isdir(the_path):
            path_type = 'dir'
        else: path_type = 'file'
        # Process file name
        the_string = make_filename_into_string(the_path)
        if the_string:
            tuple_storage, all_strings = prepare_tuple_storage(tuple_storage,
                    all_strings, path_type, the_path, the_string)
        # Process headers
        if os.path.isfile(the_path):
            header_lines = find_headers(list_lines(the_path))
            if not header_lines:
                continue
            else:
                path_type = 'header'
            for the_string in header_lines:
                tuple_storage, all_strings = prepare_tuple_storage(
                        tuple_storage, all_strings, path_type, the_path, 
                        the_string)
    words_and_their_string_hashes = normalize_words(all_strings, wnl_obj)
    # Index words and path
    # Remove duplicate entries
    words_and_their_string_hashes = remove_dups(words_and_their_string_hashes)
    last_word = None
    for i, (word, the_hash) in enumerate(words_and_their_string_hashes):
        #  Change hashes to list of # hashes
        if word == last_word:
            index_entries[word].append(the_hash)
        else:
            index_entries[word] = [the_hash]
        last_word = word
#    for word in index_entries:
#        pprint.pprint(word)
#        for item in index_entries[word]:
#            pprint.pprint(tuple_storage[item])
    with open(os.path.join('JS', 'IndexEntries.js'), 'w') as f:
        f.write('var IndexEntries = ' + json.dumps(index_entries) + ';')
    with open(os.path.join('JS', 'TupleStorage.js'), 'w') as f:
        f.write('var TupleStorage = ' + json.dumps(tuple_storage) + ';')

if __name__ == '__main__':
    main()
