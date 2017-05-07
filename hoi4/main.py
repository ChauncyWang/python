
file = open("r_modifiers_l_english.yml", 'r', encoding="UTF8").readlines()
modifiers = open("modifiers.txt", "w", encoding="UTF8")
desc = open("desc.txt", "w", encoding="UTF8")
others = open("others.txt", "w", encoding="UTF8")
for f in file:
    if f.startswith(" MODIFIER"):
        if "DESC" in f:
            desc.write(f)
        else:
            modifiers.write(f[10: len(f)])
    else:
        others.write(f)
