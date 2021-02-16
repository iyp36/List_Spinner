print('Soal 2 - List Spinner')
print('='*30)

List_Awal=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

List_Output = [[],[],[],[]]

# Function Initialization
def counterClockwise(x):
    x = len(List_Awal)-1
    for i in range(len(List_Awal[0])): #=> 0 1 2 3 
        for j in range(len(List_Awal[0])): #=> 0 1 2 3  sebanyak 4 kali
            List_Output[i].append(List_Awal[j][x-i]) #=> menambahkan list output dengan index semua dari 3 2 1 0 dari setiap list angka sesuai urutan 0 1 2 3
    return List_Output
     
# Use the Function
print(counterClockwise(List_Awal))
