import gradio as gr


# 定义一个简单的函数，该函数将输入的文本原样返回
def greet(name):
    return f"你输入的文本是: {name}"


# 创建 Gradio 界面
# `gr.Interface` 是 Gradio 中用于创建界面的主要类
# fn：指定要调用的函数，这里是 greet 函数
# inputs：指定输入组件，这里使用文本输入框
# outputs：指定输出组件，这里使用文本输出框
# title：设置界面的标题
demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="请输入文本"),
    outputs=gr.Textbox(label="输出结果"),
    title="简单的 Gradio 演示"
)

# 启动 Gradio 应用
# `launch` 方法用于启动 Gradio 界面
demo.launch()
