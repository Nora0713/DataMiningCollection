
## 面向保险领域的知识图谱构建与分析进展

05.09, Junjie Yao, <junjiey@gmail.com>


### 主要模块与环节进展。
 - 基本信息检索： http://dm-ecnu.org:8001/textSearch.html
 - 数据来源检索： http://dm-ecnu.org:5601/
 - 知识图谱检索：http://dm-ecnu.org:7474/browser/

#### 数据抽取（data extraction）：
  - 来源：保险行业协会，PDF保单数据
  - 方法：基本的规则和模式抽取方式，暂未尝试deepdive等。
  - 效果：precision可以，recall&coverage较低？
  - next step：crowdsourcing，label；新的数据来源？
    - website
    - app，保险大师？  

#### 数据存储（data storage）：
  - 文本、属性：Elastic，全文检索
  - 知识图谱： Neo.4j， 关联分析
  - next step：
    - 标注、取值等用户行为，mongoDB？
    - 文本和KG的匹配关联、丰富


#### 图谱分析（data mining）:
 - 产品画像：
   - 当前的基本属性，以及缺失值。
   - 优化目标

 - 问答模型：
    - LSTM，tree model：自动生成，基于已有问题训练。
    - next step：已有问题和KG的融合
 - 特征抽取：
    - 迭代过程？
 - next step：
    - 评估模型和baseline？

#### 数据检索交互（data retrieval）.
 - 站点：Node.js
 - 分析呈现：kibana，neo4j and others。
 - next step：
   - crowdsouring？


### Puzzling Issues：
 - 属性覆盖度？
 - 产品的更新度？
 - 数据来源覆盖？
 - 评估模型？
 - 站点的规模？

### 05.27 milestone.
  - 站点：
  - 数据：
  - 基本的QnA & relationship extraction papers。


### 06.07 milestone.
  - 量化模型
  - 数据更新？
