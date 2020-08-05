def bubbleSort(list, orderAsc):
    print('> Initiate: bubbleSort(list, orderAsc)');
    listParam = [];
    listParam = list;

    if orderAsc==1:
        print('>> Sorting ascending order');
        for index in range(len(listParam)-1):
            print(listParam[index], listParam[index+1]);
    else:
        print('>> Sorting descending order');

    print('> Result: ', listParam);
    print('> Close: bubbleSort(list, orderAsc)');


list = [1, 30, 8, 77, 27, 65]
bubbleSort(list, 1);
