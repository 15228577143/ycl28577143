from datetime import datetime

def get_today():
    return datetime.now().strftime("%Y‑%m‑%d")

def generate_zhice(today):
    filename = f"职测A类_{today}.md"
    content = f"""# 事业单位联考A类｜职业能力倾向测验（{today}）
考试时长：90分钟｜满分：150分
适用类别：综合管理类（A类）

## 第一部分 常识判断（1‑20题）
<a id="q1"></a>
1. 中国式现代化的本质要求，说法正确的是（）
A. 同步富裕
B. 坚持党的领导
C. 单纯追求经济增速
D. 走西方现代化道路
[👉查看答案解析](职测A类解析卷.md#ans1)

<a id="q2"></a>
2. 下列文种用于答复下级请示的是（）
A. 通知
B. 批复
C. 报告
D. 函
[👉查看答案解析](职测A类解析卷.md#ans2)

## 第二部分 言语理解与表达（21‑40题）
<a id="q3"></a>
3. 基层治理要倾听民意，______群众合理诉求。
A. 回应
B. 敷衍
C. 回避
D. 淡化
[👉查看答案解析](职测A类解析卷.md#ans3)

## 第三部分 判断推理（41‑70题）
<a id="q4"></a>
4. 共情：体会他人情绪。下列属于共情的是（）
A. 嘲笑失利的同事
B. 安慰遭遇困境的朋友
C. 只顾自己利益
D. 漠视他人困难
[👉查看答案解析](职测A类解析卷.md#ans4)

## 第四部分 数量关系（71‑85题）
<a id="q5"></a>
5. 一项工程甲10天完成，乙15天完成，合作需要（）天
A.5
B.6
C.7
D.8
[👉查看答案解析](职测A类解析卷.md#ans5)

## 第五部分 资料分析（86‑100题）
<a id="q6"></a>
材料：2025年产值500亿，同比增长10%
6. 2024年产值约为（）
A.454.5
B.480
C.510
D.550
[👉查看答案解析](职测A类解析卷.md#ans6)
"""
    with open(filename, "w", encoding="utf‑8") as f:
        f.write(content)
    print(f"生成：{filename}")


def generate_zongying(today):
    filename = f"综应A类_{today}.md"
    content = f"""# 事业单位联考A类｜综合应用能力（{today}）
考试时长：120分钟｜满分：150分
岗位类型：综合管理A类

# 给定材料
材料1：
某街道便民服务大厅近期投诉增多：高峰排队久、窗口人员态度一般、线上系统卡顿、引导标识不清、群众重复提交材料。街道计划开展专项整改提升服务水平。

# 作答任务
<a id="case1"></a>
## 第一题（35分）
根据材料，概括便民大厅存在的主要问题。
要求：全面准确，条理清晰，200字以内。
[👉查看参考答案](综应A类解析卷.md#ans_case1)

<a id="case2"></a>
## 第二题（35分）
针对上述问题提出可落地的整改措施。
要求：针对性强，300字左右。
[👉查看参考答案](综应A类解析卷.md#ans_case2)

<a id="case3"></a>
## 第三题（40分）
撰写一份大厅服务提质专项整治活动通知，下发全体工作人员。
格式规范，400字左右。
[👉查看参考答案](综应A类解析卷.md#ans_case3)

<a id="case4"></a>
## 第四题（40分）
整改之后领导安排你开展督导检查，简述你的工作思路。
字数450字左右。
[👉查看参考答案](综应A类解析卷.md#ans_case4)
"""
    with open(filename, "w", encoding="utf‑8") as f:
        f.write(content)
    print(f"生成：{filename}")


if __name__ == "__main__":
    day = get_today()
    generate_zhice(day)
    generate_zongying(day)
