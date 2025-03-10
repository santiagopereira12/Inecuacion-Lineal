# Análisis de Restricciones Lineales en una Empresa

Este proyecto implementa un sistema de solución gráfica para inecuaciones lineales en el contexto de una empresa. Se representa la región factible de producción basada en restricciones de recursos.

## Descripción del Código

El código en Python utiliza las bibliotecas `numpy` y `matplotlib` para visualizar gráficamente un conjunto de restricciones lineales. Estas restricciones pueden representar limitaciones en la producción, el uso de materiales o la asignación de recursos en la empresa.

### Restricciones Modeladas

El sistema de ecuaciones utilizado en este código es:

```math
2A + 3B \leq 120
```
```math
3A + 2B \leq 150
```

Donde:
- `A` y `B` representan las cantidades de dos productos o recursos dentro del sistema.
- Se determinan los valores máximos de `A` y `B` en función de las restricciones dadas.

### Funcionamiento del Código

1. Se definen funciones que representan las restricciones y despejan `B` en función de `A`.
2. Se genera un rango de valores para `A` dentro de su límite factible.
3. Se calculan los valores correspondientes de `B` según las restricciones.
4. Se grafica la región factible rellenando el área donde ambas restricciones se cumplen.
5. Se presentan las curvas de las restricciones con etiquetas y una cuadrícula para mejorar la visualización.

## Instalación y Uso

### Requisitos
Para ejecutar este código, es necesario tener instalado Python junto con las siguientes bibliotecas:

```bash
pip install numpy matplotlib
```

### Ejecución
Guarde el código en un archivo `grafico_restricciones.py` y ejecute:

```bash
python grafico_restricciones.py
```

Esto generará una gráfica con las restricciones y la región factible de la solución.

## Aplicación en la Empresa
Este análisis es útil para evaluar la cantidad óptima de recursos que se pueden asignar a la producción sin exceder las restricciones establecidas. Puede aplicarse en la planificación de manufactura, distribución y optimización de costos.

---

© 2025 Empresa CoursesBKD. Todos los derechos reservados.

