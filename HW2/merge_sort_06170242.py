#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Solution(object):
    def merge_sort(self,arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #先找到數列組中點
            L = arr[:mid] #將數列元素分兩半，且左半為到組中點前的數列;右半段為組中點到最後一數
            R = arr[mid:]  
  
            self.merge_sort(L)  #先排序左半段(前半段)
            self.merge_sort(R)  #再排序右半段(後半段) 
  
            i = j = k = 0 #先假設i,j,k為起始值
          
            #把資料暫時先複製到左、右半段(前後段) 
            while i < len(L) and j < len(R): #當i和j都小於左、右半段長度範圍內
                if L[i] < R[j]:  #假如右半段的起始值大於左半段起始值
                    arr[k] = L[i] #將比較小的左半邊放入新的陣列之首位 
                    i+=1 #因為L[i]中的首位被拉走了，所以繼續找下一位，即L[i+1]
                else: 
                    arr[k] = R[j] #將比較小的右半邊放入新的陣列之首位 
                    j+=1 #因為R[j]中的首位被拉走了，所以繼續找下一位，即R[j+1]
                k+=1 #當以上兩種情況一種成立執行時，k就往下一位找
          
            #此處情況為上述程式，左右半段有一處跑完時，另一數列即可直接加入新的陣列中
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
          
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
            
            return arr
# This code is contributed by Mayank Khanna;取用自geeksforgeeks.org/merge-sort/

