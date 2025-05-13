from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sales,predict_churn_result

# Create the app instance
app = FastAPI()

# Define a request body model
class GreetRequest(BaseModel):
    name: str

# Define a simple GET route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI example!"}

# Define a POST route to greet a user
@app.post("/greet")
def greet_user(request: GreetRequest):
    return {"message": f"Hello user, {request.name}!"}

# def predict_sales_endpoint(item: ItemData):
#     prediction = predict_sales(item.dict())
#     return {"predicted_sales": prediction}


# # Define input data model
# class CustomerData(BaseModel):
#     tenure: float
#     MonthlyCharges: float
#     TotalCharges: float
#     Contract_One_year: int
#     Contract_Two_year: int

# # Define prediction endpoint
# @app.post("/predict/")
# def predict_churn(data: CustomerData):
#     input_data = np.array([[
#         data.tenure,
#         data.MonthlyCharges,
#         data.TotalCharges,
#         data.Contract_One_year,
#         data.Contract_Two_year
#     ]])
#     input_data_scaled = scaler.transform(input_data)
#     prediction = model.predict(input_data_scaled)
#     return {"Churn Prediction": "Yes" if prediction[0] == 1 else "No"}


class CustomerData(BaseModel):
    customerID: str
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    Contract: str

@app.post("/predict/churn/")
def predict_churn(data: CustomerData):
    prediction = predict_churn_result(data.dict())
    return {"predicted_churn": prediction}

