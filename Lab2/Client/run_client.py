from time import sleep
from read_client_dataset import get_client_dataset
from Mongo.mongodb_service import MongodbService
from sklearn.preprocessing import StandardScaler

storage = MongodbService.get_instance()
X_client, y_client = get_client_dataset()
X_client, X_client_columns = StandardScaler().fit_transform(X_client), X_client.columns


def predict(num):
    dto = {}
    for columnName, columnValue in zip(X_client_columns, X_client[num]):
        dto[columnName] = columnValue
    storage.set_input_transaction(dto)
    result = None
    while result is None:
        sleep(0.5)
        result = storage.get_output_transaction()
    return result


samples_len = X_client.shape[0]
print("There is {0} samples".format(samples_len))

ans = "y"
while ans == "y":
    sample_num = int(input("\nWrite down a number between 1 and {} to specify prediction sample: ".format(samples_len)))
    sample_num -= 1

    print("Predicting...")
    predicted = predict(sample_num)
    print("Expected:  {}".format(y_client.values[sample_num]))
    print("Predicted: {}".format(predicted))

    ans = input("Continue? y/n - ")

