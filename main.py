import sys

from parser import Parser
from complition import Algorithm


if __name__ == '__main__':
    p = Parser(sys.argv[1])
    order, variables, constructors, rules = p.get_parsed_data()
    print(f"order: {order}\nvariables: {variables}\nconstructors: {constructors}")
    for x in rules:
        print(x)
    if order == 'lexicographic' or order == 'anti-lexicographic':
        a = Algorithm(order, rules)
        a.start()
    else:
        print('incorrect input')
