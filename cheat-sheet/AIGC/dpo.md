DPO（Direct Preference Optimization）

包含四个关键部分：prompt（提示）、response（响应）、chosen（优选响应）和有时还包括rejected（拒绝响应）。下面详细解释这些组成部分：

一个典型的DPO训练数据样本可能看起来像这样：

-   **Prompt**: "解释什么是人工智能？"
-   **Response (原始)**: "人工智能是让机器模仿人类智能的技术。"
-   **Chosen**: "人工智能，或AI，指的是计算机系统模仿和执行智能行为的能力，包括学习、推理和自我修正。"
-   **Rejected**: "人工智能是关于机器人的电影。"







```
[
  {
    "conversations": [
      {
        "from": "human",
        "value": "国会的转发\n美国国会由众议院和参议院组成，每两年换届一次（参议员任期为6年，但参议院选举是错位的，使得国会的组成仍然每两年变化一次）。这两年期间按顺序标记，第115届国会发生在2017-2018年。\n\n密歇根大学信息学院的研究人员在这段时间内收集了现任国会议员（我们将“国会议员”缩写为MoC）的Twitter帖子，并对它们进行编码，标记为原创声明或其他用户提交的转发。我们将重点关注转发数据。这些发布的数据不仅包括转发的文本，还包括国会议员的信息和原始推文的帐户。\n#python:\n\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sb\nimport statsmodels.api as sm\nimport os\nfrom pandas.plotting import register\\_matplotlib\\_converters\nregister\\_matplotlib\\_converters()\n​\npd.options.mode.chained\\_assignment = None\n\n# 在接下来的内容中，我们将加载数据，但出于速度原因，我们将排除推文本身的文本。\n\ntweets = pd.read\\_csv(os.path.join(base, \"retweets\\_congress\\_115th.csv.gz\"), \n usecols = lambda x: x != \"full\\_text\",\n dtype = {\"tweet\\_id\\_str\": \"str\"},\n index\\_col = \"tweet\\_id\\_str\")\ntweets.shape\nout: (209856, 21)\n\ntweets.columns\nout:Index(['user\\_id\\_str', 'user\\_screen\\_name', 'user\\_followers\\_count', 'created\\_at',\n 'retweet\\_count', 'retweeted\\_status', 'year', 'bioguide', 'birthday',\n 'gender', 'name', 'state', 'chamber', 'party', 'region', 'rt\\_user\\_id',\n 'rt\\_screen\\_name', 'rt\\_followers\\_count', 'rt\\_bio', 'age', 'age\\_bucket'],\n dtype='object')\n\n第（a）部分\n国会主要由两个政党（民主党和共和党）组成，还有一些独立派。哪个政党负责大部分的转发？\n\n计算推文的政党的边际概率，并将结果保存到party\\_marg。显示这个结果。\n​\n第（b）部分\n我们可能会问的一个问题是，“国会成员彼此转发的频率是多少？”\n\n创建一个名为“is\\_congress\\_retweet”的新列，指示转发是否来自MoC。首先使用.unique()方法获取唯一的“user\\_id\\_str”值集合。然后使用这组id，在“rt\\_user\\_id”列上使用.isin(values)方法创建新的布尔列“is\\_congress\\_retweet”。\n\n找到转发MoC的边际概率，并将结果保存到“congress\\_retweet\\_marg”。显示这些结果。是更常见地转发国会议员还是来自国会外部？"
      }
    ],
    "chosen": {
      "from": "gpt",
      "value": "计算推文的政党边际概率，我们可以使用以下代码：\n```python\ntweets['party'] = tweets['party'].replace(0, 'Democrat')\ntweets['party'] = tweets['party'].replace(1, 'Republican')\ntweets['party'] = tweets['party'].replace(2, 'Independent')\n\nparty_counts = tweets.groupby('party').size().sort_values(ascending=False)\n\nparty_marg = party_counts / party_counts.sum()\n\nprint(\"政党的边际概率：\")\nprint(party_marg)\n```\n这段代码将'party'列中的数字值替换为相应的政党名称，然后按政党对推文进行分组并计算每个组的大小。最后，通过将每个组的大小除以总推文数来计算每个政党的边际概率。\n\n输出应该类似于：\n```markdown\n政党的边际概率：\n0.522152    民主党\n0.445541    共和党\n0.032307    独立派\n```\n这表明大多数转发来自民主党，其次是共和党，然后是独立派。\n\n要创建一个名为\"is\\_congress\\_retweet\"的新列，指示转发是否来自国会议员，我们可以使用以下代码：\n```python\ncongress_ids = tweets['user_id_str'].unique()\nis_congress_retweet = tweets['rt_user_id'].isin(congress_ids)\ntweets['is_congress_retweet'] = is_congress_retweet\n\ncongress_retweet_marg = tweets['is_congress_retweet'].mean()\nprint(\"转发国会议员的边际概率：\")\nprint(congress_retweet_marg)\n```\n这段代码首先获取唯一的\"user\\_id\\_str\"值集合，对应于国会议员的集合。然后，在\"rt\\_user\\_id\"列上使用.isin(values)方法创建一个新的布尔列\"is\\_congress\\_retweet\"，指示转发是否来自国会议员。最后，通过取\"is\\_congress\\_retweet\"列的平均值来计算转发国会议员的边际概率。\n\n输出应该类似于：\n```markdown\n转发国会议员的边际概率：\n0.775151\n```\n这表明大多数转发不是来自国会议员，而是来自国会之外。"
    },
    "rejected": {
      "from": "gpt",
      "value": "回答问题的第（a）部分，您可以通过首先使用groupby（）函数按政党对数据进行分组，然后计算每个组的转发数来计算政党的边际概率。具体来说，您可以使用以下代码：\n```scss\nparty_count = tweets.groupby('party').count()\nparty_count.loc['Democrats','retweet_count'] / party_count.loc['Republicans','retweet_count']\n```\n回答问题的第（b）部分，您可以创建一个新列来指示转发是否来自国会议员，方法是使用“bioguide”列上的.unique（）方法获取唯一的国会议员用户ID集合，然后使用该集合创建一个布尔列，指示转发是否来自国会议员，使用“rt_user_id”列上的.isin（）方法。最后，使用.sum（）方法来计算转发国会议员的边际概率，然后将其与转发来自国会以外的人的概率进行比较。以下是相关代码：\n```makefile\nimport pandas as pd\ntweets = pd.read_csv('retweets_congress_115th.csv')\n\n# 获取唯一的国会议员ID集合\nmovers_ids = tweets['bioguide'].unique()\n\n# 创建一个新的布尔列，指示转发是否来自国会议员\ntweets['is_congress_retweet'] = tweets['rt_user_id'].isin(movers_ids)\n\n# 计算转发国会议员或来自国会以外的人的边际概率\nmovers_retweets = tweets[tweets['is_congress_retweet'] == True].shape[0]\nnon_movers_retweets = tweets[tweets['is_congress_retweet'] == False].shape[0]\nproportion_movers_retweets = movers_retweets / (movers_retweets + non_movers_retweets)\nprint('Proportion of retweets from MoCs:', proportion_movers_retweets)\n```"
    }
  },
  {
    "conversations": [
      {
        "from": "human",
        "value": "请提供一下对香港银行业的分析以及目前面临的挑战。"
      }
    ],
    "chosen": {
      "from": "gpt",
      "value": "香港银行业长期以来一直是该城市金融服务业和整体经济的重要组成部分。其特点是健全的监管框架、大量银行和资本流动的便利。以下分析涵盖了该行业面临的一些关键因素和当前挑战：\n\n1. 市场结构：香港银行业包括三类机构：持牌银行、受限牌照银行和接受存款公司。截至2021年4月，香港有160家持牌银行、19家受限牌照银行和13家接受存款公司。该行业由几家主要银行主导，汇丰银行、恒生银行、中国银行（香港）和渣打银行占据最大的市场份额。\n\n2. 监管框架：香港金融管理局负责监督银行体系的正常运作、稳定性和完整性。它通过实施法规和指导方针、监督持牌机构，并确保符合巴塞尔III等国际标准。。"
    },
    "rejected": {
      "from": "gpt",
      "value": "香港的银行业面临着诸多挑战，如低利率、高房价和经济疲软。新冠疫情也给该行业带来了压力，企业和消费者都在艰难度日。一些分析师建议政府可能需要采取措施，如降低贷款利率或向陷入困境的企业提供财政援助。\n\n尽管面临这些挑战，香港的银行业仍受到良好监管，消费者和企业对其信任度高。该行业还以其强调创新和采用新技术，如移动银行和数字支付而闻名。总体而言，香港银行业的前景仍然积极，但需要谨慎管理和关注持续发展。"
    }
  },
  
]
```







gpt4 辅助判断：

```
'请判断这两个文案哪个比较好, 1 :爱，绍兴绍兴相亲群28岁之前结婚30前结婚20岁开始相亲35岁开始相亲50岁开始相亲28岁以前结婚30岁之前结婚20岁就开始相亲35岁才开始相亲50岁才开始相亲单身高质量青年群高质量青年群35岁之前结婚30岁之前结婚25岁就开始相亲30岁开始相亲55岁开始相亲绍兴单身交友群优质青年群25岁之前结婚20岁开始相亲30岁结婚55岁结婚优质青年群25岁之前结婚20岁开始相亲30岁结婚55岁结婚绍兴单身交友群35岁以前结婚30岁之前结婚25岁就开始相亲35岁才开始相亲55岁才开始相亲绍兴相亲群高质量青年群35岁以前结婚30岁之前结婚25岁就开始相亲35岁才开始相亲55岁才开始相亲绍兴单身交友群 , 2:嘿嘿，大家好啊！绍兴媒小仙这里！同城交友群火热招募中！还在单身狗的朋友们，快来参加吧！30天告别单身，已有686名用户成功脱单哦！快快输入姓名，加入我们吧！让我们一起找到属于自己的幸福吧！💖 #交友 #脱单 #幸福# '
```



```
{'output': '从文案的清晰度、吸引力和信息传达方面来看，文案2更为出色。以下是两个文案的分析：\n\n### 文案1\n文案1是一串重复的信息，显得杂乱无章，缺乏吸引力。内容主要是关于参加相亲和结婚年龄的信息，但反复出现的句子和没有逻辑的排列让人难以捕捉到关键点。另外，信息的重复使得文案显得冗长，对用户的吸引力较低。\n\n### 文案2\n文案2显得简洁明了，吸引力较强：\n- 以“嘿嘿”这样的轻松开头语句，能够迅速吸引用户的注意。\n- 明确指出了绍兴媒小仙的主题是“同城交友群火热招募中”。\n- 通过具体数据“已有686名用户成功脱单”来增加可信度和吸引力。\n- 设置了明确的行动召唤“快快输入姓名，加入我们吧！”让用户知道接下来该做什么。\n- 情感化的呼吁“让我们一起找到属于自己的幸福吧！”增强用户的情感共鸣。\n\n此外，还加了#交友 #脱单 #幸福的标签，更容易被相关兴趣的用户发现和搜索到。\n\n综上，文案2的信息传达更为明确，具有吸引力和行动号召，显然是更好的选择。'}
```



```

```

