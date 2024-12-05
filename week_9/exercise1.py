class ComputerLecturer(object):
    salary = 100000
    monthly_bonus = 500
    def __init__(self, name, age, address, phone,
        programming_modules):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_modules = programming_modules


# class LinguisticsLecturer(object):
#     salary = 100000
#     monthly_bonus = 500
#     def __init__(self, name, age, address, phone, bilingual):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.phone = phone
#         self.bilingual = bilingual



# Optimised code
class LinguisticsLecturer(ComputerLecturer):
    def __init__(self, name, age, address, phone, bilingual, programming_modules):
        super().__init__(name, age, address, phone, programming_modules)
        self.bilingual = bilingual

linguisticsLecturer = LinguisticsLecturer('Logesh', 28, 'B15 3SS','8608922177', True, 'SWW1')

print(f'Lecturer name {linguisticsLecturer.name}\n'
      f'Lecturer age {linguisticsLecturer.age}\n'
      f'Lecturer address {linguisticsLecturer.address}\n'
      f'Lecturer phone {linguisticsLecturer.phone}\n'
      f'Lecturer bilingual {linguisticsLecturer.bilingual}\n'
      f'Lecturer programming_modules {linguisticsLecturer.programming_modules}\n'
      f'Lecturer salary {linguisticsLecturer.salary}\n'
      f'Lecturer monthly_bonus {linguisticsLecturer.monthly_bonus}\n')