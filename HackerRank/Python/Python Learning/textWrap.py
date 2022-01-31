#Manuel Ortiz Hernández at 2020
import textwrap

def wrap(string, max_width):
	wrap_string = textwrap.wrap(string, max_width)
	return wrap_string

if __name__ == '__main__':
	string, max_width = input(), int(input())
	result = wrap(string, max_width)
	print(result)

