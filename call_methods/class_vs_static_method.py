class employee:
    company="Google"

    @classmethod
    def change_company(cls, new_name):
        cls.company=new_name

    @staticmethod
    def change_company_static(new_name):
        company=new_name

employee.change_company("Microsoft")
print(employee.company)

employee.change_company_static("Amazon")
print(employee.company)