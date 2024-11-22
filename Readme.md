# Gradio: Build Machine Learning Web Apps — in Python

Gradio is an open-source Python library that is used to build machine learning and data science demos and web applications.

With Gradio, you can quickly create a beautiful user interface around your machine learning models or data science workflow and let people "try it out" by dragging-and-dropping in their own images, pasting text, recording their own voice, and interacting with your demo, all through the browser.

Gradio is useful for:

* **Demoing** your machine learning models for clients / collaborators / users / students

* **Deploying** your models quickly with automatic shareable links and getting feedback on model performance

* **Debugging** your model interactively during development using built-in manipulation and interpretation tools

**Get Started at [https://gradio.app/getting_started](https://gradio.app/getting_started).**

### This Template on Replit shows how to use the Gradio integration with [Hugging Face](https://huggingface.co/) through the Inference API to easily load and showcase a model in a web interface with one line of code.

## Quickstart

**Prerequisite**: Gradio requires Python 3.7 or above, that's it! 

### Hello, World ⚡

To get Gradio running with a simple "Hello, World" example, follow these three steps:

<span>1.</span> Install Gradio from pip. Note, the minimal supported Python version is 3.7.

```bash
pip install gradio
```

<span>2.</span> Run the code below as a Python script or in a Python notebook (or in a  [colab notebook](https://colab.research.google.com/drive/18ODkJvyxHutTN0P5APWyGFO_xwNcgHDZ?usp=sharing)).

```python
import gradio as gr
def greet(name):
    return "Hello " + name + "!!"
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
```

<span>3.</span> The demo below will appear automatically within the Python notebook, or pop in a browser on  [http://localhost:7860](http://localhost:7860/)  if running from a script.