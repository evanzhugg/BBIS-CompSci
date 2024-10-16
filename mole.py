# Mol Converter
# Element library
elements = {
    "H": {"name": "Hydrogen", "mass": 1.008},
    "He": {"name": "Helium", "mass": 4.0026},
    "Li": {"name": "Lithium", "mass": 6.94},
    "Be": {"name": "Beryllium", "mass": 9.0122},
    "B": {"name": "Boron", "mass": 10.81},
    "C": {"name": "Carbon", "mass": 12.011},
    "N": {"name": "Nitrogen", "mass": 14.007},
    "O": {"name": "Oxygen", "mass": 15.999},
    "F": {"name": "Fluorine", "mass": 18.998},
    "Ne": {"name": "Neon", "mass": 20.180},
    "Na": {"name": "Sodium", "mass": 22.990},
    "Mg": {"name": "Magnesium", "mass": 24.305},
    "Al": {"name": "Aluminium", "mass": 26.982},
    "Si": {"name": "Silicon", "mass": 28.085},
    "P": {"name": "Phosphorus", "mass": 30.974},
    "S": {"name": "Sulfur", "mass": 32.06},
    "Cl": {"name": "Chlorine", "mass": 35.45},
    "Ar": {"name": "Argon", "mass": 39.948},
    "K": {"name": "Potassium", "mass": 39.098},
    "Ca": {"name": "Calcium", "mass": 40.078},
    "Sc": {"name": "Scandium", "mass": 44.956},
    "Ti": {"name": "Titanium", "mass": 47.867},
    "V": {"name": "Vanadium", "mass": 50.942},
    "Cr": {"name": "Chromium", "mass": 51.996},
    "Mn": {"name": "Manganese", "mass": 54.938},
    "Fe": {"name": "Iron", "mass": 55.845},
    "Co": {"name": "Cobalt", "mass": 58.933},
    "Ni": {"name": "Nickel", "mass": 58.693},
    "Cu": {"name": "Copper", "mass": 63.546},
    "Zn": {"name": "Zinc", "mass": 65.38},
    "Ga": {"name": "Gallium", "mass": 69.723},
    "Ge": {"name": "Germanium", "mass": 72.63},
    "As": {"name": "Arsenic", "mass": 74.922},
    "Se": {"name": "Selenium", "mass": 78.971},
    "Br": {"name": "Bromine", "mass": 79.904},
    "Kr": {"name": "Krypton", "mass": 83.798},
    "Rb": {"name": "Rubidium", "mass": 85.468},
    "Sr": {"name": "Strontium", "mass": 87.62},
    "Y": {"name": "Yttrium", "mass": 88.906},
    "Zr": {"name": "Zirconium", "mass": 91.224},
    "Nb": {"name": "Niobium", "mass": 92.906},
    "Mo": {"name": "Molybdenum", "mass": 95.95},
    "Tc": {"name": "Technetium", "mass": 98},
    "Ru": {"name": "Ruthenium", "mass": 101.07},
    "Rh": {"name": "Rhodium", "mass": 102.91},
    "Pd": {"name": "Palladium", "mass": 106.42},
    "Ag": {"name": "Silver", "mass": 107.87},
    "Cd": {"name": "Cadmium", "mass": 112.41},
    "In": {"name": "Indium", "mass": 114.82},
    "Sn": {"name": "Tin", "mass": 118.71},
    "Sb": {"name": "Antimony", "mass": 121.76},
    "Te": {"name": "Tellurium", "mass": 127.60},
    "I": {"name": "Iodine", "mass": 126.90},
    "Xe": {"name": "Xenon", "mass": 131.29},
    "Cs": {"name": "Caesium", "mass": 132.91},
    "Ba": {"name": "Barium", "mass": 137.33},
    "La": {"name": "Lanthanum", "mass": 138.91},
    "Ce": {"name": "Cerium", "mass": 140.12},
    "Pr": {"name": "Praseodymium", "mass": 140.91},
    "Nd": {"name": "Neodymium", "mass": 144.24},
    "Pm": {"name": "Promethium", "mass": 145},
    "Sm": {"name": "Samarium", "mass": 150.36},
    "Eu": {"name": "Europium", "mass": 151.96},
    "Gd": {"name": "Gadolinium", "mass": 157.25},
    "Tb": {"name": "Terbium", "mass": 158.93},
    "Dy": {"name": "Dysprosium", "mass": 162.50},
    "Ho": {"name": "Holmium", "mass": 164.93},
    "Er": {"name": "Erbium", "mass": 167.26},
    "Tm": {"name": "Thulium", "mass": 168.93},
    "Yb": {"name": "Ytterbium", "mass": 173.05},
    "Lu": {"name": "Lutetium", "mass": 174.97},
    "Hf": {"name": "Hafnium", "mass": 178.49},
    "Ta": {"name": "Tantalum", "mass": 180.95},
    "W": {"name": "Tungsten", "mass": 183.84},
    "Re": {"name": "Rhenium", "mass": 186.21},
    "Os": {"name": "Osmium", "mass": 190.23},
    "Ir": {"name": "Iridium", "mass": 192.22},
    "Pt": {"name": "Platinum", "mass": 195.08},
    "Au": {"name": "Gold", "mass": 196.97},
    "Hg": {"name": "Mercury", "mass": 200.59},
    "Tl": {"name": "Thallium", "mass": 204.38},
    "Pb": {"name": "Lead", "mass": 207.2},
    "Bi": {"name": "Bismuth", "mass": 208.98},
    "Po": {"name": "Polonium", "mass": 209},
    "At": {"name": "Astatine", "mass": 210},
    "Rn": {"name": "Radon", "mass": 222},
    "Fr": {"name": "Francium", "mass": 223},
    "Ra": {"name": "Radium", "mass": 226},
    "Ac": {"name": "Actinium", "mass": 227},
    "Th": {"name": "Thorium", "mass": 232.04},
    "Pa": {"name": "Protactinium", "mass": 231.04},
    "U": {"name": "Uranium", "mass": 238.03},
    "Np": {"name": "Neptunium", "mass": 237},
    "Pu": {"name": "Plutonium", "mass": 244},
    "Am": {"name": "Americium", "mass": 243},
    "Cm": {"name": "Curium", "mass": 247},
    "Bk": {"name": "Berkelium", "mass": 247},
    "Cf": {"name": "Californium", "mass": 251},
    "Es": {"name": "Einsteinium", "mass": 252},
    "Fm": {"name": "Fermium", "mass": 257},
    "Md": {"name": "Mendelevium", "mass": 258},
    "No": {"name": "Nobelium", "mass": 259},
    "Lr": {"name": "Lawrencium", "mass": 262},
    "Rf": {"name": "Rutherfordium", "mass": 267},
    "Db": {"name": "Dubnium", "mass": 270},
    "Sg": {"name": "Seaborgium", "mass": 271},
    "Bh": {"name": "Bohrium", "mass": 270},
    "Hs": {"name": "Hassium", "mass": 277},
    "Mt": {"name": "Meitnerium", "mass": 278},
    "Ds": {"name": "Darmstadtium", "mass": 281},
    "Rg": {"name": "Roentgenium", "mass": 282},
    "Cn": {"name": "Copernicium", "mass": 285},
    "Nh": {"name": "Nihonium", "mass": 286},
    "Fl": {"name": "Flerovium", "mass": 289},
    "Mc": {"name": "Moscovium", "mass": 290},
    "Lv": {"name": "Livermorium", "mass": 293},
    "Ts": {"name": "Tennessine", "mass": 294},
    "Og": {"name": "Oganesson", "mass": 294}
}

