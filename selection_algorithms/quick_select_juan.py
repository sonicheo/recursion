
import random

class QuickSelect():
    def __init__(self,arr):
        self.arr = arr

    def swap(self,fi,si):
        self.arr[fi], self.arr[si] = self.arr[si],self.arr[fi]

    def partition(self,fi,si):
        ri = random.randint(fi,si)
        print(self.arr)
        self.swap(ri,si)
        for i in range(fi,si):
            if self.arr[i] < self.arr[si]:
                self.swap(i,fi)
                fi += 1
        self.swap(fi,si)
        return fi

    def selection(self,fi,si,k):
        check = self.partition(fi,si)
        print(f"Check: {check}")
        if check < k:   
           return self.selection(check+1,si,k)
        elif check > k:
           return self.selection(fi,check-1,k)
        
        return select.arr[check]

    def run(self,k):
        #k is the hightest_lowest value that we are looking for
        k = k-1
        fi = 0
        si = len(self.arr) - 1
        return self.selection(fi,si,k)


arr = [1,2,-5,10,100,-7,3,4]
select = QuickSelect(arr)
print(select.run(5))