from models.employee import Employee
from exceptions.custom_exceptions import InvalidSalaryError
import utils.logger

try:

    emp1 = Employee(
        "Hamna",
        22,
        20000
    )

    emp1.display()

except InvalidSalaryError as e:

    print("Error:", e)

finally:

    print("Program Finished")