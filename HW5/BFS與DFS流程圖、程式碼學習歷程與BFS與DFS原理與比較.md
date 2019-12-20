# BFS與DFS原理與比較
# DFS原理
* 深度優先搜尋演算法（英語：Depth-First-Search，DFS）是一種用於遍歷或搜尋樹或圖的演算法。沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。屬於盲目搜尋。

* 深度優先搜尋是圖論中的經典演算法，利用深度優先搜尋演算法可以產生目標圖的相應拓撲排序表，利用拓撲排序表可以方便的解決很多相關的圖論問題，如最大路徑問題等等。

* 時間複雜度：	{\displaystyle O(b^{m})}O(b^m)
* 空間複雜度：	{\displaystyle O(bm)}O(bm)
# BFS原理
* 廣度優先搜尋演算法（英語：Breadth-First-Search，縮寫為BFS），又譯作寬度優先搜尋，或橫向優先搜尋，是一種圖形搜尋演算法。簡單的說，BFS是從根節點開始，沿著樹的寬度遍歷樹的節點。如果所有節點均被存取，則演算法中止。廣度優先搜尋的實現一般採用open-closed表。

* 空間複雜度
* 因為所有節點都必須被儲存，因此BFS的空間複雜度為{\displaystyle O(|V|+|E|)}{\displaystyle O(|V|+|E|)}，其中{\displaystyle |V|}{\displaystyle |V|}是節點的數目，而{\displaystyle |E|}{\displaystyle |E|}是圖中邊的數目。註：另一種說法稱BFS的空間複雜度為{\displaystyle O(B^{M})}O(B^M)，其中B是最大分支係數，而M是樹的最長路徑長度。由於對空間的大量需求，因此BFS並不適合解非常大的問題，對於類似的問題，應用IDDFS以達節省空間的效果。

* 時間複雜度
* 最差情形下，BFS必須尋找所有到可能節點的所有路徑，因此其時間複雜度為{\displaystyle O(|V|+|E|)}{\displaystyle O(|V|+|E|)}，其中{\displaystyle |V|}{\displaystyle |V|}是節點的數目，而{\displaystyle |E|}{\displaystyle |E|}是圖中邊的數目。
