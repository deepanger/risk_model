# 风控模型（risk_model）自动建模代码

   由于一些原因吧，跳坑太频繁了，所以难以回到一个大厂做风控模型，因此就把这几年积攒的一些代码公开出来，
如果有人能有所裨益，把风险做好，也算是种安慰，真的挺喜欢作风控的哈哈哈。当然可能存在一些bug，等有心情在
好好修改添加吧。如果发现bug或者使用问题欢迎发邮件给我：fengyuguohou2010@hotmail.com

# 目录：

1、一些非传统衍生类的的数据处理，包括缺失值处理，label_encode,离散值woe赋值，基于y信息的tf-idf，基于四种无监督聚类（kmeans，pca，tsne，nmf）变量衍生，基于gbdt的变量衍生
有时间（后续会把基于rnn之类的衍生加上）。存在data_transform.py文件。

2、自动woe最优分箱（单调或者单峰且满足iv等条件），接近sas-em效果，不太需要手动介入调整。bin_new.py

3、变量选择：基于psi，相关性，iv，ks和变量聚类。auswahlen.py

4、因子分析：无监督的因子分析。factor_analysis.py

5、样本分布对齐，可以做类似样本的迁移学习，在大样本中召回更接近新业务小样本进行学习。distribution_adjust.py

6、建模代码，包括stewise选变量和蒙特卡洛选变量的逻辑回归，lgbm，rnn。以及基于shap和分箱对比的机器学习变量解释性代码。build_model.py

7、评分卡打分代码。score.py

