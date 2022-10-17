class Trs():
    def __init__(self, left_term, right_term):
        self.left_term = left_term
        self.right_term = right_term

    def __str__(self) -> str:
        return f"{self.left_term} = {self.right_term}"

    def __eq__(self, __o: object) -> bool:
        return str(self) == str(__o)

    def __ne__(self, __o: object) -> bool:
        return str(self) != str(__o)

    def __hash__(self) -> int:
        return len(str(self))