from fastapi import APIRouter

from schema.doctors import doctors, DoctorCreateEdit
from services.doctors import DoctorsService

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctors():
    data = DoctorsService.parse_doctors(doctors_data=doctors)
    return {'message': 'Succesful', 'data': data}

@doctor_router.get('/{doctors_id}', status_code=200)
def get_doctors_by_id(doctors_id: int):
    data = DoctorsService.get_doctors_by_id(doctors_id)
    return {'message': 'successful', 'data': data}

@doctor_router.post('/', status_code=201)
def create_doctors(payload: DoctorCreateEdit):
    data = DoctorsService.create_doctors(payload)
    return {'message': 'Doctor Created Successfully', 'data': data}

@doctor_router.put('/{doctors_id}', status_code=200)
def edit_doctors(doctors_id: int, payload: DoctorCreateEdit):
    data = DoctorsService.edit_doctors(doctors_id, payload)
    return {'message': 'Doctor Edited Successfully', 'data': data}

@doctor_router.put('/doctors/{doctor_id}/status', status_code=200)
def update_doctor_availability(doctor_id: int, is_available: bool):    
    doctor = doctors[doctor_id]  
    doctor.is_available = is_available
    return {"message": f"Doctor {doctor_id} availability updated successfully to {'available' if is_available else 'unavailable'}"}

@doctor_router.delete('/{doctors_id}')
def delete_doctors(doctors_id: int):
    if DoctorsService.delete_doctors(doctors_id):
        return {'message': 'Doctor deleted succesfully'}



    