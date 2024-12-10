import json
from urllib import request

# This is the ComfyUI api prompt format.

# If you want it for a specific workflow you can "enable dev mode options"
# in the settings of the UI (gear beside the "Queue Size: ") this will enable
# a button on the UI to save workflows in api format.

# keep in mind ComfyUI is pre alpha software so this format will change a bit.

# this is the one for the default workflow
prompt_text1 = """
{
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "cfg": 8,
            "denoise": 1,
            "latent_image": [
                "5",
                0
            ],
            "model": [
                "4",
                0
            ],
            "negative": [
                "7",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "sampler_name": "euler",
            "scheduler": "normal",
            "seed": 8566257,
            "steps": 20
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "v1-5-pruned-emaonly.safetensors"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "batch_size": 1,
            "height": 512,
            "width": 512
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "masterpiece best quality girl"
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "bad hands"
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [
                "3",
                0
            ],
            "vae": [
                "4",
                2
            ]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "8",
                0
            ]
        }
    }
}
"""


prompt_text = """{
    "1": {
        "inputs": {
            "ckpt_name": "dreamshaper_8.safetensors"
        },
        "class_type": "CheckpointLoaderSimple"
    },
    "2": {
        "inputs": {
            "seed": 1234,
            "steps": 30,
            "cfg": 8,
            "sampler_name": "dpmpp_2m_sde",
            "scheduler": "normal",
            "denoise": 1,
            "model": [
                "1",
                0
            ],
            "positive": [
                "3",
                0
            ],
            "negative": [
                "4",
                0
            ],
            "latent_image": [
                "5",
                0
            ]
        },
        "class_type": "KSampler"
    },
    "3": {
        "inputs": {
            "text": "cgmech, (realistic)\\nsolo, white mecha robot, cape, science fiction, torn clothes, glowing, standing, robot joints, mecha, armor, cowboy shot, (floating cape), intense sunlight, silver dragonborn, outdoors, landscape, nature\\n, ((masterpiece, best quality)),  <lora:cgmechmix_offset:1><lora:more_details:0.3>  <lora:Niji:0.5><lora:dragonborn_offset:0.7>\\n, volumetrics dtx, (film grain, blurry background, blurry foreground, bokeh, depth of field, motion blur:1.3)",
            "clip": [
                "1",
                1
            ]
        },
        "class_type": "CLIPTextEncode"
    },
    "4": {
        "inputs": {
            "text": "BadDream, FastNegativeV2",
            "clip": [
                "1",
                1
            ]
        },
        "class_type": "CLIPTextEncode"
    },
    "5": {
        "inputs": {
            "width": 512,
            "height": 512,
            "batch_size": 1
        },
        "class_type": "EmptyLatentImage"
    },
    "6": {
        "inputs": {
            "samples": [
                "2",
                0
            ],
            "vae": [
                "1",
                2
            ]
        },
        "class_type": "VAEDecode"
    },
    "7": {
        "inputs": {
            "images": [
                "6",
                0
            ]
        },
        "class_type": "PreviewImage"
    },
    "8": {
        "inputs": {
            "images": [
                "6",
                0
            ]
        },
        "class_type": "PreviewImage"
    },
    "9": {
        "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "6",
                0
            ]
        },
        "class_type": "SaveImage"
    }
}"""
prompt = json.loads(prompt_text1)
prompt = json.loads(prompt_text)


def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode("utf-8")
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)


import os

print(os.getcwd())
with open("ComfyUI/script_examples/valid_prompt.json", "r") as f:
    prompt = json.load(f)


queue_prompt(prompt)
