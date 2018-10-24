temp_str = "C12.3"
if temp_str[0] in ['F', 'f']:
    f_temp = float(temp_str[1:])
    c_temp = (f_temp - 32) / 1.8
    print("%.2f" % c_temp)
elif temp_str[0] in ["C", "c"]:
    c_temp = float(temp_str[1:])
    f_temp = 1.8 * c_temp + 32
    print("%.2f" % f_temp)
