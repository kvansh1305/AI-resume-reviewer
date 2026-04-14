import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
import asyncio
from main import review_resume
from memory.memory_store import memory

def run_review(resume_text, job_desc):
    if not resume_text.strip():
        return "Please paste your resume text above."
    return asyncio.run(review_resume(resume_text, job_desc))

def clear_memory():
    memory.clear()
    return "Memory cleared. Starting fresh session."

with gr.Blocks(title="AI Resume Reviewer", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# AI Resume Reviewer & Improver")
    gr.Markdown("Paste your resume below to get structured feedback and rewrite suggestions.")

    with gr.Row():
        with gr.Column():
            resume_input = gr.Textbox(
                label="Resume Text",
                placeholder="Paste your full resume here...",
                lines=15
            )
            job_input = gr.Textbox(
                label="Job Description (optional)",
                placeholder="Paste the job posting to get tailored advice...",
                lines=5
            )
            with gr.Row():
                submit_btn = gr.Button("Review My Resume", variant="primary")
                clear_btn = gr.Button("Clear Memory")

        with gr.Column():
            output = gr.Textbox(
                label="Review & Suggestions",
                lines=25,
                interactive=False
            )

    submit_btn.click(run_review, inputs=[resume_input, job_input], outputs=output)
    clear_btn.click(clear_memory, outputs=output)

if __name__ == "__main__":
    demo.launch(share=True)