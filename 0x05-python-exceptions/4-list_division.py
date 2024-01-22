#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = []
    t_r = 0
    for a in range(0, list_length):
        try:
            t_r = my_list_1[a] / my_list_2[a]
        except TypeError:
            t_r = 0
            print("wrong type")
        except ZeroDivisionError:
            t_r = 0
            print("division by 0")
        except IndexError:
            t_r = 0
            print("out of range")
        finally:
            pass
        division.append(t_r)
    return division
