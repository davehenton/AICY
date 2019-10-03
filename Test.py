from text_coding_lib.math_lib.basic_math_lib.test_number_odd import isOdd
from text_coding_lib.math_lib.basic_math_lib.test_divisor import isDivisor
from text_coding_lib.math_lib.basic_math_lib.test_divisor import threeIsDivisor, fiveIsDivisor, sevenIsDivisor, elevenIsDivisor, thirteenIsDivisor

a=525
b=574
c="Test"
d=5
e=121
f=390

a_r=isOdd(a)
b_r=isOdd(b)
c_r=isDivisor(a,d)
d_r=isDivisor(a,b)
e_r=threeIsDivisor(a)
f_r=threeIsDivisor(b)
g_r=fiveIsDivisor(a)
h_r=fiveIsDivisor(b)
i_r=sevenIsDivisor(a)
j_r=sevenIsDivisor(d)
k_r=elevenIsDivisor(e)
l_r=elevenIsDivisor(b)
m_r=thirteenIsDivisor(f)
n_r=thirteenIsDivisor(b)

print(a_r)  #True
print(b_r)  #False
print(c_r)  #True
print(d_r)  #False
print(e_r)  #True
print(f_r)  #False
print(g_r)  #True
print(h_r)  #False
print(i_r)  #True
print(j_r)  #False
print(k_r)  #True
print(l_r)  #False
print(m_r)  #True
print(n_r)  #False
