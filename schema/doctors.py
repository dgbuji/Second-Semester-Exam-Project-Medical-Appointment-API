from pydantic import BaseModel

class Doctors(BaseModel):
    id: int
    name: str
    specialization: str
    phone: str
    is_available: bool = True

class DoctorCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool = True


doctors: dict[int: Doctors] = {
    0: Doctors(id=0, name='doctor 0', specialization='Paediatrics', phone='0800', is_available=True),
    1: Doctors(id=1, name='doctor 1', specialization='Orthopedics', phone='0801', is_available=True),
    2: Doctors(id=2, name='doctor 2', specialization='Gynaecologist', phone='0802', is_available=True),
    3: Doctors(id=3, name='doctor 3', specialization='Oncologist', phone='0803', is_available=True)
}
