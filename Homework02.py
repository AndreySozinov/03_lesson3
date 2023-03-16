# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых
# частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

text = "Help on built-in module sys:\
    NAME\
    sys\
    MODULE REFERENCE\
    https://docs.python.org/3.10/library/sys.html\
    The following documentation is automatically generated from the Python\
    source files.  It may be incomplete, incorrect or include features that\
    are considered implementation detail and may vary between Python\
    implementations.  When in doubt, consult the module reference at the\
    location listed above.\
    DESCRIPTION\
    This module provides access to some objects used or maintained by the\
    interpreter and to functions that interact strongly with the interpreter.\
    Dynamic objects:\
    argv -- command line arguments; argv[0] is the script pathname if known\
    path -- module search path; path[0] is the script directory, else ''\
    modules -- dictionary of loaded modules\
    displayhook -- called to show results in an interactive session\
    excepthook -- called to handle any uncaught exception other than SystemExit\
      To customize printing in an interactive session or to install a custom\
      top-level exception handler, assign other functions to replace these.\
    stdin -- standard input file object; used by input()\
    stdout -- standard output file object; used by print()\
    stderr -- standard error object; used for error messages\
      By assigning other file objects (or objects that behave like files)\
      to these, it is possible to redirect all of the interpreter's I/O\
    last_type -- type of last uncaught exception\
    last_value -- value of last uncaught exception\
    last_traceback -- traceback of last uncaught exception\
      These three are only available in an interactive session after a\
      traceback has been printed."
COUNT = 10

cleared_text = ' '.join(filter(str.isalpha, text.lower().split())).split()
frequency_dict = {}

for word in set(cleared_text):
    frequency_dict[word] = cleared_text.count(word)

sorted_tuple = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
frequency_dict = dict(sorted_tuple)

i = 1
for word, amount in frequency_dict.items():
    print(f'{word} {amount}')
    if i == COUNT:
        break
    i += 1
