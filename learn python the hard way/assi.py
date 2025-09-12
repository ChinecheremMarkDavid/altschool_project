def humidity_checker():
    normal_humidity = 50
    current_humidity = int(input("what is the current humidity"))

    if current_humidity >= 45 and current_humidity <= 50:
        print("it is normal")
    else:
        print("raise an alarm")

humidity_checker()