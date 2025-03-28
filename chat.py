from fastapi import FastAPI, Request
from pydantic import BaseModel
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import json
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust according to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Question(BaseModel):
    question: str

genai.configure(api_key=os.getenv("GEMINI"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Sample responses (Replace with actual model integration)
resume="""
Suharsh Agrawal

Bhopal, Madhya Pradesh

 +91 8269469177 # suharshsuyash@gmail.com ï LinkedIn ¬ GitHub

Education
Indian Institute of Technology Dharwad December 2022 - 2026
Bachelor of Technology in civil and infrastructure engineering CGPA-7.02 Dharwad, India
– Relevant Coursework: Operating Systems, Computer Networks, Data Structure & Algorithms, Database
Management System, Object-Oriented Programming
Experience
Machine Learning Research Ongoing
Deep Learning Research Project Under the guidance of Professor [Achyut Mani Tripathi]
– Trained models using ResNet-80 and ResNet-50 architectures on the CIFAR-10 dataset to achieve high classification accuracy.
– Applied self-learning techniques to enhance model performance and conducted experiments to optimize training workflows.
– Developed expertise in leveraging deep learning frameworks for image classification tasks.
Projects
Invoice Similarity Comparison System July 2024
– Constructed a system to process and compare invoices using OCR and text similarity metrics, achieving 90% accuracy in
document comparison.
– Executed PDF-to-image conversion, Tesseract OCR text extraction, and similarity analysis based on extracted fields.
RC Cars | Website June 2024
– Engineered a real-time car listing platform utilizing React.js and Node.js, with a responsive design ensuring 99% mobile
compatibility and 30% faster load times compared to the previous system.
– Established secure admin access with CRUD operations, cutting down listing management time by 40%.
Achievements
• Solved over 200+ questions on various coding platforms, showcasing strong problem-solving skills.
• Currently serving as the Cricket Club Secretary at IIT Dharwad, managing team activities and events.
• Mentored over 100+ students in my startup idea during the first year of college with a team of 20+ students.
• Represented IIT Dharwad as the Contingent Leader for two consecutive years at the Inter-IIT Sports Meet.
• Organized and participated in various college events, including Parsec Tech Fest at IIT Dharwad.
• Actively contributed to multiple clubs, including the Institute Innovation Council, fostering a culture of innovation.
Technical Skills
Languages: C++, Python, JavaScript, HTML/CSS
Web Development: React.js
Machine Learning: TensorFlow, Matplotlib, pytorch, supervised and unsupervised learning methods.
"""



@app.post("/chatbot")
async def chatbot(request: Question):
    user_question = request.question.lower()
    prompt=f"""
You are Suharsh Agrawal avatar. You are a chatbot that can answer questions about Suharsh's projects, resume, and skills.
You are not allowed to answer any other question other than suharsh. If the user asks about anything else, just say "I'm not sure, but feel free to ask about my projects, resume, or skills!".
You can use the information below to answer the questions.
Resume:
{resume}

User Question: {user_question}
Assistant:
"""
    response = model.generate_content([prompt], safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }, generation_config={"temperature": 0})

    print(response.text)
    
    
    return {"answer": response.text}

