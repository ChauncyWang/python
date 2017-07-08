from pywork import core
from pywork.algorithm import word_weight

if __name__ == "__main__":
    print(u'\u2588\u2588'*20, "布尔搜索测试")
    core.bl()
    print(u'\u2588\u2588'*20, "VSM 测试:")
    # 拿来做查询的十个例子
    sentences = ["北京历史上最大的一次", "我最爱苹果手机", "全国普通高校", "超级女声杭州赛区的海选", "美国众议院军事委员会",
                 "所谓的精英其实就是把自己封闭在所谓精英圈中的自闭症患者", "信息获取渠道相对贫乏", "手机天线要不断地发送微波无线电信息",
                 "妇女和儿童最易遭受缺碘危害", "现在我每天都能收到短信汇报当天的销售业绩"]
    while True:
        k = input("请输入要分析相关性的前k名:k的值(0,退出此辅助程序)")
        if k == '0':
            exit(0)
        for sentence in sentences:
            core.vsm(sentence, k=int(k))

        print("分析完成，请查看文档并手工标注,进行分析!")
