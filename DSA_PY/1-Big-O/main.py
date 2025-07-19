import time

nemo = ["nemo"] * 100000



def find_nemo(array: list):
    t0 = time.time()  # start time
    for name in array:
        if name == "nemo":
            print("I found player")

    t1 = time.time()  # end timer

    return f"It took {(t1-t0) * 1000: .2f} millisec"


print(find_nemo(nemo))



