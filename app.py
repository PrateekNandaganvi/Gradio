import gradio as gr
gr.close_all()

def getDetails(name, age, preference, hobbies):
    return f"Name: {name}\nAge: {age}\nSubject Preference: {preference}\nHobbies: {', '.join(hobbies)}"

demo = gr.Interface(
    fn=getDetails,
    inputs=[
        gr.Textbox(label="Name:"),
        gr.Slider(label="Age:", min=0, max=70),
        gr.Radio(label="Subject Preference:", choices=['C', 'C++', 'Java', 'Python']),
        gr.CheckboxGroup(label="Hobbies:", choices=['Painting', 'Singing', 'Reading', 'Gaming'])
    ],
    outputs=[gr.Textbox()]
)

demo.launch()
