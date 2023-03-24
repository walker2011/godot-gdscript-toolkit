import sys
from gdtoolkit.formatter import format_code

formatted_code = format_code(sys.stdin.read(), 1e8)
sys.stdout.write(formatted_code)