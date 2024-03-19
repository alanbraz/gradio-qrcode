import gradio as gr
import segno, random

def qrcode(text_or_URL, color, bg, transp, border=None):
    qrcode = segno.make_qr(text_or_URL)
    path = "/tmp/qrcode-{}.png".format(random.randint(1,9999))
    qrcode.save(path, scale=100, dark=color, light=bg if not transp else None, border=border)
    return path

demo = gr.Interface(
    fn=qrcode,
    inputs=["text", 
            gr.ColorPicker(label="Code color", value="#000000"),
            gr.ColorPicker(label="Background color", value="#FFFFFF"),
            gr.Checkbox(label="Transparent background", value=False),
            gr.Slider(minimum=0, maximum=10, step=1, label="Border", value=2),
            ],
    outputs=["image"],
)

demo.launch()
