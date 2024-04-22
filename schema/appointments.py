from datetime import date
from pydantic import BaseModel

from schema.doctors import Doctors, doctors
from schema.patients import Patients, patients

class Appointments(BaseModel):
    id: int
    patients: Patients
    doctors: Doctors
    date: date
    completed: bool

class AppointmentsCreate(BaseModel):
    patients: int
    doctors: int
    date: date

appointments: dict[int: Appointments] = {
    0: Appointments (id = 0, patients= patients[0], doctors= doctors[0], date= date(2024, 1, 30), completed= False),
    1: Appointments (id = 1, patients= patients[1], doctors= doctors[1], date= date(2024, 3, 30), completed= False)
}


