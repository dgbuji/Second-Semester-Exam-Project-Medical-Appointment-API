from pydantic import BaseModel
from decimal import Decimal

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: Decimal
    height: Decimal
    phone: str

patients: dict[int: Patients] = {
    0: Patients(id=0, name='Patient 0', age=9, sex='male', weight=Decimal(29.0), height=Decimal(4.2), phone='0800'),
    1: Patients(id=1, name='Patient 1', age=29, sex='female', weight=Decimal(59.0), height=Decimal(4.8), phone='0801'),
    2: Patients(id=2, name='Patient 2', age=39, sex='male', weight=Decimal(89.0), height=Decimal(6.2), phone='0802'),
    3: Patients(id=3, name='Patient 3', age=29, sex='female', weight=Decimal(49.0), height=Decimal(5.), phone='0803')
}


