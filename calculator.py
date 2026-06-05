import kairo as kr

def index():
    A1 = kr.inname("A1", 1)
    A3 = kr.inname("A3", 1)
    B0 = kr.inname("B0", 1)
    B2 = kr.inname("B2", 1)

    for i in range(16):
        A[i] = kr.inname("A{i}", 0)
        B[i] = kr.inname("B{i}", 0)

    C_minus_1 = kr.inname("Cin", 0)

    for i in range(16):
        S[i] = kr.XOR(A[i], B[i], C[i-1])
        C[i] = kr.OR(kr.AND(A[i], B[i]), kr.AND(B[i], C[i-1]), kr.AND(A[i], C[i-1]))
        out[i] = kr.outname("Ans{i}", S[i])

    out_overflow = kr.outname("Overflow", C15)
