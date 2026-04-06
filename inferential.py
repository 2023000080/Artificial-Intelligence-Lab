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

pyDatalog.clear()

# IMPORTANT: use different names
pyDatalog.create_terms('parent_pd, grandparent_pd, X, Y, Z')

+ parent_pd('john', 'mary')
+ parent_pd('mary', 'sam')

grandparent_pd(X, Z) <= parent_pd(X, Y) & parent_pd(Y, Z)

print("Grandparent relation:")
print(grandparent_pd(X, Z))
