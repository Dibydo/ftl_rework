class Srs():
    def __init__(self, left_term, right_term):
        self.left_term = left_term
        self.right_term = right_term

    def __str__(self) -> str:
        return f"{self.left_term} -> {self.right_term}"

    def __eq__(self, __o: object) -> bool:
        return str(self) == str(__o)

    def __ne__(self, __o: object) -> bool:
        return str(self) != str(__o)

    def __hash__(self) -> int:
        return len(str(self))

    def to_trs(self):
        print(self.left_term)
        print(self.right_term)
        temp_res_l = ""
        for i in range(len(self.left_term)):
            temp_res_l += self.left_term[i] + "("
        temp_res_l += "x"
        for i in range(len(self.left_term)):
            temp_res_l += ")"

        temp_res_r = ""
        for i in range(len(self.right_term)):
            temp_res_r += self.right_term[i] + "("
        temp_res_r += "x"
        for i in range(len(self.right_term)):
            temp_res_r += ")"
        return "(" + temp_res_l + " = " + temp_res_r + ")"
