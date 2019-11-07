#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Solution(object):
    def heapify(self,arr, n, i):  #arr為待排序的list,n為list的長度
        largest = i          # 初始值先假設最大值(父節點)為i
        l = 2 * i + 1        # l為左子節點 = 2*i + 1 
        r = 2 * i + 2        # r為右子節點 = 2*i + 2 
  
        #查看左子節點是否存在，且大於父節點
        #先假設l還在n(此list)的範圍內，且arr[l](對應位置數值)大於arr[i]初始位置數值;則li互換，最大值為l。
        if l < n and arr[i] < arr[l]: 
            largest = l 
  
        #查看左子節點是否存在，且大於父節點
        #一樣先確認r是否在n(此list)的範圍內，且arr[r](對應位置數值)大於arr[largest]最大位置數值;則r與largest互換，最大值為r。
        if r < n and arr[largest] < arr[r]: 
            largest = r 
  
        #如果需要，則更換父節點
        #倘若largest不等於i，則i與largest互換位置
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] 
  
            #執行此code，並且重新堆積List
            self.heapify(arr, n, largest) 
  
    #以下為主要heapsort排列主程式
    #首先先定義heap_sort排列arr(數列)的程式
    #n為arr此數列之長度   
    def heap_sort(self,arr):
        n = len(arr) 
  
    #建立maxheap
        #當i在此n[len(arr)]的長度範圍內，則以一次減1的方式列出到對應位置-1之前的數。{[n(起始位置),-1(結束位置),-1(運行方式)]}
        #則heapify組合起此數列
        for i in range(n, -1, -1): 
            self.heapify(arr, n, i) 
        
        #一一匯出元素
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] 
            self.heapify(arr, i, 0)
        return arr
# This code is contributed by Mohit Kumra;取用自 https://www.geeksforgeeks.org/python-program-for-heap-sort/

