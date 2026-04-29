
def extraction_prompt(text):
    return f"""
提取合同关键条款：违约责任、支付条款、管辖权、保密条款
{text}
"""

def reasoning_prompt(clauses, knowledge):
    return f"""
结合知识库分析风险：
条款：{clauses}
知识：{knowledge}
输出风险点
"""

def review_prompt(clauses, risks):
    return f"""
生成审查报告：
条款：{clauses}
风险：{risks}
输出风险+修改建议
"""
