def stockPairs(stocksProfit, target):
    somados = []
    for i in range(len(stocksProfit) - 1):
        for j in range(i+1,len(stocksProfit)):
            if stocksProfit[i] + stocksProfit[j] == target and [stocksProfit[i], stocksProfit[j]] not in somados and [stocksProfit[j], stocksProfit[i]] not in somados:
                somados.append([stocksProfit[i], stocksProfit[j]])
    return len(somados)

print(stockPairs([5, 7, 9, 13, 11, 6, 6, 3, 3], 12)) # deve retornar 3
print(stockPairs([6, 6, 3, 9, 3, 5, 1], 12)) # deve retornar 2
print(stockPairs([92, 407, 1152, 403, 1419, 689, 1029, 108, 128, 1307, 300, 775, 622, 730,
    978, 526, 943, 127, 566, 869, 715, 983, 820, 1394, 901, 606, 497, 98, 1222,
    843, 600, 1153, 302, 1450, 1457, 973, 1431, 217, 936, 958, 1258, 970, 1155,
    1061, 1341, 657, 333, 1151, 790, 101, 588, 263, 101, 534, 747, 405, 585,
    111, 849, 695, 1256, 1508, 139, 336, 1430, 615, 1295, 550, 783, 575, 992,
    709, 828, 1447, 1457, 738, 1024, 529, 406, 164, 994, 1008, 50, 811, 564,
    580, 952, 768, 863, 1225, 251, 1032, 1460], 1558)) # deve retornar 45

