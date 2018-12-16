from random import randint
def losowe_zdanie(n=5):

    wyrazy= ["ala","ma","kota","a","kot","ma","ale"]

    i = 0
    zdanie = ""

    while i<n:
        index_los=randint(0, len(wyrazy)-1)
        zdanie += wyrazy[index_los]
        i +=1
    return zdanie
print(losowe_zdanie(3))