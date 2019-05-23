from rest_framework import serializers
from api.models import Item, Employee, Shift, Machine, Line, ProdGoal, ProdSnap
from django.db.models.fields.related import ForeignKey

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "number",
            "description",
            "p182_conversion"
            )

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "emp_id",
            "first_name",
            "middle_name",
            "last_name",
            "suffix",
            "birth_date",
            "language",
            "supervisor",
            "manager",
            "certificates",
            "med_restrictions"
            )

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = (
            "number",
            "start_time",
            "end_time"
            )


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = (
            "number"
            )


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = (
            "name",
            "line"
            )


class ProdGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdGoal
        fields = (
            "date",
            "quantity",
            "item"
            )


class ProdSnapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdSnap
        field = (
            "shifts",
            "employees",
            "line",
            "machines",
            "item",
            "quant",
            "date",
            "timestamp"
            )
