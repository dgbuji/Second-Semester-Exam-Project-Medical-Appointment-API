from fastapi import APIRouter, HTTPException
from datetime import date

from schema.appointments import Appointments, AppointmentsCreate, appointments
from services.appointments import AppointmentService
from schema.doctors import doctors
from schema.patients import patients

appointment_router = APIRouter()

@appointment_router.get('/', status_code=200)
def get_appointments():
    data = AppointmentService.parse_appointments(appointments_data=appointments)
    return {'message': 'Succesful', 'data': data}

@appointment_router.post("/", response_model=dict, status_code= 201)
def create_appointment(appointment: AppointmentsCreate):
    return AppointmentService.create_appointment(appointment)

@appointment_router.delete("/{appointment_id}")
def cancel_appointment(appointment_id: int):
    return AppointmentService.cancel_appointment(appointment_id)

@appointment_router.put("/{appointment_id}")
def complete_appointment(appointment_id: int):
    return AppointmentService.complete_appointment(appointment_id)

