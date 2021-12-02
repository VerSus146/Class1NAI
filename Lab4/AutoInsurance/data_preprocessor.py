from numpy import loadtxt

def import_data() -> []:
    data = loadtxt('AutoInsurance/auto_insurance_sweden.txt', delimiter='\t',
                   dtype=([('claims', 'i1'), ('total_payment', 'f4')]),
                   skiprows=1, usecols=(0, 1))
    return data
