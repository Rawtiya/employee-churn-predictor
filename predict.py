
def predict_new(model, new_data):
    return model.predict(new_data)

if __name__ == "__main__":
    from churn_model import train_model
    model = train_model([[25, 2], [30, 5], [45, 10], [50, 3]], [0, 1, 1, 0])
    print(predict_new(model, [[28, 4]]))
