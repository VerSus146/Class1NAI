def sex_converter(sex):
    if "M" in sex:
        return 0
    else:
        return 1


def chestpaintype_converter(cpt):
    if "ASY" in cpt:
        return 0
    elif "NAP" in cpt:
        return 1
    elif "ATA" in cpt:
        return 2
    elif "TA" in cpt:
        return 3


def restingecg_converter(recg):
    if "Normal" in recg:
        return 0
    elif "LVH" in recg:
        return 1
    elif "ST" in recg:
        return 2


def exerciseangina_converter(ea):
    if "N" in ea:
        return 0
    elif "Y" in ea:
        return 1


def st_slope_converter(sts):
    if "Up" in sts:
        return 0
    elif "Flat" in sts:
        return 1
    elif "Down" in sts:
        return 2
