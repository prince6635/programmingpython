def make_stdin_stdout_as_file():
    fileName = './data/test.txt'

    import sys
    stdinPrevious = sys.stdin
    stdoutPrevious = sys.stdout
    sys.stdin = open(fileName)
    sys.stdout = open(fileName, 'w')

    # sys.stdout.write('e f g\n')
    # print('e    f   g')
    # TODO: can't read any content if stdin and stdout both point to the file
    content = sys.stdin.read()
    sys.stdout.write(('.' * 4).join(sys.stdin.read().split('\t')))
    sys.stdout.write(sys.stdin.read().replace('\t', '.' * 4))

    sys.stdin.close()
    sys.stdout.close()
    sys.stdin = stdinPrevious
    sys.stdout = stdoutPrevious
    print('Back to console output')
    print('content: ' + content)

def testStringMethods():
    # slicing: substring extraction
    str = 'spam eggs ham'
    print(str[5:10])

    # concatenation (and *, len(), [ix])
    print('spam ' + 'eggs ham')
    print(3 * 'spam')

    # formatting expression: substitution
    formatted1 = 'spam %s %s' % ('eggs', 'ham')
    print(formatted1)

    # formatting method: % alternative
    formatted2 = 'spam {} {}'.format('eggs', 'ham')
    print(formatted2)

    # templating
    template = '---$target1---$target2---'
    val1 = 'spam'
    val2 = 'shrubbery'
    template = template.replace('$target1', val1)
    template = template.replace('$target2', val2)
    print(template)

    # string module's Template feature
    vals = {'key2': 'world', 'key1': 'Hello'}
    import string
    template = string.Template('---$key1---$key2---')
    template = template.substitute(vals)
    print(template)

    # parsing with split and join
    print('A B C D'.split())
    print('A+B+C+D'.split('+'))
    print('--'.join(['a', 'b', 'c']))
    make_stdin_stdout_as_file()


if __name__ == '__main__':
    # testStringMethods()

    from textprocess_lib import file_text
    # sum(eval(sys.argv[1]), sys.argv[2]))
    print(file_text.sum(5, './data/table1.txt'))
    print(file_text.sumWithZipsAndListComprehensions(5, './data/table2.txt'))
    sums = file_text.sumWithDictionaries('./data/table3.txt')
    for key in sorted(sums):
        print(key, '=', sums[key])
