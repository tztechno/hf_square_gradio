import gradio as gr

def square_number(x: float) -> float:
    return x * x

demo = gr.Interface(
    fn=square_number,
    inputs=gr.Number(label="Enter a number"),
    outputs=gr.Number(label="Square of the number"),
    title="Number Squaring Calculator",
    description="Enter a number and get its square value"
)

if __name__ == "__main__":
    demo.launch(share=True) 
