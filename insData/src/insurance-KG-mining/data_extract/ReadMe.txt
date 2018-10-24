Readme.txt - 殷擎
文件的命名均由a.xls里面文档链接中的后缀名确定
1、 a.xls中在售pdf有9814个，经过下载并用qpdf转化后，发现bc3f288f-dff5-4a6a-a2f7-08b5cce86312_TERMS.PDF是需要非空密码才可打开，所以在insurances_byid_qpdf文件夹中去掉了此pdf，所以insurances_byid_qpdf文件夹中共有9813个pdf
2、 qpdf_txt 文件夹是pdf->txt的产物，共成功了 8834个文档（ps. 成功的每个文档的转化程度不一）
3、转化失败的文档记录放在了 exception_add.txt


为了解决复旦提出的的
1、我们发现抽取到了部分团体保险，考虑到团体保险在议价能力、个人选择等方面和个人保险的不同，建议去掉团体保险的保单之后再抽样；
2、样本数量的话，我们发现，如果直接随机抽样，可能存在某些类别不足的问题（因为本身基数比较小，抽到的概率比较小），因此建议在仍然抽取100或200的情况下，对未达到10个样本的小类（如健康保险-失能保险）再抽取，直到达到10个样本为止（有些全部加起来可能也不超过10个，那么就全部计入）
这些问题，后续进行了修改
InsurClass_pandas_mod_noGroup.py 得出每类中去掉团体险的保险， 结果输出至 InsurClass_pandas_mod_noGroup.xlsx
selectProduct_byclassratio.py 则是考虑到问题2的代码，并以100和200为基准抽取了selectProducts_num136、selectProducts_num228
两个文件夹，两文件夹中均包含description.txt，描述了文件夹中的信息。

相关文件夹
insurances_byid_qpdf、qpdf_txt、selectProducts_num136、selectProducts_num228
请看118.89.234.98服务器下用户qing目录
