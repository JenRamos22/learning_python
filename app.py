
luggage= [12, 25, 8, 23, 30, 15]

def luggage_Weight(weigth_list):
    heavy_suitcases = 0
    standard_suitcases = 0

    for weigth in weigth_list:
        if weigth >= 23:
            heavy_suitcases += 1

        else: 
            standard_suitcases += 1

    print("heavy suitcases")
    print(heavy_suitcases)
    print("standard suitcases")
    print(standard_suitcases)

luggage_Weight(luggage)




