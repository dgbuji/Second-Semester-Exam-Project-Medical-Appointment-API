from fastapi import HTTPException
from schema.appointments import Appointments, AppointmentsCreate, appointments
from schema.doctors import doctors
from schema.patients import patients

class AppointmentService:

    @staticmethod
    def parse_appointments(appointments_data):
        data = []
        for Appointments in appointments_data:
            data.append(appointments[Appointments])
        return data 

    @staticmethod
    def get_first_available_doctor_id():
        for doctor_id, doctor in doctors.items():
            if doctor.is_available:
                return doctor_id
        return None


    @staticmethod
    def create_appointment(appointment: AppointmentsCreate) -> Appointments:
        # Check if patient ID is valid since its only patients that can book appointments
        if appointment.patients not in patients:
            raise HTTPException(status_code=404, detail="Patient not found and does not exist")
        
        # Check if doctor is available
        available_doctors = [doctor for doctor in doctors.values() if doctor.is_available]
        if not available_doctors:
            raise HTTPException(status_code=400, detail="No available doctors")
        
        # Get the first available doctor
        first_available_doctor = available_doctors[0]

        # Create the appointment
        new_appointment = Appointments(
            id=len(appointments),
            patients=patients[appointment.patients],
            doctors=first_available_doctor,
            date=appointment.date,
            completed=False
        )
        appointments[id] = new_appointment
        first_available_doctor.is_available = False  # Mark doctor as unavailable
        return new_appointment.model_dump()
    
    
    @staticmethod
    def cancel_appointment(appointment_id: int):
        if appointment_id in appointments:
            appointment = appointments[appointment_id]
            if not appointment.completed:  # Check if appointment is not completed
                doctor_id = appointment.doctors.id
                doctors[doctor_id].is_available = True
                appointments.pop(appointment_id)
                return {'message': 'Appointment cancelled successfully'}
            else:
                raise HTTPException(status_code=400, detail="Cannot cancel a completed appointment")
        else:
            raise HTTPException(status_code=404, detail="Appointment not found")


    @staticmethod
    def complete_appointment(appointment_id: int):
        if appointment_id in appointments:
            appointment = appointments[appointment_id]
            appointment.completed = True
            # Mark the doctor as available again
            doctor_id = appointment.doctors.id
            doctors[doctor_id].is_available = True
            return {'message': 'Appointment completed successfully'}
        else:
            raise HTTPException(status_code=404, detail="Appointment not found")
   