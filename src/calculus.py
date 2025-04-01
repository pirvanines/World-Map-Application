# pantele dreptelor tarilor
m_d1 = (300-60)/(245-410)
m_d2 = (410-300)/(385-245)
m_d3 = (410-325)/(490-505)
m_d4 = (325-235)/(505-435)

# pantele dreptelor oceanelor
m_d_OP = (460-220)/(203-55)
m_d_AT_1 = (465-380)/(265-340)
m_d_AT_2 = (435-380)/(415-340)
m_d_IN_1 = (420-330)/(495-530)
m_d_IN_2 = (355-330)/(580-530)
m_d_IN_3 = (445-355)/(605-580)

# Returneaza pozitia punctului fata de dreapta
def compare(val):
    if val > 0:
        return 1
    elif val == 0:
        return 0
    return -1

# Dreptele care despart tarile
def d1(x, y):
    res = y - 60 - m_d1*(x-410)
    return compare(res)

def d2(x, y):
    res = y - 300 - m_d2*(x-245)
    return compare(res)

def d3(x, y):
    res = y - 410 - m_d3*(x-490)
    return compare(res)

def d4(x, y):
    res = y - 325 - m_d4*(x-505)
    return compare(res)

# Spatiu nedefinit
def UndefinedSpace(x, y):
    if y < 70 or y > 460:
        return 1

# Spatiul oceanelor
def OceanulPacific(x, y):
    res = y - 220 - m_d_OP*(x-55)
    if compare(res) > 0:
        return 1
    return 0

def OceanulAtlantic(x, y):
    dr1 = y - 380 - m_d_AT_1*(x-340)
    dr2 = y - 380 - m_d_AT_2*(x-340)
    if compare(dr1) > 0 and compare(dr2) > 0:
        return 1
    return 0

def OceanulIndian(x, y):
    dr1 = y - 330 - m_d_IN_1*(x-530)
    dr2 = y - 330 - m_d_IN_2*(x-530)
    dr3 = y - 355 - m_d_IN_3*(x-580)
    if compare(dr1) > 0 and compare(dr2) > 0 and compare(dr3) > 0:
        return 1
    return 0