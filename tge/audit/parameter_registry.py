"""
parameter_registry.py - Registro de Proveniência e Auditoria de Parâmetros da TGE
Gerencia o catálogo rigoroso de todos os parâmetros, constantes e hipóteses utilizados no código.
"""

from enum import Enum
from typing import Dict, Any, Optional, List


class ParameterType(Enum):
    DERIVED = "DERIVADO"
    OBSERVATIONAL = "OBSERVACIONAL"
    EXPERIMENTAL = "EXPERIMENTAL"
    FITTED = "CALIBRADO"
    HYPOTHESIS = "HIPÓTESE"
    HARD_CODED = "INSERIDO"


class ProvenanceParameter:
    def __init__(
        self,
        name: str,
        value: Any,
        param_type: ParameterType,
        source: str,
        description: str,
        derivation_formula: Optional[str] = None,
        uncertainty: Optional[float] = None,
        module: Optional[str] = None,
        line_number: Optional[int] = None
    ):
        self.name = name
        self.value = value
        self.param_type = param_type
        self.source = source
        self.description = description
        self.derivation_formula = derivation_formula
        self.uncertainty = uncertainty
        self.module = module
        self.line_number = line_number

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value,
            "type": self.param_type.value,
            "source": self.source,
            "description": self.description,
            "derivation_formula": self.derivation_formula,
            "uncertainty": self.uncertainty,
            "module": self.module,
            "line_number": self.line_number
        }


class ParameterRegistry:
    def __init__(self):
        self._parameters: Dict[str, ProvenanceParameter] = {}

    def register(self, param: ProvenanceParameter):
        self._parameters[param.name] = param

    def get(self, name: str) -> Optional[ProvenanceParameter]:
        return self._parameters.get(name)

    def list_by_type(self, param_type: ParameterType) -> List[ProvenanceParameter]:
        return [p for p in self._parameters.values() if p.param_type == param_type]

    def export_report(self) -> List[Dict[str, Any]]:
        return [p.to_dict() for p in self._parameters.values()]


# Registro Global Padrão da TGE
global_registry = ParameterRegistry()
