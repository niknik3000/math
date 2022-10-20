from random import randint
import re

class MathematicalExamples:
    def __check_result(self, users_res, ref_res):
        if not re.match(r"\d+", users_res) or int(users_res) != ref_res:
            print(f"Это неправильный ответ! Правильный {ref_res}")
            return False
        else:
            print("Правильно.")
            return True

    def multiplication(self):
        a = randint(2, 10)
        b = randint(2, 10)
        check = input(f"Сколько будет {a} умножить на {b}?\n")
        return self.__check_result(check, a * b)

    def __generate_examples_table(self):
        a = 1
        b = 1
        examples = []
        while a <= 90:
            while b <= 9:
                if a % b == 0 and a != b and b != 1 and a / b <= 9:
                    examples.append([a,b])
                b += 1
            b = 1
            a += 1
        return examples

    def division(self):
        example_tables = self.__generate_examples_table()
        a, b = example_tables.pop(randint(0, len(example_tables)))
        check = input(f"Сколько будет {a} разделить на {b}?\n")
        return self.__check_result(check, int(a / b))


if __name__ == "__main__":
    MathematicalExamples().division()