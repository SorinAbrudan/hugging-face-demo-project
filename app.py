from transformers import pipeline
import gradio as gr

model = pipeline("summarization")


def predict(prompt):
    return model(prompt)[0]["summary_text"]

textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
interface = gr.Interface(fn=predict, inputs=textbox, outputs="text")
interface.launch()