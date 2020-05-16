import sys

def Loot(no_of_items, knapsack_weight):
    vpu = []
    v = [0] * no_of_items #values of all items
    w = [0] * no_of_items #weights of all items
    val = 0

    for i in range(no_of_items) :
        x = input()
        v[i],w[i] = map(int, x.split())
        #print(v[i])
        #print(w[i])
        vpu.append(v[i]/w[i]) #value per unit weight
        #print(vpu)

    if no_of_items == 1 and w[0] <= knapsack_weight :
        return v[0]
    if no_of_items == 1 and w[0] > knapsack_weight :
        return (knapsack_weight * vpu[0])

    
    while knapsack_weight > 0 :
        i = vpu.index(max(vpu))
        #print(vpu[i])
        n = w[i] if w[i] <= knapsack_weight else knapsack_weight
        #print(n)
        val += (vpu[i] * n)
        knapsack_weight -= n
        del vpu[i]
        del w[i]
        del v[i]
    return val

if __name__ == '__main__' :
    m = sys.stdin.readline()
    no_of_items, knapsack_weight = map(int, m.split())
    print("{:.4f}".format(float(Loot(no_of_items, knapsack_weight))))


    

