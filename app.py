import gradio as gr
import segno, random

def qrcode(text_or_URL, color, bg, transp, border=None):
    qrcode = segno.make_qr(text_or_URL)
    path = "/tmp/qrcode-{}.png".format(random.randint(1,9999))
    qrcode.save(path, scale=100, dark=color, light=bg if not transp else None, border=border)
    return path

demo = gr.Interface(
    fn=qrcode,
    inputs=[gr.Text(label="URL or text"), 
            gr.ColorPicker(label="Code color", value="#000000"),
            gr.ColorPicker(label="Background color", value="#FFFFFF"),
            gr.Checkbox(label="Transparent background", value=False),
            gr.Slider(minimum=0, maximum=10, step=1, label="Border", value=2),
            ],
    outputs=["image"],
    title="Generate QR Code for free that never expires", 
    allow_flagging="never",
    description = "Source-code available at [github.com/alanbraz/gradio-qrcode](https://github.com/alanbraz/gradio-qrcode)",
    # article = "Check out [the original model](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english).",
    examples= [ [ "http://canal.pullrecast.dev", "#004ce2", "#000", True, 1], [ "https://www.ibm.com/br-pt", "#FFFFFF", "#0f62fe", False, 4] ]
)

demo.launch(share=False)# server_port=8080, server_name=None)