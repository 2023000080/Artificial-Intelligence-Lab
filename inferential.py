from kanren import run, var, fact, Relation
import sympy
from pyDatalog import pyDatalog

# ----------- KANREN -----------
print("Inferential logic using Kanren")

parent = Relation()

fact(parent, "john", "mary")
fact(parent, "mary", "sam")

x = var()

result = run(0, x, parent("john", x))
print("Children of john:", result)


# ----------- SYMPY -----------
print("\nInferential logic using SymPy")

p, q = sympy.symbols('p q')

rule = sympy.Implies(p, q)

result_sympy = rule.subs({p: True, q: True})

print("Implication (p -> q) when p=True, q=True:", result_sympy)


# ----------- PYDATALOG -----------
print("\nInferential logic using pyDatalog")

pyDatalog.create_terms('parent, grandparent, X, Y, Z')

+ parent("john", "mary")
+ parent("mary", "sam")

grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)

print("Grandparent relation:")
print(grandparent(X, Z))