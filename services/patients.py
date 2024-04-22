from fastapi import HTTPException

from schema.patients import patients, PatientsCreateEdit, Patients


class PatientService:

    @staticmethod
    def parse_patients(patients_data):
        data = []
        for Patients in patients_data:
            data.append(patients[Patients])
        return data   

    @staticmethod
    def get_patients_by_id(patients_id):
        return patients[patients_id]
    
    @staticmethod
    def create_patients(patients_data: PatientsCreateEdit):
        id = len(patients)
        new_patients = Patients(
        id=id,
        **patients_data.model_dump()
    )
        patients[id] = new_patients
        return new_patients
    
    @staticmethod
    def edit_patients(patients_id: int, payload: PatientsCreateEdit):
        if patients_id not in patients:
            raise HTTPException(detail='Patient not found.', status_code=404)

        patient = patients[patients_id]
        patient.name = payload.name
        patient.age = payload.age
        patient.sex = payload.sex
        patient.weight = payload.weight
        patient.height = payload.height
        patient.phone = payload.phone

        return patient

    @staticmethod
    def delete_patients(patients_id: int):
        if patients_id in patients:
            del patients[patients_id]
            return {'message': 'Patient deleted succesfully'}
        else:
            raise HTTPException(detail='Patient not found.', status_code=404)
            

    
    
    
    


      



