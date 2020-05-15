from my_queue import Queue


def hot_potato(name_list, num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)
    while simqueue.size > 1:
        for _ in range(num-1):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()



if __name__ == '__main__':
    print(hot_potato(['A', 'B', 'C'], 2))