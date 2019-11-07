## Heapsort以及Mergesort時間複雜度比較
  Merge Sort  best case   NlogN 	average case   NlogN   worst case	  NlogN 
  Heap  Sort  best case   NlogN   average case   NlogN   worst case   NlogN 		         	           
上表格為五種排序法之時間複雜度比較(節錄自http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)
## Merge Sort 和 Quick Sort 的比較:
    Heap sort的原理在觀念上是一棵binary tree , 每個node (節點) 內的資料比它左右兩側 child nodes (子節點) 內的資料都小, 一個 heap 內如果有一個元素 x 的資料值改變，因而違反了 heap property，我們可以用 upheap 和 downheap 來修復這個heap tree , 建立 heap 的動作，先把所有元素不分順序直接放入heap中。 一開始將整個陣列的後半部看成是一大堆小 heaps，逐層由下往上建立稍大的 heaps，最後建立出一個完整的大 heap。
    merge , heap 這兩個演算法之間的爭議就很大 , 因為這兩個演算法的複雜度是比較好也比較接近的 , 很多的資料都有比較他們之間的優缺點 , 像是 merge sort雖然是 O(n log n) 但是他所需要的space就是 O(n) , heap sort 也是O(n log n) 同時也沒有space的問題 , 但是他程式的overhead 比較大,在某些情況反而會執行的比較慢。
    總而言之,比較完這兩個演算法後,可以發現到沒有最好的演算法,不同的case下,演算法的表現也不同,也就是說一個好的演算法是可以再不同的情況下去判定要使用那一種演算法,使得程式的效率可以達到最高。

(節錄自https://sls.weco.net/blog/lixs/11-jan-2007/1735)
