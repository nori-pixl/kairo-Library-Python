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

    # 0桁目だけループ外で処理（C_minus_1を安全に繋ぐため）
    S0 = kr.XOR(A0, B0, C_minus_1)
    C0 = kr.OR(kr.AND(A0, B0), kr.AND(B0, C_minus_1), kr.AND(A0, C_minus_1))
    out0 = kr.outname("Ans0", S0)

    # 1桁目から15桁目までをループで回す
    for i in range(15):
        # iは0から始まるので、+1 して 1桁目〜15桁目を表現
        S[i+1] = kr.XOR(A[i+1], B[i+1], C[i])
        C[i+1] = kr.OR(kr.AND(A[i+1], B[i+1]), kr.AND(B[i+1], C[i]), kr.AND(A[i+1], C[i]))
        out[i+1] = kr.outname("Ans{i+1}", S[i+1])

    out_overflow = kr.outname("Overflow", C14)
