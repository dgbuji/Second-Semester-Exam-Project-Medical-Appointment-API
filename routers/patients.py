from fastapi import APIRouter

from schema.patients import patients, PatientsCreateEdit
from services.patients import PatientService

patient_router = APIRouter()

@patient_router.get('/', status_code=200)
def get_patients():
    data = PatientService.parse_patients(patients_data=patients)
    return {'message': 'Succesful', 'data': data}

@patient_router.get('/{patients_id}', status_code=200)
def get_patients_by_id(patients_id: int):
    data = PatientService.get_patients_by_id(patients_id)
    return {'message': 'successful', 'data': data}

@patient_router.post('/', status_code=201)
def create_patients(payload: PatientsCreateEdit):
    data = PatientService.create_patients(payload)
    return {'message': 'Patient Created Successfully', 'data': data}

@patient_router.put('/{patients_id}', status_code=200)
def edit_patients(patients_id: int, payload: PatientsCreateEdit):
    data = PatientService.edit_patients(patients_id, payload)
    return {'message': 'Patient Edited Successfully', 'data': data}

@patient_router.delete('/{patients_id}')
def delete_patient(patients_id: int):
    if PatientService.delete_patients(patients_id):
        return {'message': 'Patient deleted succesfully'}




