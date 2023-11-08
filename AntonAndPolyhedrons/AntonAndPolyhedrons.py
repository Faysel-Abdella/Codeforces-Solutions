def countSides(polyhedrons):
    sides = 0
    for i in range(polyhedrons):
        polyhedron = input()
        if polyhedron == "Tetrahedron":
            sides += 4
        elif polyhedron == "Cube":
            sides += 6
        elif polyhedron == "Octahedron":
            sides += 8
        elif polyhedron == "Dodecahedron":
            sides += 12
        elif polyhedron == "Icosahedron":
            sides += 20         
    
    return sides

tests = int(input())
print(countSides(tests))