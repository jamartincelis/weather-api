from rest_framework import serializers

from budget.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    """
    Permite acceder a lo datos basicos de un presupuesto.
    """
    class Meta:
        model = Budget
        exclude = [
            'status'
        ]


class BudgetDetailSerializer(serializers.ModelSerializer):
    """
    Permite editar los datos basicos de un presupuesto.
    """
    class Meta:
        model = Budget
        exclude = [
            'status'
        ]
