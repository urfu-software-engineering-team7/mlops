import torch
from torchvision import models, transforms
import urllib.request
from PIL import Image
from fastapi import FastAPI
from io import BytesIO

app = FastAPI()

# Загрузка предобученной модели из PyTorch Hub
model = torch.hub.load('pytorch/vision', 'resnet18', pretrained=True)
model.eval()

# Преобразования изображения для соответствия требованиям модели
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Классы объектов, которые модель может распознавать
# Из числа получает имя породы
with urllib.request.urlopen('https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json') as url_file:
    labels = url_file.read().decode()
    labels = labels.split('\n')

# Функция для предсказания класса объекта на изображении
def predict_image(image):
    image = preprocess(image)
    image = torch.unsqueeze(image, 0)
    with torch.no_grad():
        output = model(image)
    _, predicted_idx = torch.max(output, 1)
    predicted_label = labels[predicted_idx.item()]
    return predicted_label

@app.post("/predict")
async def predict_post(url: str):
    image = None
    try:
        with urllib.request.urlopen(url) as url_file:
            image = Image.open(url_file)
            predicted_label = predict_image(image)
            return {"url": url, "predicted_label": predicted_label}
    except Exception as e:
        return {"error": str(e)}

@app.get("/predict")
async def predict_get(url: str):
    image = None
    try:
        with urllib.request.urlopen(url) as url_file:
            image = Image.open(url_file)
            predicted_label = predict_image(image)
            return {"url": url, "predicted_label": predicted_label}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
