def create_phone_number(n):
    number_str = []
    for i in range(10):
        number_str.append(str(n[i]))
    number_str = ''.join(number_str)
    phone_number = "(" + number_str[0:3] + ") " + number_str[3:6] + "-" + number_str[6:10]
    return phone_number


def run():
    number = create_phone_number([1,2,3,4,5,6,7,8,9,0])
    print(number)


if __name__ == "__main__":
    run()