## fasttext

FastText是一种高效的词向量和文本分类模型，由Facebook AI Research（FAIR）团队开发。其核心原理在于通过学习词的子结构信息来改进词向量的表示，并且在文本分类任务中展现出高效性能。

基于经典的Skip-gram模型。

**子词（Subword）**。即字符n-grams。

这意味着每个词被分解为多个子词序列，如“apple”可以分解为“<ap, ple, app, pple, e>”。这种方法有助于解决未登录词（Out-of-Vocabulary, OOV）

每个子词都有一个向量表示，最终一个词的向量是其所有子词向量的加权和或平均。



**负采样**：在训练过程中，FastText也可能使用负采样技术来减少训练时间，通过随机选取少量的“负例”来近似优化过程



## fasttext 和word2vec的区别

1.  FastText，引入了子词概念，可以处理oov词 ， word2vec 直接对整个词建模。
2.  CBOW模式中， fasttext 预测中心词，输入的是n-gram的统计信息 。  word2vec 输入的词的id，输出是
3.  FastText可以直接将文本中所有词的向量简单相加或平均，然后用于分类。





## glove



uid : [query1,query2, query3]

 整个query ，不分词



```
output:
query :  sim_query1,sim_query2
```

