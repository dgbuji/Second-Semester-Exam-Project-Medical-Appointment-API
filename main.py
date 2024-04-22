from fastapi import FastAPI

from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointments import appointment_router

app = FastAPI()

app.include_router(patient_router, prefix= '/Patients', tags=['Patients'])
app.include_router(doctor_router, prefix= '/Doctors', tags=['Doctors'])
app.include_router(appointment_router, prefix='/Appointments', tags=['Appointments'] )

@app.get('/Home')
def index():
    return "Welcome to my Medical Appointment App"