# Avogadro's constant
_Na = 6.022e23

def start():
    notfinished = True
    while notfinished:
        print(
            "Welcome to the moles calculator, what would you like to do?\n"
            "1. Mass to moles\n"
            "2. Moles to molecules\n"
            "3. Mass to molecules\n"
            "4. Molecules to Mass\n"
        )

    choice = input("What option would you like? Type 'exit' to exit the program: ")
    if choice.lower == "exit":
        exit()

    try:
        mode = int(choice)
        if 0 < mode < 5:
            if mode == 1:
                masstomoles()
            elif mode == 2:
                molestonumber()

    except ValueError:
        print("You didn't input a valid value, or type \"exit\" to quit")

def masstomoles():
    mass = float(input("What is your mass?"))
    element = input("What is your element? Type in symbol of element (Capitalization matter)")
    element_mass = elements[element]["mass"]
    moles = mass / element_mass
    result = round(moles, 2)
    print(f"You have {result} moles of {elements[element]["name"]}")


def molestonumber():
    moles = float(input("How many moles of your element do you have?"))
    result = round(moles * _Na, 2)
    print(f"You have {result} atoms of your element")

def masstonumber():
    mass = float(input("What is your mass?"))
    element = input("What is your element? Type in symbol of element (Capitalization matter)")
    element_mass = elements[element]["mass"]
    moles = mass / element_mass
    result = round(moles * _Na, 2)
    print(f"You have {result} atoms of {elements[element]["name"]}")

def numbertomass():
    element = input("What is your element symbol? (Capitalization matter)")
    number = float(input("How many atoms do you have of your element?"))
    element_mass = elements[element]["mass"]
    moles = number * _Na
    result = round(moles * element_mass, 2)
    print(f"You have {result}g of {elements[element]["name"]}")

if __name__ == "__main__":
    start()