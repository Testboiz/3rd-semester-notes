def FIFO(arr,frames):
    frameArr = [None] * frames
    fault = 0
    index = 0
    for item in arr :
        for i in range(frames):
            if frameArr[i] == None:
                frameArr[i] = item
                fault+=1
                break
        if item not in frameArr:
            fault+=1
            frameArr[index] = item
            index+=1
            index%=3
        print(frameArr)
    return fault

def Optimal(arr,frames):
    frameArr = [None] * frames
    fault = 0
    for item in arr :
        for i in range(frames):
            if frameArr[i] == None:
                frameArr[i] = item
                fault+=1
                break
    return fault

def LRU(arr,frames):
    frameArr = [None] * frames
    frameEndIndex = frames-1
    fault = 0
    for item in arr :
        isFirstEntry = False
        for i in range(frames):
            if frameArr[i] == None:
                frameArr[i] = item
                fault+=1
                isFirstEntry = True
                break
        if isFirstEntry:
            print(frameArr)
            continue
        if item in frameArr:
            itemIndex = frameArr.index(item)
            frameEnd = frameArr.index(frameArr[frameEndIndex])
            frameEnd,itemIndex = itemIndex, frameEnd
        else:
            frameArr.pop(0)
            frameArr.append(item)
            fault+=1
        print(frameArr)
    return fault

arr = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]

print(LRU(arr,3))