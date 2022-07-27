
from func import Executer

er = Executer()
r = er.execute("x^2 + 2 * x + 1", 1)
f = er.get_function("x^2 + 2 * x + 1")

print(r)
print(f(1))

