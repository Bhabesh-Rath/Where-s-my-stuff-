#!/usr/bin/env python
# TFLite FP32 conversion — run after:  pip install ai-edge-torch
import torch, ai_edge_torch

model = torch.load(
    "/kaggle/input/models/rath429/finetuned-pruned-model/pytorch/default/1/finetuned_model.pth", map_location="cpu", weights_only=False)
model.eval()
sample     = (torch.randn(1, 3, 224, 224),)
edge_model = ai_edge_torch.convert(model, sample)
edge_model.export("./eval_outputs/finetuned_model.tflite")
print("Saved:", "./eval_outputs/finetuned_model.tflite")
