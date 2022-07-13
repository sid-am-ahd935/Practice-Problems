## Basically the question asks for the longest substring with all unique characters, and this solution here requires a lot of optimisation
def test_1(string = ""):

    # initialising the substring

    substring = " "
    testList = []
    initial = 0

    for char in string:
        for i in range(initial, len(string)):
            substring += string[i]

            if substring.count(string[i]) > 1:
                testList.append(substring[:-1])
                initial += 1
                substring = " "
                break

    maxi = ""
    for word in testList:
        if len(word) > len(maxi):
            maxi = word

    if len(maxi) < 3:
        return "-1"

    else:
        return maxi


if __name__ == "__main__":
    print(test_1("character"))
    print(test_1("standfan"))
    print(test_1("class"))