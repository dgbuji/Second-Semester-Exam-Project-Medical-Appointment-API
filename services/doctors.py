from fastapi import HTTPException

from schema.doctors import doctors, DoctorCreateEdit, Doctors

class DoctorsService:

    @staticmethod
    def parse_doctors(doctors_data):
        data = []
        for Doctors in doctors_data:
            data.append(doctors[Doctors])
        return data   

    @staticmethod
    def get_doctors_by_id(doctors_id):
        return doctors[doctors_id]
    
    @staticmethod
    def create_doctors(doctors_data: DoctorCreateEdit):
        id = len(doctors)
        new_doctors = Doctors(
        id=id,
        **doctors_data.model_dump()
    )
        doctors[id] = new_doctors
        return new_doctors
    
    @staticmethod
    def edit_doctors(doctors_id: int, payload: DoctorCreateEdit):
        if doctors_id not in doctors:
            raise HTTPException(detail='Doctor not found.', status_code=404)

        doctor = doctors[doctors_id]
        doctor.name = payload.name
        doctor.specialization = payload.specialization
        doctor.phone = payload.phone

        return doctor

    @staticmethod
    def delete_doctors(doctor_id: int):
        if doctor_id in doctors:
            del doctors[doctor_id]
            return {'message': 'Doctor deleted succesfully'}
        else:
            raise HTTPException(detail='Doctor not found.', status_code=404)