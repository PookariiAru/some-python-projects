import zipfile
import itertools


class Bruteforce:
    def __init__(self, filename: str):
        self.filename = filename

    def create_combinations(self):
        alphabets = ["a", "b", "c", "d", "e", "1", "2", "3", "4", "5"]
        for passlen in [5]:
            combinations = itertools.product(alphabets, repeat=passlen)

        return ["".join(combination) for combination in combinations]

    def extract_zip(self, pwd: str, zip_file: str):
        pwd = str.encode(pwd)
        try:
            zip_file.extractall(pwd=pwd)
            return True
        except Exception:
            return False

    def bruteforce_zip(self):
        zip_file = zipfile.ZipFile(self.filename)
        dictionary = self.create_combinations()

        for line in dictionary:
            self.extract_zip(line, zip_file)


if __name__ == "__main__":
    test = Bruteforce("secret.zip")
    test.bruteforce_zip()
