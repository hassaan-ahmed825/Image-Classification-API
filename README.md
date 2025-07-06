# Image-Classification-API
“Flask API for flower image classification using Transfer Learning (MobileNetV2).”

README FILE
 Flower Image Classification API
A production-ready Flask API for predicting flower types using Transfer Learning with TensorFlow and MobileNetV2.
________________________________________
Project Highlights
 Transfer Learning: Uses MobileNetV2 for accurate image classification
 Trained on Flowers Dataset: 5 flower categories: Daisy, Dandelion, Rose, Sunflower, Tulip
 REST API: Predict flower type by uploading an image
 Swagger UI: Simple interface to test the API in your browser
 Ready for Deployment: Can be hosted on any server
________________________________________
 Project Structure
.
├── flowers_model.keras          # Saved trained model
├── tensor_Api.py                # Flask API script
├── templates/                   # Swagger UI templates (if any)
├── flowers/                     # Flower dataset (not needed in production)
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation (this file!)
└── venv/                        # Virtual environment (should be in .gitignore)
________________________________________
 Flower Classes
•	Daisy
•	Dandelion
•	Rose
•	Sunflower
•	Tulip
________________________________________
 How It Works
1 Train Model
•	The model is trained using TensorFlow with MobileNetV2 as the base.
•	Transfer Learning improves accuracy with fewer resources.
2 API Endpoint
•	/predict — Send an image file via POST request.
•	The API returns the predicted flower type.
3 Test with Swagger UI
•	Open the provided Swagger link in your browser.
•	Upload an image.
•	See instant prediction results in JSON format.
________________________________________
Example Request
Request:
POST /predict
Body: { image: flower.jpg }
Response:
{
  "results": [
    {
      "filename": "example.jpg",
      "predicted_class": "daisy"
    }
  ]
}
________________________________________
How To Run Locally
1 Clone this repo
git clone https://github.com/YOUR_USERNAME/flower-classifier-api.git
cd flower-classifier-api
2 Create virtual environment
python -m venv venv
source venv/bin/activate  # On Linux/macOS
# OR
venv\Scripts\activate     # On Windows
3 Install dependencies
pip install -r requirements.txt
4 Run the API
python tensor_Api.py
5 Open Swagger UI
Visit http://127.0.0.1:5000/apidocs/
________________________________________
Deployment
You can easily deploy this API on:
•	Heroku
•	Render
•	Railway
•	AWS / GCP
________________________________________
 How To Use
•	Upload single or multiple flower images.
•	Get JSON predictions instantly.
•	Integrate into any web or mobile app.
________________________________________
What’s Included
✔ Clean, documented source code
✔ Ready-to-use trained model
✔ Swagger documentation for easy testing
✔ Example images for testing predictions
________________________________________
 Contact
Built by: Hassaan Ahmed
Email: hassaanahmed80400@gmail.com
GitHub: https://github.com/hassaan-ahmed825
________________________________________
This repo demonstrates ability to:
•	Build production-ready ML models
•	Deploy them as REST APIs
•	Provide clear documentation for clients & developers
________________________________________
Note: Accuracy can be improved by:
•	Using Early Stopping to prevent overfitting
•	Adding Data Augmentation (rotation, flipping, zoom)
•	Fine-tuning the base model layers
•	Training longer on more data



