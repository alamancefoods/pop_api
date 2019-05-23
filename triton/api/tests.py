from django.test import TestCase
from model_mommy import mommy
from api.models import Item, Employee, Shift, Line, Machine, ProdGoal, ProdSnap
# Create your tests here.

class ItemTest(TestCase):

    def test_item(self):
        item = mommy.make(Item)
        self.assertTrue(isinstance(item, Item))


class EmployeeTest(TestCase):

    def test_employee(self):
        employee = mommy.make(Employee)
        self.assertTrue(isinstance(employee, Employee))


class ShiftTest(TestCase):

    def test_shift(self):
        shift = mommy.make(Shift)
        self.assertTrue(isinstance(shift, Shift))


class LineTest(TestCase):

    def test_line(self):
        line = mommy.make(Line)
        self.assertTrue(isinstance(line, Line))


class MachineTest(TestCase):

    def test_machine(self):
        machine = mommy.make(Machine)
        self.assertTrue(isinstance(machine, Machine))


class ProdGoalTest(TestCase):

    def test_prod_goal(self):
        prod_goal = mommy.make(ProdGoal)
        self.assertTrue(isinstance(prod_goal, ProdGoal))


class ProdSnapTest(TestCase):

    def test_prod_snap(self):
        prod_snap = mommy.make(ProdSnap)
        self.assertTrue(isinstance(prod_snap, ProdSnap))
