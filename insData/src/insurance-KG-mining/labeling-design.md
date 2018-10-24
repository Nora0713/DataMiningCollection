### 初始设计想法

05.09 Junjie Yao, <junjiey@gmail.com>

**miniminal crowdsource labelling website设计**：

1. 标注提示信息展示
2. 标注答案收集记录
3. 用户权限管理和行为记录
4. 标注结果清理和分析。

#### 工作意义：
  - 收集到足够有价值的行业专家标注数据，便于我们后面更容易讲故事的storytelling，几千条*20维的数据记录还是很impressive的。
  - but，实现会比较engineering些。当做熟悉和上手吧。

#### 技术储备：
  - 数据库：用关系型的传统设计还是新的nosql的嵌套灵活方式？两者在数据组织，更新等方面的差异
  - web framework：
     - 比较熟悉的，开发起来比较快捷的？node.js or django or others?
     - 点击、交互等的Ajax及时记录实现难易（得高明老师组农业图谱有初步的修改功能？不过没有做太全。）
  - 界面布局：bootstrap？
  - 分析逻辑：python为主吧？

#### 数据筛选：
  - 3000条左右，类别、描述和候选文本. 05.10 ready?
  - 其他辅助信息。

#### 后台数据库：
1. table 1：
     保险产品的基本描述信息 （read only）
2. table 2：
     产品的属性的候选文本（会有一定补充和调整）
3. table 3：
      产品属性的标注值（属性key，属性值，标注者）频繁更新吧。

remark：以上使用relational db or mongodb的嵌套灵活模式？


#### 界面模块：
  - js or 展示为主的ajax行为收集？

#### 处理逻辑：
  - 分析标注的用户正确率和行为分布；
  - 收集和确认标注的统计信息。

#### 相关参考：
1. https://github.com/CrowdTruth/CrowdTruth  两年前的，php，mongodb。

2. https://github.com/Scifabric/pybossa python，postgresql，也比较重一些。
