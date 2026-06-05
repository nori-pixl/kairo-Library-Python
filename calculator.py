import kairo as kr

def index():
    # --- 入力Aのビット定義（12345 = 0011 0000 0011 1001） ---
    A0  = kr.inname("A0",  1)
    A1  = kr.inname("A1",  0)
    A2  = kr.inname("A2",  0)
    A3  = kr.inname("A3",  1)
    A4  = kr.inname("A4",  1)
    A5  = kr.inname("A5",  1)
    A6  = kr.inname("A6",  0)
    A7  = kr.inname("A7",  0)
    A8  = kr.inname("A8",  0)
    A9  = kr.inname("A9",  0)
    A10 = kr.inname("A10", 1)
    A11 = kr.inname("A11", 1)
    A12 = kr.inname("A12", 0)
    A13 = kr.inname("A13", 0)
    A14 = kr.inname("A14", 1)
    A15 = kr.inname("A15", 0)

    # --- 入力Bのビット定義（6789 = 0001 1010 1000 0101） ---
    B0  = kr.inname("B0",  1)
    B1  = kr.inname("B1",  0)
    B2  = kr.inname("B2",  1)
    B3  = kr.inname("B3",  0)
    B4  = kr.inname("B4",  0)
    B5  = kr.inname("B5",  0)
    B6  = kr.inname("B6",  0)
    B7  = kr.inname("B7",  1)
    B8  = kr.inname("B8",  0)
    B9  = kr.inname("B9",  1)
    B10 = kr.inname("B10", 0)
    B11 = kr.inname("B11", 1)
    B12 = kr.inname("B12", 1)
    B13 = kr.inname("B13", 0)
    B14 = kr.inname("B14", 0)
    B15 = kr.inname("B15", 0)

    # --- キャリー初期値 ---
    Cin = kr.inname("Cin", 0)

    # --- 16ビット全加算器の並び ---
    S0   = kr.XOR(A0, B0, Cin)
    C0   = kr.OR(kr.AND(A0, B0), kr.AND(B0, Cin), kr.AND(A0, Cin))

    S1   = kr.XOR(A1, B1, C0)
    C1   = kr.OR(kr.AND(A1, B1), kr.AND(B1, C0), kr.AND(A1, C0))

    S2   = kr.XOR(A2, B2, C1)
    C2   = kr.OR(kr.AND(A2, B2), kr.AND(B2, C1), kr.AND(A2, C1))

    S3   = kr.XOR(A3, B3, C2)
    C3   = kr.OR(kr.AND(A3, B3), kr.AND(B3, C2), kr.AND(A3, C2))

    S4   = kr.XOR(A4, B4, C3)
    C4   = kr.OR(kr.AND(A4, B4), kr.AND(B4, C3), kr.AND(A4, C3))

    S5   = kr.XOR(A5, B5, C4)
    C5   = kr.OR(kr.AND(A5, B5), kr.AND(B5, C4), kr.AND(A5, C4))

    S6   = kr.XOR(A6, B6, C5)
    C6   = kr.OR(kr.AND(A6, B6), kr.AND(B6, C5), kr.AND(A6, C5))

    S7   = kr.XOR(A7, B7, C6)
    C7   = kr.OR(kr.AND(A7, B7), kr.AND(B7, C6), kr.AND(A7, C6))

    S8   = kr.XOR(A8, B8, C7)
    C8   = kr.OR(kr.AND(A8, B8), kr.AND(B8, C7), kr.AND(A8, C7))

    S9   = kr.XOR(A9, B9, C8)
    C9   = kr.OR(kr.AND(A9, B9), kr.AND(B9, C8), kr.AND(A9, C8))

    S10  = kr.XOR(A10, B10, C9)
    C10  = kr.OR(kr.AND(A10, B10), kr.AND(B10, C9), kr.AND(A10, C9))

    S11  = kr.XOR(A11, B11, C10)
    C11  = kr.OR(kr.AND(A11, B11), kr.AND(B11, C10), kr.AND(A11, C10))

    S12  = kr.XOR(A12, B12, C11)
    C12  = kr.OR(kr.AND(A12, B12), kr.AND(B12, C11), kr.AND(A12, C11))

    S13  = kr.XOR(A13, B13, C12)
    C13  = kr.OR(kr.AND(A13, B13), kr.AND(B13, C12), kr.AND(A13, C12))

    S14  = kr.XOR(A14, B14, C13)
    C14  = kr.OR(kr.AND(A14, B14), kr.AND(B14, C13), kr.AND(A14, C13))

    S15  = kr.XOR(A15, B15, C14)
    C15  = kr.OR(kr.AND(A15, B15), kr.AND(B15, C14), kr.AND(A15, C14))

    # --- 出力定義 ---
    out0  = kr.outname("Ans0", S0)
    out1  = kr.outname("Ans1", S1)
    out2  = kr.outname("Ans2", S2)
    out3  = kr.outname("Ans3", S3)
    out4  = kr.outname("Ans4", S4)
    out5  = kr.outname("Ans5", S5)
    out6  = kr.outname("Ans6", S6)
    out7  = kr.outname("Ans7", S7)
    out8  = kr.outname("Ans8", S8)
    out9  = kr.outname("Ans9", S9)
    out10 = kr.outname("Ans10", S10)
    out11 = kr.outname("Ans11", S11)
    out12 = kr.outname("Ans12", S12)
    out13 = kr.outname("Ans13", S13)
    out14 = kr.outname("Ans14", S14)
    out15 = kr.outname("Ans15", S15)
    
    out_overflow = kr.outname("Overflow", C15)
