from setfit import SetFitModel


model_path = "ml_models/model_v1"
model = SetFitModel.from_pretrained(model_path)

def model_predict(message):
    if message == "":
        return ""
    prediction = model.predict(message)
    return prediction