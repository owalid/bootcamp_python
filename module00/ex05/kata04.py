t = ( 0, 4, 132.42222, 10000, 12345.67)

module = "module_" + str(t[0]).zfill(len(str(t[0])) + 1)
ex = "ex_" + str(t[1]).zfill(len(str(t[1])) + 1)
floated = ": " + str(round(t[2], 2))
exp = "{0:.2E}".format(t[3])
exp_float = "{0:.2E}".format(t[4])

print(module + " " + ex + " " + floated + " " + exp + " " + exp_float)